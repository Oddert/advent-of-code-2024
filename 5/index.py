import sys

import math as maths

from typing import List

# Needed to import from folder directory. Replace with your own project.
# Probably a better way to do this that doesn't involve revealing my own file structure but whatever, you're not my mum.
sys.path.append(r'C:\dev\advent-of-code-2024')

# from utils.maths import quicksort
from utils.read_input import read_input, read_input_raw

# raw_text = read_input_raw('./5/example.txt')
# text = read_input('./5/example.txt')
raw_text = read_input_raw('./5/input.txt')
text = read_input('./5/input.txt')
# raw_text = read_input_raw('./5/text.txt')
# text = read_input('./5/text.txt')

# Part 1
pt1_value = 0

rules = {}
pages = []
loading_rules = True

for line in text:
    if line == '':
        loading_rules = False
    elif loading_rules:
        split = line.split('|')
        if split[0] not in rules:
            rules[split[0]] = []
        rules[split[0]].append(split[1])
    else:
        pages.append(line)

def pt1():
    value = 0
    middle_nums = []

    for page in pages:
        nums = page.split(',')
        seen = {}
        valid = True
        for idx, num in enumerate(nums):
            if num in rules:
                for val in seen:
                    if val in rules[num]:
                        valid = False
            seen[num] = idx
        if valid:
            middle_nums.append(nums[maths.floor(len(nums) / 2)])

    for num in middle_nums:
        value += int(num)
    return value

pt1_value = pt1()

# Part 2
print('================================ PT2')
pt2_value = 0

def pt2():
    value = 0
    middle_nums = []

    def process_page(nums: List[str], depth: int = 0):
        seen = {}
        valid = True
        fail_source_int = 0
        fail_target_int = 0
        print('======')
        print(nums)

        for idx, num in enumerate(nums):
            if num in rules:
                for seen_val in seen:
                    if seen_val in rules[num]:
                        valid = False
                        fail_source_int = num
                        fail_target_int = seen_val
            seen[num] = idx
    
        if valid:
            print('valid: ', nums)
            if depth >= 1:
                middle_nums.append(nums[maths.floor(len(nums) / 2)])
        else:
            print(f'value: {fail_source_int} must be before: {fail_target_int}')
            if depth < 9999:
                target_idx = seen[fail_target_int]
                source_idx = seen[fail_source_int]
                if target_idx >= 0:
                    nums[target_idx], nums[source_idx] = nums[source_idx], nums[target_idx]
                    process_page(nums, depth + 1)
                else:
                    print('unrecoverable')
            
    
    for page in pages:
        process_page(nums = page.split(','))

    print(middle_nums)
    for num in middle_nums:
        value += int(num)
    return value

pt2_value = pt2()

print('Part 1 Total: ', pt1_value)
print('Part 2 Total: ', pt2_value)
