import sys
import re

# Needed to import from folder directory. Replace with your own project.
# Probably a better way to do this that doesn't involve revealing my own file structure but whatever, you're not my mum.
sys.path.append(r'C:\dev\advent-of-code-2024')

# from utils.maths import quicksort
from utils.read_input import read_input, read_input_raw

# raw_text = read_input_raw('./3/example.txt')
# text = read_input('./3/example.txt')
# raw_text = read_input_raw('./3/example2.txt')
# text = read_input('./3/example2.txt')
raw_text = read_input_raw('./3/input.txt')
text = read_input('./3/input.txt')

# Part 1
pt1_value = 0

exp = 'mul\(\d{1,3},\d{1,3}\)'
for line in text:
    matches = re.findall(exp, line)
    for m in matches:
        nums = re.findall('\d{1,3}', m)
        pt1_value += int(nums[0]) * int(nums[1])

# Part 2
print('================================ PT2')
pt2_value = 0

exp2 = "don't\(\)|do\(\)|mul\(\d{0,3},\d{0,3}\)"
all_matches = []
for line in text:
    matches = re.findall(exp2, line)
    all_matches += matches

active = True
for m in all_matches:
    if re.match("don't()", m):
        active = False
        continue
    elif re.match('do()', m):
        active = True
        continue
    else:
        if active:
            nums = re.findall('\d{1,3}', m)
            pt2_value += int(nums[0]) * int(nums[1])

print('Part 1 Total: ', pt1_value)
print('Part 2 Total: ', pt2_value)
