import sys

# Needed to import from folder directory. Replace with your own project.
# Probably a better way to do this that doesn't involve revealing my own file structure but whatever, you're not my mum. 
sys.path.append(r'C:\dev\advent-of-code-2024')

from utils.maths import quicksort
from utils.read_input import read_input, read_input_raw

raw_text = read_input_raw('./1/example.txt')
text = read_input('./1/example.txt')
# raw_text = read_input_raw('./1/input.txt')
# text = read_input('./1/input.txt')

# Part 1
pt1_value = 0
instructions = []

for line in text:
    split_line = line.split(' ')
    instructions.append((split_line[0], split_line[1], split_line[2][1:-1]))

for instruction in instructions:
    pass

print(quicksort([5, 2, 8, 4, 9, 1]))

# Part 2
print('================================ PT2')
pt2_value = 0

print('Part 1 Total: ', pt1_value)
print('Part 2 Total: ', pt2_value)
