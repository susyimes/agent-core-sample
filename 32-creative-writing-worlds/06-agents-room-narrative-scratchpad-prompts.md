# Agents' Room (DeepMind, ICLR 2025) - narrative generation through multi-step collaboration: Appendix B agent prompt templates

Title: Agents' Room (DeepMind, ICLR 2025) - narrative generation through multi-step collaboration: Appendix B agent prompt templates
Source-URL: https://ar5iv.labs.arxiv.org/html/2410.02603
Source-Repo-or-Site: arXiv:2410.02603 (Huot et al., Agents' Room)
Original-Path: ar5iv HTML, Appendix B scratchpad formatting and prompt templates (planning agents CONFLICT/CHARACTER/SETTING/PLOT + writing agents)
Category: 32-creative-writing-worlds/multiagent-writers-room
Tags: agents-room, deepmind, tell-me-a-story, scratchpad, planning-agents, writing-agents, narrative-theory
Retrieved: 2026-11-08
Value-Note: A writers' room as cognition: specialized planning agents fill a shared scratchpad (conflict, characters, setting, plot) before section writers draft - narrative identity is negotiated between roles rather than emitted by one voice.
NOTE: Extracted as text from ar5iv HTML (tags stripped); Appendix B reproduced from its heading to paper end (HTML tags stripped; tables flattened to text). Full original: https://ar5iv.labs.arxiv.org/html/2410.02603

--- ORIGINAL ---
~~~~text
Appendix B Specialized Agents’ Prompt Templates

Each specialized LLM-based agent has a specific prompt template that formats the scratchpad into a suitable prompt for the LLM call.

B.1 Scratchpad

Concretely, the scratchpad is typically formatted as follows:

[Scratchpad] Format

[Creative Writing Task]
<<the original writing prompt>>
[Central Conflict]
<<the output of the conflict agent>>

[Character Descriptions]
<<the output of the character agent>>

[Setting]
<<the output of the setting agent>>

[Key Plot Points]
<<the output of the plot agent>>

[Exposition]
<<the output of the exposition agent>>

[Rising Action]
<<the output of the rising action agent>>

[Climax]
<<the output of the climax agent>>

[Falling Action]
<<the output of the falling action agent>>

[Resolution]
<<the output of the resolution agent>>

The number and order of items in the scratchpad is of course a function of which agents have been called so far.

B.2 Planning Agents

[Conflict] Agent Prompt

Given
<<identifiers found in the scratchpad>>,
describe the central conflict in detail (more than 5 sentences). The description should answer the following questions:

⋆\star 

What’s the protagonist’s main goal in this story?

⋆\star 

Why do they want it?

⋆\star 

What’s stopping them from achieving it?

<<scratchpad>>

[Character] Agent Prompt

Given
<<identifiers found in the scratchpad>>,
describe the characters in detailed bullet points (more than 5
sentences for each character). The description should answer the
following questions:

⋆\star 

What do the characters sound like? Are they
talkative or quiet? What kind of slang do they use? What is their
sense of humor like?

⋆\star 

What do they look like? Do they have any
defining gestures? What’s the first thing people notice about
them?

⋆\star 

What are their motivations and internal characteristics?
What are their flaws? What are their values? What are they afraid of?
How will they change and grow over the course of this story?

<<scratchpad>>

[Setting] Agent Prompt

Given
<<identifiers found in the scratchpad>>,
describe the setting in detail (more than 5 sentences). The
description should answer the following questions:

⋆\star 

Where does the
story take place? Is it set in a fictional world, or is it simply set
in someone’s backyard?

⋆\star 

When does the story take place? What decade
is it set in? How much time elapses over the course of the story?

<<scratchpad>>

[Plot] Agent Prompt

Given
<<identifiers found in the scratchpad>>,
describe the key plot points in detailed bullet points.
<<scratchpad>>

The <<identifiers found in the scratchpad>> are extracted from the scratchpad and formatted to fit the prompt. For instance, for a scratchpad that contains the original prompt, the [conflict] and [character] agents’ contributions, the resulting <<identifiers found in the scratchpad>> would be: “a Creative Writing Task, the Central Conflict, and the Character Descriptions”.

B.3 Writing Agents

[<<Section>>] Agent Prompt

Given
<<identifiers found in the scratchpad>>,
continue the story by writing the <<section>> part.
<<If previous sections have been written, include the following in the prompt:>>
Begin your portion of the story in a way that naturally flows from the previous ending. Match the writing style, vocabulary, and overall mood of the existing text. Do not re-explain details or events that have already been described.
<<If this is not the meant to be the last section, include the following in the prompt:>>
Focus only on the <<section>> part of the story. Do not write about the following parts of the story. Do not end the story.
<<scratchpad>>

In these writing agents’ prompt templates:

• 

<<section>> is one of “Exposition”, “Rising Action”, “Climax”, “Falling Action”, or “Resolution”,

• 

<<identifiers found in the scratchpad>> are extracted from the scratchpad and formatted to fit the prompt. For these writing agents they are formatted as follows:
“a Creative Writing Task, the Content Plan (Central Conflict, Character Descriptions, Setting, Key Plot Points), and the Previous Parts of the Story (Exposition, Rising Action, Climax)”, where the enumerated elements correspond to what is in the scratchpad.

In the specific case of the Agents’ Room [planning] variant, with only the planning agents, we still need a single writing agent to finalize the story, which we denote as the [finalizer]. This [finalizer] agent uses the following prompt template:

[Finalizer] Agent Prompt

Given
<<identifiers found in the scratchpad>>,
write a story using the information below.
<<scratchpad>>

Appendix C Prompt Templates for Synthetic Data Generation

For the planning agents, we use the same prompt templates as in Section B.2 to generate the synthetic training data, except in this case, we provide the gold standard data in the scratchpad. As a consequence, the scratchpad is formatted as follows:

[Scratchpad] Format

[Creative Writing Task]
<<the original writing prompt>>
[User-Written Response]
<<the gold output>>

The <<identifiers found in the scratchpad>> are formatted as “a Creative Writing Task and a User-Written Response”.

For the writing agents, we use the following prompt template to split to gold standard stories into distinct sections:

[Writing] Synthetic Data Generation

Split the following story into sections:

⋆\star 

[Exposition]: The exposition gives the reader the background info they need to jump right into the story’s world. This is often found towards the beginning of the story.

⋆\star 

[Rising Action]: The rising action is the moments in the story that lead up to the climax — choices the main characters have made and the events happening that are at odds with the characters’ goals. This is where the story builds and the reader begins to invest in the characters.

⋆\star 

[Climax]: The climax is the primary turning point and what the story has been building towards.

⋆\star 

[Falling Action]: The falling action is the period of time in a story that follows the climax and leads to the resolution. It can be used to clarify the events of the climax, ease any built-up tension, or wrap up loose ends.

⋆\star 

[Resolution]: This is the end of the story. It answers the remaining unanswered questions in the plot. The resolution is also the time to show the next step in the characters’ lives.

For each section, give the section header (marked as [Exposition], [Rising Action], [Climax], [Falling Action], and [Resolution]) followed by the first sentence of that section, copied exactly from the story.
[User-Written Response]
<<the gold output>>

Appendix D Human Evaluation Instructions

For this task, you will be presented with a writing prompt and two short stories corresponding to this prompt. Your task is to compare the quality of the two stories across several dimensions. This is a judgment task rather than an annotation task. As such, you should use your own judgment when you assign ratings, calibrated by the rubrics we provide.

This rating task consists of three steps: (1) Compare the quality of the two stories across four dimensions. (2) Rate which story you preferred. (3) (optional) Leave comment / feedback on the stories.
In the following we provide detailed instructions for each step:

D.1 Rate the Quality of the Story

Your task is to compare the quality of two stories along four different dimensions (plot, creativity, development, language use), as described in the Rubric table below.

While the dimensions may have overlap and work in interdependent ways, they are intended to capture distinct aspects of what makes a good story. Therefore, a story may score highly in one dimension and poorly in another. Furthermore, the features (marked as a, b, c) that make up a dimension may be thought of as cumulative. For example, a story may have strong characters but suffer from an underdeveloped setting.

The Rubric table is intended to help you calibrate your judgment so that you can roughly determine when a story is very good or even excellent along a particular dimension because it exhibits all of the features of that dimension. Conversely, if a story fails to exhibit most or all of the features of a dimension, then you may score the story as being poor or very poor along that dimension. The features are meant to be illustrative but not exhaustive; you may determine that a story should score poorly or well due to the absence or presence of additional features for a given dimension based on your judgment.

Another important thing to note about the features that make up the dimensions we’re asking you to rate is that they describe conventions that may be followed or flouted; a story may contain intentional plot devices like non-linear timelines, discontinuity, and other stylistic choices to create effects. As with other features, these elements of a story should inform your judgment on their own merit (so that they only negatively impact your rating if they are ineffective or confusing and positively impact your rating if they are used well to make the story more interesting and unique).

We use a 3-point comparative rating scale for each of the dimensions. The rating scale can be thought of as described below:

Rating

A is better
Response A is better than Response B in that dimension.

About the same
Both responses are about the same in that dimension.

B is better
Response B is better than Response A in that dimension.

The focus of this rubric is the quality of the writing, and not how well the stories follow the writing prompt. In particular, when rating with this rubric, we encourage you not to focus on the number of words mentioned in the writing prompts, but rather on the features described in the table below.

Dimension

Features

Plot

a.

The story has a recognizable structure, e.g. with a connected beginning, middle, and end.

b.

The story exhibits events and turns that move the plot forward.

c.

The story does not have logical or conceptual inconsistencies. Surprising or disruptive elements are intentional, e.g., they serve the story and do not feel jarring, odd, or out of place.

Creativity of Ideas, Themes, and Topics

a.

Engaging characters, themes, and imagery. The ideas do not feel generic or bland.

b.

Avoidance of overly cliched characters and storylines, unintentional tropes, and stereotypes. When used, tropes and cliches serve a purpose (e.g. comedic effect, twist on a common trope etc).

c.

The story includes original elements that were not explicitly mentioned in the prompt.

Development

a.

Characters and settings are introduced and contextualized with relevant details that allow the reader to understand their place in the story.

b.

Appropriate levels of detail and complexity are provided to lend the story a feeling of realness and believability.

Reminder: The features that make up a dimension may be thought of as cumulative. A story with a well-developed character, but in a lackluster setting (or vice-versa) would score lower in Development than a story that does well on both aspects.

Language Use

a.

The language used feels varied and rich: Variance of sentence structure, verbiage, and vocabulary.

b.

The story exhibits rhetorical, linguistic and literary devices (e.g. ambiguity, alliteration, etc) to create interesting effects

c.

The story avoids bland or repetitive phrases (unless used intentionally to create a narrative, thematic, or linguistic effect).

We provided examples rated along these rubrics. While the examples include explanations, these are there as an aid, and you are not requested to provide explanations for your ratings.

D.2 Which story do you prefer?

Do you find the story interesting, engaging, funny, or emotionally-rich? In addition to getting your judgments of the dimensions, we would also like to know whether you enjoyed reading the story. Similar to the dimensions, we will ask you to score which story you prefer:

• 

A is better

• 

About the same

• 

B is better

When rating, do not hesitate to be very critical.

D.3 Optional: Leave comments or feedback on the stories

Thank you for completing the ratings! If you have any additional comments or feedback you would like to provide on the story, feel free to add them in the “comments” section.

Appendix E Prompt Template for the LLM Evaluator

The following prompt template is used by the LLM to evaluate two system outputs side-by-side (we replace <<story a>> and <<story b>> with the two stories being evaluated):

[LLM Evaluator] Prompt Template

You will conduct a side-by-side evaluation. You will be given two
system-generated stories. Your task is to compare the two stories and
determine which one is better based on the following dimensions:

• 

Plot: The story should have a recognizable structure, e.g., with a
connected beginning, middle, and end. The story should exhibit events and
turns that move the plot forward. The story should not have logical or
conceptual inconsistencies. Surprising or disruptive elements should be
intentional, e.g., they serve the story and do not feel jarring, odd, or
out of place.

• 

Creativity: There should be engaging characters, themes, and imagery. The
ideas should not feel generic or bland. There should be avoidance of
overly cliched characters and storylines, unintentional tropes, and
stereotypes. When used, tropes and cliches should serve a purpose (e.g.,
comedic effect, twist on a common trope etc). The story should include
original elements that were not explicitly mentioned in the prompt.

• 

Development: Characters and settings should be introduced and
contextualized with relevant details that allow the reader to understand
their place in the story. Appropriate levels of detail and complexity
should be provided to lend the story a feeling of realness and
believability.

• 

Language Use: The language used should feel varied and rich: Variance of
sentence structure, verbiage, and vocabulary. The story should exhibit
rhetorical, linguistic and literary devices (e.g., ambiguity,
alliteration, etc) to create interesting effects. The story should avoid
bland or repetitive phrases (unless used intentionally to create a
narrative, thematic, or linguistic effect).

Provide a detailed assessment of the two stories in terms of these four
dimensions. Conclude your assessment with scores for each dimension using
the template below. Do not add any emphasis, such as bold and italics, on
your assessment.

[[Assessment Ending Template]]

Based on my assessment, the better story for each dimension is:

Plot:
[A or B or Same]

Creativity:
[A or B or Same]

Development:
[A or B or Same]

Language Use:
[A or B or Same]

Overall:
[A or B or Same]

[[Story A]]
<<story a>>
[[Story B]]
<<story b>>
[[Assessment]]

Below we show example output from the LLM evaluator from which we extract preference scores. In this case, the evaluator preferred story A on all dimensions.

[LLM Evaluator] Example Output

Story A has a more defined plot structure with a clear beginning, rising action, climax, and resolution. The summoning of Horus, his reaction to the modern world, and his eventual acceptance create a compelling narrative arc. Story B, while touching upon interesting themes, lacks a clear climax and resolution. The story feels incomplete, leaving the reader with unanswered questions about Horus’s fate and Ash’s journey.

Story A exhibits more creativity in its portrayal of Horus and his interactions with Amelia. The falcon god’s bewilderment, anger, and eventual acceptance are depicted with nuance and depth. The story also introduces original elements, such as the restoration of the canopic jar, which adds a layer of symbolism and reinforces the theme of reconciliation. Story B relies on more generic depictions of a god’s reaction to the modern world, lacking the originality and depth seen in Story A.

Both stories provide adequate development of their main characters, Amelia and Ash, respectively. However, Story A excels in its development of Horus, providing a more nuanced and believable portrayal of a god grappling with the realities of a changed world. The story delves into his emotions, his struggles, and his eventual acceptance, making him a more compelling and relatable character. Story B’s portrayal of Horus, while touching upon his disillusionment, lacks the same level of depth and complexity.

Story A utilizes a richer and more varied language, employing vivid imagery, sensory details, and a wider range of vocabulary. The story effectively uses rhetorical devices, such as repetition and contrast, to emphasize the differences between the ancient and modern worlds. Story B, while adequately written, lacks the same level of linguistic richness and sophistication.
Based on my assessment, the better story for each dimension is:

Plot:
A

Creativity:
A

Development:
A

Language Use:
A

Overall:
A

Appendix F Additional Results

While we consider human-based evaluation our primary means of
evaluation, the LLM evaluator helps us assess overall system-level
trends. We report pairwise win rate (proportion of examples on which
our Agents’ Room plan + write variant performed better than
comparison systems according to our LLM-based
evaluator. Table 3 complements Figure 3a.

ARZS plan + write vs
overall
plot
creativ.
develop.
language

E2EZS plan
74.55
63.64
75.47
75.93
81.13

E2EZS reflect
67.27
63.64
67.92
68.52
69.23

E2EZS decompose
89.09
80.00
87.04
90.91
90.91

2Stage decompose
66.67
59.26
64.15
66.67
67.92

Table 3: Proportion of times
LLM-based evaluator preferred ARZS to comparison system
across overall, and across the dimensions of plot, creatitivy,
development, and language use.

The majority of our experiments were conducted using a Gemini 1.5
Flash backbone model. This choice was dictated by the nature of the
creative writing task which is challenging to accomplish with models
that do not have a long enough context window and adequate writing
quality. Most recent work on storytelling using a single model resorts
to large, proprietary models such as GPT
(Yang et al. 2023; Yang et al. 2022), or Claude
(Chakrabarty et al. 2024a). This is also the case for multi-agent
systems targeting writing which seem to be exclusively relying on
GPT-4
(Chen et al. 2024; Bai et al. 2024). Nevertheless,
using Gemma2-9B-it (Riviere et al. 2024) as a backbone model we
compare Agents’ Room and E2E systems in the zero-shot setting,
using the LLM-based evaluator.

Agents’ RoomZS plan+write vs.
overall
plot
creativ.
develop.
language

E2EZS
80.00
67.27
84.62
83.33
77.78

Table 4: Proportion of times LLM-based evaluator
preferred Agents’ RoomZS to E2EZS overall, and across the
dimensions of plot, creativity, development, and language use.

As can be seen in Table 4, even with the smaller scale
Gemma2-9B-it model, Agents’ Room greatly
outperforms the end-to-end baseline across all dimensions of
evaluation.

Finally, although we did not elicit feedback on individual story dimensions, we did ask participants to comment on the quality of the stories produced by our systems, and possibly on aspects of story quality our instructions did not cover (see Section D). We show some of this feedback below.

Participant Feedback

”The task was interesting, but over time, I found the language redundant. There seemed to be a go-to vocabulary list utilized in the majority of the stories, phrases used time and again, making the output somewhat predictable.”

”It was interesting to see what kind of fictional narrative the model would generate. Most of the stories seemed to be written at a seventh grade level. The stories didn’t stray too far from the input and for the most part were grammatically correct. There were at times, instances of repetitiveness, including entire paragraphs, that made me wonder what the model was doing.”

”The stories showed some promise, but often fell into the same pitfalls of loops or sudden tone discordance…”

◄
 
 Feeling
lucky?
 
 Conversion
report
 Report
an issue
 View original
on arXiv►

Copyright
Privacy Policy

Generated by LaTeXML oxide
~~~~
