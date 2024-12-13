import sys
import re

import math as maths

from typing import List

# Needed to import from folder directory. Replace with your own project.
# Probably a better way to do this that doesn't involve revealing my own file structure but whatever, you're not my mum.
sys.path.append(r'C:\dev\advent-of-code-2024')

# from utils.maths import quicksort
from utils.read_input import read_input, read_input_raw

# raw_text = read_input_raw('./7/example.txt')
# text = read_input('./7/example.txt')
raw_text = read_input_raw('./7/input.txt')
text = read_input('./7/input.txt')

# Part 1
pt1_value = 0

for line in text:
    nums = [int(item) for item in re.findall('[0-9]+', line)]
    print('-----------', nums)
    target = nums[0]
    possible_pt1 = False

    def recurse_pt1(accumulator: int, items: List[int], trace=''):
        """placeholder"""
        # print(accumulator, items, f'depth: {depth}')
        if len(items):
            recurse_pt1(accumulator + items[0], items[1:], f'{trace} + {items[0]}')
            recurse_pt1(accumulator * items[0], items[1:], f'{trace} * {items[0]}')
        elif accumulator == target:
            print('debug is possible_pt1', target)
            global possible_pt1
            possible_pt1 = True

    recurse_pt1(0, nums[1:], str(0))
    print(target, possible_pt1)
    pt1_value += 0 if not possible_pt1 else target

# Part 2
print('================================ PT2')
pt2_value = 0

for line in text:
    nums = [int(item) for item in re.findall('[0-9]+', line)]
    print('-----------', nums)
    target = nums[0]
    possible_pt2 = False

    def recurse_pt2(accumulator: int, items: List[int], trace=''):
        """placeholder"""
        # print(accumulator, items, f'depth: {depth}')
        if len(items):
            recurse_pt2(accumulator + items[0], items[1:], f'{trace} + {items[0]}')
            recurse_pt2(accumulator * items[0], items[1:], f'{trace} * {items[0]}')
            recurse_pt2(
                int(str(accumulator) + str(items[0])),
                items[1:],
                f'{trace} * {items[0]}',
            )
        elif accumulator == target:
            print('debug is possible_pt2', target)
            global possible_pt2
            possible_pt2 = True

    recurse_pt2(0, nums[1:], str(0))
    print(target, possible_pt2)
    pt2_value += 0 if not possible_pt2 else target

print('Part 1 Total: ', pt1_value)
print('Part 2 Total: ', pt2_value)
