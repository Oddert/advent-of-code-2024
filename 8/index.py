import sys
import re

from typing import Tuple, List

# Needed to import from folder directory. Replace with your own project.
# Probably a better way to do this that doesn't involve revealing my own file structure but whatever, you're not my mum.
sys.path.append(r'C:\dev\advent-of-code-2024')

# from utils.maths import quicksort
from utils.read_input import read_input, read_input_raw

# raw_text = read_input_raw('./8/example2.txt')
# text = read_input('./8/example2.txt')
# raw_text = read_input_raw('./8/example.txt')
# text = read_input('./8/example.txt')
raw_text = read_input_raw('./8/input.txt')
text = read_input('./8/input.txt')

# Part 1
pt1_value = 0

def oob(board: List[List[int]], coords: Tuple[int, int]):
    width = len(board[0]) - 1
    height = len(board) - 1
    if coords[0] > height or coords[0] < 0 or coords[1] > width or coords[1] < 0:
        return True
    return False

def pt1 ():
    points = {}
    pairs = {}
    anti_nodes = {}

    board = []

    for line_i, line in enumerate(text):
        chars = re.findall('.', line)
        board.append(chars)
        for char_i, char in enumerate(chars):
            if char != '.':
                if char not in points:
                    points[char] = []
                points[char].append((line_i, char_i))

    for key, coords in points.items():
        pairs[key] = []
        for coord_i, coord in enumerate(coords):
            for remaining_coord in coords[coord_i + 1 :]:
                pairs[key].append((coord, remaining_coord))

    for key, list_pairs in pairs.items():
        for pair in list_pairs:
            row_diff = pair[0][0] - pair[1][0]
            col_diff = pair[0][1] - pair[1][1]
            left = (pair[0][0] + row_diff, pair[0][1] + col_diff)
            right = (pair[1][0] - row_diff, pair[1][1] - col_diff)

            for anti_node in [left, right]:
                if not oob(board, anti_node):
                    anti_nodes[anti_node] = True
                    if board[anti_node[0]][anti_node[1]] == '.':
                        board[anti_node[0]][anti_node[1]] = '#'

    print(points)
    print(pairs)

    for row in board:
        print(''.join(row))

    print(anti_nodes)
    return len(anti_nodes)
pt1_value = pt1()

# Part 2
print('================================ PT2')
pt2_value = 0


def pt2 ():
    points = {}
    pairs = {}
    anti_nodes = {}

    board = []

    for line_i, line in enumerate(text):
        chars = re.findall('.', line)
        board.append(chars)
        for char_i, char in enumerate(chars):
            if char != '.':
                if char not in points:
                    points[char] = []
                points[char].append((line_i, char_i))

    for key, coords in points.items():
        pairs[key] = []
        for coord_i, coord in enumerate(coords):
            for remaining_coord in coords[coord_i + 1 :]:
                pairs[key].append((coord, remaining_coord))

    for key, list_pairs in pairs.items():
        for pair in list_pairs:
            row_diff = pair[0][0] - pair[1][0]
            col_diff = pair[0][1] - pair[1][1]
            left = (pair[0][0] + row_diff, pair[0][1] + col_diff)
            right = (pair[1][0] - row_diff, pair[1][1] - col_diff)

            anti_nodes[pair[0]] = True
            anti_nodes[pair[1]] = True

            while not oob(board, left):
                anti_nodes[left] = True
                if board[left[0]][left[1]] == '.':
                    board[left[0]][left[1]] = '#'
                left = (left[0] + row_diff, left[1] + col_diff)

            while not oob(board, right):
                anti_nodes[right] = True
                if board[right[0]][right[1]] == '.':
                    board[right[0]][right[1]] = '#'
                right = (right[0] - row_diff, right[1] - col_diff)

    print(points)
    print(pairs)

    for row in board:
        print(''.join(row))

    print(anti_nodes)
    return len(anti_nodes)
pt2_value = pt2()

print('Part 1 Total: ', pt1_value)
print('Part 2 Total: ', pt2_value)
