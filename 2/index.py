import sys

from typing import List

# Needed to import from folder directory. Replace with your own project.
# Probably a better way to do this that doesn't involve revealing my own file structure but whatever, you're not my mum.
sys.path.append(r'C:\dev\advent-of-code-2024')

# from utils.maths import quicksort
from utils.read_input import read_input, read_input_raw

# raw_text = read_input_raw('./2/example.txt')
# text = read_input('./2/example.txt')
raw_text = read_input_raw('./2/input.txt')
text = read_input('./2/input.txt')

# Part 1
pt1_value = 0


def find_direction(items: List[str]):
    desc = 0
    asc = 0
    for idx in range(len(items) - 2):
        value = int(items[idx])
        next_val = int(items[idx + 1])
        if value < next_val:
            asc += 1
        if value > next_val:
            desc += 1
    if asc > desc:
        return 'asc'
    if desc > asc:
        return 'desc'
    return 'neutral'


def single_report(nums: List[str]):
    prev_value = int(nums[0])
    original_increasing = find_direction(nums)
    i = 0
    for num in nums[1:]:
        val = int(num)
        increasing = (
            'desc' if prev_value > val else 'asc' if prev_value < val else 'neutral'
        )
        if (
            increasing != original_increasing
            or increasing == 'neutral'
            or abs(prev_value - val) > 3
            or abs(prev_value - val) < 1
        ):
            return i
        prev_value = val
        i += 1
    return None


for line in text:
    fail = single_report(line.split(' '))
    if fail is None:
        pt1_value += 1

# Part 2
print('================================ PT2')
pt2_value = 0

idx = 0
test_ids = [154, 258, 259, 260]
for line in text:
    line_split = line.split(' ')
    fail = single_report(line_split)
    if fail is not None:
        left_list = [*line_split[0:fail], *line_split[fail + 1 :]]
        right_list = [*line_split[0 : fail + 1], *line_split[fail + 2 :]]
        left = single_report(left_list)
        right = single_report(right_list)
        if left is None or right is None:
            pt2_value += 1
    else:
        pt2_value += 1
    idx += 1

print('Part 1 Total: ', pt1_value)
print('Part 2 Total: ', pt2_value)
