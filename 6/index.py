import sys
import re

# from typing import List

# Needed to import from folder directory. Replace with your own project.
# Probably a better way to do this that doesn't involve revealing my own file structure but whatever, you're not my mum.
sys.path.append(r'C:\dev\advent-of-code-2024')

# from utils.maths import quicksort
from utils.read_input import read_input, read_input_raw

raw_text = read_input_raw('./6/example.txt')
text = read_input('./6/example.txt')
# raw_text = read_input_raw('./6/input.txt')
# text = read_input('./6/input.txt')

# Part 1
pt1_value = 0

visited = {}
board = []
start_pos = (0, 0)

for row_i, line in enumerate(text):
    row = re.findall('.', line)
    board.append(row)
    for col_i, col in enumerate(row):
        if col == '^':
            start_pos = (row_i, col_i)

for r in board:
    print(r)
print(start_pos)

# Part 2
print('================================ PT2')
pt2_value = 0

print('Part 1 Total: ', pt1_value)
print('Part 2 Total: ', pt2_value)
