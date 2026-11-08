# SayCan Robot Pick-and-Place Prompt and LLM/Affordance Scoring

Title: SayCan Robot Pick-and-Place Prompt and LLM/Affordance Scoring
Source-URL: https://raw.githubusercontent.com/google-research/google-research/master/saycan/SayCan-Robot-Pick-Place.ipynb
Source-Repo-or-Site: google-research/google-research (github.com/google-research/google-research)
Original-Path: saycan/SayCan-Robot-Pick-Place.ipynb (cells 2,41,42,43,44,47,48,52,53)
Category: 25-embodied-robotics (language goals into robot plans/code with perception feedback)
Tags: saycan,affordance-grounding,llm-scoring,pick-place,embodied-planning
Retrieved: 2026-11-08
Value-Note: Say (LLM likelihood) times Can (affordance value) scoring grounds fluent plans in what this body can actually do now; judgement under embodiment limits.
Truncation-Note: Relevant prompt/scoring cell sources reproduced verbatim; environment, ViLD, model and training cells omitted; cell separators added by collector; outputs/metadata omitted. Full notebook (3067 lines JSON) at Source-URL.

--- ORIGINAL ---

````python
# %% [markdown] cell 2  (separator added by collector)
# SayCan on a Robot Pick and Place Tabletop Environment

[SayCan](https://say-can.github.io/) is an algorithm that grounds large language models with robotic affordances for long-horizon planning. Given a set of low-level robotic skills (e.g., "put the green block in the red bowl") and a high-level instruction (e.g., "stack all the blocks"), it scores what a language model believes will help forward the high-level instruction and scores what a robotic affordance model believes is possible. Together these give a task that is useful and possible and the robot executes the command.

<img src="https://github.com/say-can/say-can.github.io/blob/main/img/saycan.png?raw=true" height="320px">

This colab runs an example of SayCan for a pick and place robot on a table top.

<img src="https://raw.githubusercontent.com/say-can/say-can.github.io/main/img/open_source_tabletop.png" height="320px">

Models used: [GPT-3](https://arxiv.org/abs/2005.14165) (InstructGPT), [CLIP](https://arxiv.org/abs/2103.00020) (ViT-B/32), [ViLD](https://arxiv.org/abs/2104.13921), and [CLIPort](https://cliport.github.io/) variant ([Transporter Nets](https://transporternets.github.io/))

### **Quick Start:**

**Step 1.** Register for an [OpenAI API key](https://openai.com/blog/openai-api/) to use GPT-3 (there's a free trial) and enter it below

**Step 2.** Menu > Change runtime type > Hardware accelerator > "GPU"

**Step 3.** Menu > Runtime > Run all

# %% [code] cell 41  (separator added by collector)
#@title LLM Scoring

def gpt3_call(engine="text-ada-001", prompt="", max_tokens=128, temperature=0, 
              logprobs=1, echo=False):
  full_query = ""
  for p in prompt:
    full_query += p
  id = tuple((engine, full_query, max_tokens, temperature, logprobs, echo))
  if id in LLM_CACHE.keys():
    print('cache hit, returning')
    response = LLM_CACHE[id]
  else:
    response = openai.Completion.create(engine=engine, 
                                        prompt=prompt, 
                                        max_tokens=max_tokens, 
                                        temperature=temperature,
                                        logprobs=logprobs,
                                        echo=echo)
    LLM_CACHE[id] = response
  return response

def gpt3_scoring(query, options, engine="text-ada-001", limit_num_options=None, option_start="\n", verbose=False, print_tokens=False):
  if limit_num_options:
    options = options[:limit_num_options]
  verbose and print("Scoring", len(options), "options")
  gpt3_prompt_options = [query + option for option in options]
  response = gpt3_call(
      engine=engine, 
      prompt=gpt3_prompt_options, 
      max_tokens=0,
      logprobs=1, 
      temperature=0,
      echo=True,)
  
  scores = {}
  for option, choice in zip(options, response["choices"]):
    tokens = choice["logprobs"]["tokens"]
    token_logprobs = choice["logprobs"]["token_logprobs"]

    total_logprob = 0
    for token, token_logprob in zip(reversed(tokens), reversed(token_logprobs)):
      print_tokens and print(token, token_logprob)
      if option_start is None and not token in option:
        break
      if token == option_start:
        break
      total_logprob += token_logprob
    scores[option] = total_logprob

  for i, option in enumerate(sorted(scores.items(), key=lambda x : -x[1])):
    verbose and print(option[1], "\t", option[0])
    if i >= 10:
      break

  return scores, response

def make_options(pick_targets=None, place_targets=None, options_in_api_form=True, termination_string="done()"):
  if not pick_targets:
    pick_targets = PICK_TARGETS
  if not place_targets:
    place_targets = PLACE_TARGETS
  options = []
  for pick in pick_targets:
    for place in place_targets:
      if options_in_api_form:
        option = "robot.pick_and_place({}, {})".format(pick, place)
      else:
        option = "Pick the {} and place it on the {}.".format(pick, place)
      options.append(option)

  options.append(termination_string)
  print("Considering", len(options), "options")
  return options

# %% [code] cell 42  (separator added by collector)
query = "To pick the blue block and put it on the red block, I should:\n"
options = make_options(PICK_TARGETS, PLACE_TARGETS)
scores, response = gpt3_scoring(query, options, engine=ENGINE, limit_num_options=5, option_start='\n', verbose=True)

# %% [code] cell 43  (separator added by collector)
#@title Helper Functions

def build_scene_description(found_objects, block_name="box", bowl_name="circle"):
  scene_description = f"objects = {found_objects}"
  scene_description = scene_description.replace(block_name, "block")
  scene_description = scene_description.replace(bowl_name, "bowl")
  scene_description = scene_description.replace("'", "")
  return scene_description

def step_to_nlp(step):
  step = step.replace("robot.pick_and_place(", "")
  step = step.replace(")", "")
  pick, place = step.split(", ")
  return "Pick the " + pick + " and place it on the " + place + "."

def normalize_scores(scores):
  max_score = max(scores.values())  
  normed_scores = {key: np.clip(scores[key] / max_score, 0, 1) for key in scores}
  return normed_scores

def plot_saycan(llm_scores, vfs, combined_scores, task, correct=True, show_top=None):
  if show_top:
    top_options = nlargest(show_top, combined_scores, key = combined_scores.get)
    # add a few top llm options in if not already shown
    top_llm_options = nlargest(show_top // 2, llm_scores, key = llm_scores.get)
    for llm_option in top_llm_options:
      if not llm_option in top_options:
        top_options.append(llm_option)
    llm_scores = {option: llm_scores[option] for option in top_options}
    vfs = {option: vfs[option] for option in top_options}
    combined_scores = {option: combined_scores[option] for option in top_options}

  sorted_keys = dict(sorted(combined_scores.items()))
  keys = [key for key in sorted_keys]
  positions = np.arange(len(combined_scores.items()))
  width = 0.3

  fig = plt.figure(figsize=(12, 6))
  ax1 = fig.add_subplot(1,1,1)

  plot_llm_scores = normalize_scores({key: np.exp(llm_scores[key]) for key in sorted_keys})
  plot_llm_scores = np.asarray([plot_llm_scores[key] for key in sorted_keys])
  plot_affordance_scores = np.asarray([vfs[key] for key in sorted_keys])
  plot_combined_scores = np.asarray([combined_scores[key] for key in sorted_keys])
  
  ax1.bar(positions, plot_combined_scores, 3 * width, alpha=0.6, color="#93CE8E", label="combined")
    
  score_colors = ["#ea9999ff" for score in plot_affordance_scores]
  ax1.bar(positions + width / 2, 0 * plot_combined_scores, width, color="#ea9999ff", label="vfs")
  ax1.bar(positions + width / 2, 0 * plot_combined_scores, width, color="#a4c2f4ff", label="language")
  ax1.bar(positions - width / 2, np.abs(plot_affordance_scores), width, color=score_colors)
  
  plt.xticks(rotation="vertical")
  ax1.set_ylim(0.0, 1.0)

  ax1.grid(True, which="both")
  ax1.axis("on")

  ax1_llm = ax1.twinx()
  ax1_llm.bar(positions + width / 2, plot_llm_scores, width, color="#a4c2f4ff", label="language")
  ax1_llm.set_ylim(0.01, 1.0)
  plt.yscale("log")
  
  font = {"fontname":"Arial", "size":"16", "color":"k" if correct else "r"}
  plt.title(task, **font)
  key_strings = [key.replace("robot.pick_and_place", "").replace(", ", " to ").replace("(", "").replace(")","") for key in keys]
  plt.xticks(positions, key_strings, **font)
  ax1.legend()
  plt.show()

# %% [code] cell 44  (separator added by collector)
#@title Affordance Scoring
#@markdown Given this environment does not have RL-trained policies or an asscociated value function, we use affordances through an object detector.

def affordance_scoring(options, found_objects, verbose=False, block_name="box", bowl_name="circle", termination_string="done()"):
  affordance_scores = {}
  found_objects = [
                   found_object.replace(block_name, "block").replace(bowl_name, "bowl") 
                   for found_object in found_objects + list(PLACE_TARGETS.keys())[-5:]]
  verbose and print("found_objects", found_objects)
  for option in options:
    if option == termination_string:
      affordance_scores[option] = 0.2
      continue
    pick, place = option.replace("robot.pick_and_place(", "").replace(")", "").split(", ")
    affordance = 0
    found_objects_copy = found_objects.copy()
    if pick in found_objects_copy:
      found_objects_copy.remove(pick)
      if place in found_objects_copy:
        affordance = 1
    affordance_scores[option] = affordance
    verbose and print(affordance, '\t', option)
  return affordance_scores

# %% [markdown] cell 47  (separator added by collector)
## **SayCan**

Here we implement SayCan with LLM scoring and robotic affordances from ViLD (in the absence of a trained value function from an RL policy).

# %% [code] cell 48  (separator added by collector)
#@title Prompt

termination_string = "done()"

gpt3_context = """
objects = [red block, yellow block, blue block, green bowl]
# move all the blocks to the top left corner.
robot.pick_and_place(blue block, top left corner)
robot.pick_and_place(red block, top left corner)
robot.pick_and_place(yellow block, top left corner)
done()

objects = [red block, yellow block, blue block, green bowl]
# put the yellow one the green thing.
robot.pick_and_place(yellow block, green bowl)
done()

objects = [yellow block, blue block, red block]
# move the light colored block to the middle.
robot.pick_and_place(yellow block, middle)
done()

objects = [blue block, green bowl, red block, yellow bowl, green block]
# stack the blocks.
robot.pick_and_place(green block, blue block)
robot.pick_and_place(red block, green block)
done()

objects = [red block, blue block, green bowl, blue bowl, yellow block, green block]
# group the blue objects together.
robot.pick_and_place(blue block, blue bowl)
done()

objects = [green bowl, red block, green block, red bowl, yellow bowl, yellow block]
# sort all the blocks into their matching color bowls.
robot.pick_and_place(green block, green bowl)
robot.pick_and_place(red block, red bowl)
robot.pick_and_place(yellow block, yellow bowl)
done()
"""

use_environment_description = False
gpt3_context_lines = gpt3_context.split("\n")
gpt3_context_lines_keep = []
for gpt3_context_line in gpt3_context_lines:
  if "objects =" in gpt3_context_line and not use_environment_description:
    continue
  gpt3_context_lines_keep.append(gpt3_context_line)

gpt3_context = "\n".join(gpt3_context_lines_keep)
print(gpt3_context)

# %% [markdown] cell 52  (separator added by collector)
## Socratic Model: VILD, GPT3, CLIPort

This implements a version of LLM planning shown in [Socratic Models](https://socraticmodels.github.io/), without the grounding, but with a scene description. For this relatively simple environment with clear robotic affordances, the scene description is generally sufficient. This mirrors the implementation attached to the paper [here](https://github.com/google-research/google-research/tree/master/socraticmodels).

# %% [code] cell 53  (separator added by collector)
#@title Prompt

gpt3_context = """
objects = [red block, yellow block, blue block, green bowl]
# move all the blocks to the top left corner.
robot.pick_and_place(blue block, top left corner)
robot.pick_and_place(red block, top left corner)
robot.pick_and_place(yellow block, top left corner)
done()

objects = [red block, yellow block, blue block, green bowl]
# put the yellow one the green thing.
robot.pick_and_place(yellow block, green bowl)
done()

objects = [yellow block, blue block, red block]
# move the light colored block to the middle.
robot.pick_and_place(yellow block, middle)
done()

objects = [blue block, green bowl, red block, yellow bowl, green block]
# stack the blocks.
robot.pick_and_place(green block, blue block)
robot.pick_and_place(red block, green block)
done()

objects = [red block, blue block, green bowl, blue bowl, yellow block, green block]
# group the blue objects together.
robot.pick_and_place(blue block, blue bowl)
done()

objects = [green bowl, red block, green block, red bowl, yellow bowl, yellow block]
# sort all the blocks into their matching color bowls.
robot.pick_and_place(green block, green bowl)
robot.pick_and_place(red block, red bowl)
robot.pick_and_place(yellow block, yellow bowl)
done()
"""


````
