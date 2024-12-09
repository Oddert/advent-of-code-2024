import sys

from typing import List

# Needed to import from folder directory. Replace with your own project.
# Probably a better way to do this that doesn't involve revealing my own file structure but whatever, you're not my mum.
sys.path.append(r'C:\dev\advent-of-code-2024')

from utils.maths import quicksort
from utils.read_input import read_input, read_input_raw

# raw_text = read_input_raw('./1/example.txt')
# text = read_input('./1/example.txt')
raw_text = read_input_raw('./1/input.txt')
text = read_input('./1/input.txt')

# Part 1
pt1_value = 0
left_list = []
right_list = []

for line in text:
    split_line = line.split('   ')
    left_list.append(int(split_line[0]))
    right_list.append(int(split_line[1]))

left_list = quicksort(left_list)
right_list = quicksort(right_list)

for i in range(len(left_list)):
    diff = abs(left_list[i] - right_list[i])
    pt1_value += diff

# Part 2
print('================================ PT2')
pt2_value = 0

def accumulate_frequencies(items: List[int]):
	acc = {}
	for item in items:
		if item not in acc:
			acc[item] = 0
		acc[item] += 1
	return acc

freq_right = accumulate_frequencies(right_list)

for item in left_list:
	if item in freq_right:
		freq = freq_right[item]
		similarity = freq * item
		pt2_value += similarity

print('Part 1 Total: ', pt1_value)
print('Part 2 Total: ', pt2_value)
