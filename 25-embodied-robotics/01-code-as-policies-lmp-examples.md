# Code as Policies LMP Examples (Language Model Programs for embodied control)

Title: Code as Policies LMP Examples (Language Model Programs for embodied control)
Source-URL: https://raw.githubusercontent.com/google-research/google-research/master/code_as_policies/LMP%20Examples.ipynb
Source-Repo-or-Site: google-research/google-research (github.com/google-research/google-research)
Original-Path: code_as_policies/LMP Examples.ipynb
Category: 25-embodied-robotics (language goals into robot plans/code with perception feedback)
Tags: code-as-policies,lmp,hierarchical-code-gen,robot-policy-code,perception-apis
Retrieved: 2026-11-08
Value-Note: Hierarchical LMPs: language comments become executable policy code recomposing perception/control APIs; undefined functions recursively self-defined, so goals compile into a body.
Truncation-Note: All notebook cell sources reproduced verbatim in order; cell separator lines added by collector; cell outputs and notebook JSON metadata omitted. Full notebook at Source-URL.

--- ORIGINAL ---

````python
# %% [markdown] cell 0  (separator added by collector)
Copyright 2022 Google LLC. SPDX-License-Identifier: Apache-2.0

Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the License. You may obtain a copy of the License at

https://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.

# %% [markdown] cell 1  (separator added by collector)
# Language Model Program Examples

This notebook is a part of the open-source code release associated with the paper:

[Code as Policies: Language Model Programs for Embodied Control](https://code-as-policies.github.io/)

This notebook accompanies examples given in the Method section of the paper.

1) Please obtain an OpenAI API Key here:
https://openai.com/blog/openai-api/

2) Gain Codex access by joining the waitlist here:
https://openai.com/blog/openai-codex/

Once you have Codex access you can use `code-davinci-002` as the `model_name`. Using the GPT-3 model (`text-dainvci-002`) is also ok, but performance won't be as good (there will be more code logic errors).

# %% [code] cell 2  (separator added by collector)
openai_api_key = 'YOUR KEY HERE'
model_name = 'code-davinci-002' # 'text-davinci-002'

# %% [markdown] cell 3  (separator added by collector)
# Setup

# %% [code] cell 4  (separator added by collector)
! pip install openai

import openai
openai.api_key = openai_api_key

# %% [code] cell 5  (separator added by collector)
def lmp(base_prompt, query, stop_tokens=None, query_kwargs=None):
    new_prompt = f'{base_prompt}\n{query}'

    use_query_kwargs = {
        'engine': model_name,
        'max_tokens': 512,
        'temperature': 0,
    }
    if query_kwargs is not None:
      use_query_kwargs.update(query_kwargs)

    response = openai.Completion.create(
        prompt=new_prompt, stop=stop_tokens, **use_query_kwargs
    )['choices'][0]['text'].strip()

    print(query)
    print(response)

    return response

# %% [markdown] cell 6  (separator added by collector)
# Simple LMPs

# %% [markdown] cell 7  (separator added by collector)
## Pure Python

# %% [code] cell 8  (separator added by collector)
prompt_pure_python = '''
# Python script
# get the variable a.
ret_val = a
'''.strip()

# %% [code] cell 9  (separator added by collector)
_ = lmp(prompt_pure_python, '# find the sum of variables a and b.', ['#'])

# %% [code] cell 10  (separator added by collector)
_ = lmp(prompt_pure_python, '# find the sum of numbers in a list called values.', ['#'])

# %% [code] cell 11  (separator added by collector)
_ = lmp(prompt_pure_python, '# find the difference between the max and min numbers in a list called xs.', ['#'])

# %% [code] cell 12  (separator added by collector)
_ = lmp(prompt_pure_python, '# see if any number is divisible by 3 in a list called xs.', ['#'])

# %% [markdown] cell 13  (separator added by collector)
## Using Context

# %% [code] cell 14  (separator added by collector)
prompt_context = '''
objects = ['green block', 'green bowl', 'yellow block', 'yellow bowl']
# the yellow block.
ret_val = 'yellow block'
# the blocks.
ret_val = ['green block', 'yellow block']
'''.strip()

# %% [code] cell 15  (separator added by collector)
context = "objects = ['blue bowl', 'red block', 'red bowl', 'blue block']"
query = '# the bowls.'

print(context)
_ = lmp(f'{prompt_context}\n{context}', query, ['#', 'objects = ['])

# %% [code] cell 16  (separator added by collector)
context = "objects = ['blue bowl', 'red block', 'red bowl', 'blue block']"
query = '# sea-colored block.'

print(context)
_ = lmp(f'{prompt_context}\n{context}', query, ['#', 'objects = ['])

# %% [code] cell 17  (separator added by collector)
context = '''
objects = ['blue bowl', 'red block', 'red bowl', 'blue block']
# sea-colored block.
ret_val = 'blue block'
objects = ['blue bowl', 'red block', 'red bowl', 'blue block']
'''.strip()
query = '# the other block.'

print(context)
_ = lmp(f'{prompt_context}\n{context}', query, ['#', 'objects = ['])

# %% [markdown] cell 18  (separator added by collector)
## Using 3rd Party Libraries

# %% [code] cell 19  (separator added by collector)
prompt_3lib = '''
import numpy as np
# move all points in pts_np toward the right.
ret_val = pts_np + [0.3, 0]
# move a pt_np toward the top.
ret_val = pt_np + [0, 0.3]
'''.strip()

# %% [code] cell 20  (separator added by collector)
query = '# get the left most point in pts_np.'

_ = lmp(prompt_3lib, query, ['#'])

# %% [code] cell 21  (separator added by collector)
query = '# get the center of pts_np.'

_ = lmp(prompt_3lib, query, ['#'])

# %% [code] cell 22  (separator added by collector)
query = '# the closest point in pts_np to pt_np.'

_ = lmp(prompt_3lib, query, ['#'])

# %% [markdown] cell 23  (separator added by collector)
## Using 1st Party Libraries

# %% [code] cell 24  (separator added by collector)
prompt_1lib = '''
from utils import get_pos, put_first_on_second
objects = ['gray block', 'gray bowl']
# put the gray block on the gray bowl.
put_first_on_second('gray block', 'gray bowl')
objects = ['purple block', 'purple bowl']
# move the purple bowl toward the left.
target_pos = get_pos('purple bowl') + [-0.3, 0]
put_first_on_second('purple bowl', target_pos)
'''.strip()

# %% [code] cell 25  (separator added by collector)
context = "objects = ['blue bowl', 'red block', 'red bowl', 'blue block']"
query = '# move the red block a bit to the right.'

print(context)
_ = lmp(f'{prompt_1lib}\n{context}', query, ['#', 'objects = ['])

# %% [code] cell 26  (separator added by collector)
context = "objects = ['blue bowl', 'red block', 'red bowl', 'blue block']"
query = '# put the blue block on the bowl with the same color.'

print(context)
_ = lmp(f'{prompt_1lib}\n{context}', query, ['#', 'objects = ['])

# %% [markdown] cell 27  (separator added by collector)
## Combined Examples

# %% [code] cell 28  (separator added by collector)
prompt_combined = '''
import numpy as np
from utils import get_pos, put_first_on_second
objects = ['cyan block', 'cyan bowl', 'pink bowl']
# put the cyan block in cyan bowl.
put_first_on_second('cyan block', 'cyan bowl')
objects = ['gray block', 'silver block', 'gray bowl']
# place the top most block on the gray bowl.
names = ['gray block', 'silver block']
positions = np.array([get_pos(name) for name in names])
name = names[np.argmax(positions[:,1])]
put_first_on_second(name, 'gray bowl')
objects = ['purple block', 'purple bowl']
# put the purple bowl to the left of the purple block.
target_pos = get_pos('purple block') + [-0.3, 0]
put_first_on_second('purple bowl', target_pos)
'''.strip()

# %% [code] cell 29  (separator added by collector)
context = "objects = ['red block', 'blue bowl', 'blue block', 'red bowl']"
query = '# move the left most bowl toward the right.'

print(context)
_ = lmp(f'{prompt_combined}\n{context}', query, ['#', 'objects = ['])

# %% [code] cell 30  (separator added by collector)
context = "objects = ['red block', 'blue bowl', 'blue block', 'red bowl']"
query = '# place the blocks in bowls with their colors.'

print(context)
_ = lmp(f'{prompt_combined}\n{context}', query, ['#', 'objects = ['])

# %% [code] cell 31  (separator added by collector)
context = "objects = ['red block', 'blue bowl', 'blue block', 'red bowl']"
query = '# move the red block to the middle of the bowls.'

print(context)
_ = lmp(f'{prompt_combined}\n{context}', query, ['#', 'objects = ['])

# %% [markdown] cell 32  (separator added by collector)
# Complex LMPs

# %% [markdown] cell 33  (separator added by collector)
## Control Flows

# %% [code] cell 34  (separator added by collector)
prompt_ctrl = '''
from utils import get_pos, put_first_on_second
# move the orange block toward the top.
target_pos = get_pos('orange block') + [0, 0.3]
put_first_on_second('orange block', target_pos)
# move the purple bowl toward the left.
target_pos = get_pos('purple bowl') + [-0.3, 0]
put_first_on_second('purple bowl', target_pos)
'''

# %% [code] cell 35  (separator added by collector)
context = "objects = ['red block', 'blue bowl', 'blue block', 'red bowl']"
query = '# while the red block is to the left of the blue bowl, move it to the right 5cm at a time.'

_ = lmp(f'{prompt_ctrl}\n{context}', query, ['#', 'objects = ['])

# %% [code] cell 36  (separator added by collector)
context = "objects = ['yellow block', 'green bowl', 'green block', 'yellow bowl']"
query = "# move the yellow block toward its bowl 1cm at a time until their distance is less than 5cm apart."

_ = lmp(f'{prompt_ctrl}\n{context}', query, ['#', 'objects = ['])

# %% [markdown] cell 37  (separator added by collector)
## Calling Other LMPs

# %% [code] cell 38  (separator added by collector)
prompt_modular_ui = '''
import numpy as np
from utils import get_pos, put_first_on_second, parse_obj
objects = ['yellow block', 'yellow bowl', 'gray block', 'gray bowl']
# move the sun colored block toward the left.
block_name = parse_obj('sun colored block')
target_pos = get_pos(block_name) + [-0.3, 0]
put_first_on_second(block_name, target_pos)
objects = ['white block', 'white bowl', 'yellow block', 'yellow bowl']
# place the block closest to the blue bowl on the other bowl.
block_name = parse_obj('the block closest to the blue bowl', f'objects = {objects}')
bowl_name = parse_obj('a bowl other than the blue bowl', f'objects = {objects}')
put_first_on_second(block_name, bowl_name)
'''.strip()

prompt_modular_parse_obj = '''
import numpy as np
from utils import get_pos
objects = ['brown bowl', 'green block', 'brown block', 'green bowl']
# the blocks.
ret_val = ['brown block', 'green block']
# the sky colored block.
ret_val = 'blue block'
objects = ['orange block', 'cyan block', 'purple bowl', 'gray bowl']
# the right most block.
block_names = ['orange block', 'cyan block']
block_positions = np.array([get_pos(block_name) for block_name in block_names])
right_block_name = block_names[np.argmax(block_positions[:, 0])]
ret_val = right_block_name
'''.strip()

# %% [code] cell 39  (separator added by collector)
context = "objects = ['red block', 'blue bowl', 'blue block', 'red bowl']"
query = '# while the left most block is the red block, move it toward the right.'

print(context)
_ = lmp(f'{prompt_modular_ui}\n{context}', query, ['#', 'objects = ['])

# %% [code] cell 40  (separator added by collector)
context = "objects = ['red block', 'blue bowl', 'blue block', 'red bowl']"
query = '# the left most block.'

print(context)
_ = lmp(f'{prompt_modular_parse_obj}\n{context}', query, ['#', 'objects = ['])

# %% [markdown] cell 41  (separator added by collector)
## Function-Generating LMPs

# %% [code] cell 42  (separator added by collector)
prompt_f_gen = '''
import numpy as np
from utils import get_pos, get_obj_bbox_xyxy
# define function: total = get_total(xs=numbers).
def get_total(xs):
    return np.sum(xs)
'''.strip()

# %% [code] cell 43  (separator added by collector)
query = '# define function: get_objs_bigger_than_area_th(obj_names, bbox_area_th).'

_ = lmp(f'{prompt_f_gen}', query, ['# define', '# example'])

# %% [markdown] cell 44  (separator added by collector)
## Hierarchical Function-Generating LMPs

# %% [code] cell 45  (separator added by collector)
query = '# define function: get_obj_bbox_area(obj_name).'

_ = lmp(prompt_f_gen, query, ['# define', '# example'])

# %% [code] cell 46  (separator added by collector)
prompt_hier_f_gen = '''
import numpy as np
from utils import get_obj_pos, get_obj_bbox_xyxy
# define function: total = get_total(xs=numbers).
def get_total(xs):
    return np.sum(xs)
# define function: pt_np = move_pt_left(pt_np, dist).
def move_pt_left(pt_np, dist):
    delta = np.array([-dist, 0])
    return translate_pt_np(pt_np, delta=delta)
'''.strip()

# %% [code] cell 47  (separator added by collector)
query = '# define function: get_obj_bbox_area(obj_name).'

_ = lmp(prompt_hier_f_gen, query, ['# define', '# example'])

# %% [code] cell 48  (separator added by collector)
query = '# define function: area = get_bbox_area(bbox_xyxy).'

_ = lmp(prompt_hier_f_gen, query, ['# define', '# example'])

# %% [markdown] cell 49  (separator added by collector)
## Combined Example

# %% [code] cell 50  (separator added by collector)
prompt_combined_parse_pos = '''
from utils import get_obj_pos

# right of the red block.
ret_val = get_obj_pos('red block') + np.array([0.3, 0])
# a bit below the cyan bowl.
ret_val = get_obj_pos('cyan bowl') + np.array([0, -0.1])
# a point between the cyan block and purple bowl.
pos = get_mid_point_np(pt0=get_obj_pos('cyan block'), pt1=get_obj_pos('purple bowl'))
ret_val = pos
# the corner closest to the yellow block.
corner_positions = get_corner_positions()
closest_corner_idx = get_closest_idx(points=corner_positions, point=get_obj_pos('yellow block'))
closest_corner_pos = corner_positions(closest_corner_idx)
ret_val = closest_corner_pos
'''.strip()

prompt_combined_parse_obj = '''
import numpy as np
from utils import get_obj_pos, get_objs_bigger_than_area_th

objects = ['brown bowl', 'green block', 'brown block', 'green bowl', 'blue bowl', 'blue block']
# the blocks.
ret_val = ['brown block', 'blue block']
# the sky colored block.
ret_val = 'blue block'
objects = ['blue block', 'cyan block', 'purple bowl', 'gray bowl', 'brown bowl', 'pink block']
# the right most block.
block_names = ['cyan block', 'pink block', 'blue block']
block_positions = np.array([get_obj_pos(block_name) for block_name in block_names])
right_block_name = block_names[np.argmax(block_positions[:, 0])]
ret_val = right_block_name
objects = ['blue block', 'cyan block', 'purple bowl', 'brown bowl', 'purple block']
# blocks above the brown bowl.
block_names = ['blue block', 'cyan block', 'purple block']
brown_bowl_pos = get_obj_pos('brown bowl')
use_block_names = [name for name in block_names if get_obj_pos(name)[1] > brown_bowl_pos[1]]
ret_val = use_block_names
'''.strip()

prompt_combined_ui = '''
import numpy as np
from utils import get_obj_pos, put_first_on_second, parse_obj

objects = ['green block', 'green bowl', 'yellow block', 'yellow bowl']
# move the bowls below the yellow block upwards.
bowl_names = parse_obj('the bowls below the yellow block', f'objects = {objects}')
for bowl_name in bowl_names:
  target_pos = get_obj_pos(bowl_name) + np.array([0, 0.1])
  put_first_on_second(bowl_name, target_pos)
objects = ['white block', 'white bowl', 'yellow block', 'yellow bowl']
# if the banana colored bowl is the top most bowl, then place it on the white bowl.
bowl_name = parse_obj('the banana colored bowl', f'objects = {objects}')
top_bowl_name = parse_obj('the top most bowl', f'objects = {objects}')
if bowl_name == top_bowl_name:
  put_first_on_second(bowl_name, 'white bowl')
objects = ['blue block', 'blue bowl', 'red block', 'red bowl']
# place the block closest to the blue bowl on the other bowl.
block_name = parse_obj('the block closest to the blue bowl', f'objects = {objects}')
bowl_name = parse_obj('a bowl other than the blue bowl', f'objects = {objects}')
put_first_on_second(block_name, 'red bowl')
'''.strip()

# %% [code] cell 51  (separator added by collector)
context = "objects = ['red block', 'blue bowl', 'blue block', 'red bowl']"
query = '# while there are blocks with area bigger than 0.2 that are left of the red bowl, move them toward the right.'

print(context)
_ = lmp(f'{prompt_combined_ui}\n{context}', query, ['#', 'objects = ['])

# %% [code] cell 52  (separator added by collector)
context = "objects = ['red block', 'blue bowl', 'blue block', 'red bowl']"
query = '# blocks with area bigger than 0.2 that are left of the red bowl.'

print(context)
_ = lmp(f'{prompt_combined_parse_obj}\n{context}', query, ['#', 'objects = ['])


````
