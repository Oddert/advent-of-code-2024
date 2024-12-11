import sys
import re

# Needed to import from folder directory. Replace with your own project.
# Probably a better way to do this that doesn't involve revealing my own file structure but whatever, you're not my mum.
sys.path.append(r'C:\dev\advent-of-code-2024')

# from utils.maths import quicksort
from utils.read_input import read_input, read_input_raw

# raw_text = read_input_raw('./4/example.txt')
# text = read_input('./4/example.txt')
raw_text = read_input_raw('./4/input.txt')
text = read_input('./4/input.txt')

# Part 1
pt1_value = 0

"""
List of transformations to search through, assuming X is the starting point 0,0.

Each instruction takes the format: [expected letter, x axis transfomation, y axis transfomation] 
"""
pt1_directions = [
    [['M', 0, 1], ['A', 0, 2], ['S', 0, 3]],  # Horizontal left-right
    [['M', 0, -1], ['A', 0, -2], ['S', 0, -3]],  # Horizontal right-left
    [['M', 1, 0], ['A', 2, 0], ['S', 3, 0]],  # Vertical down
    [['M', -1, 0], ['A', -2, 0], ['S', -3, 0]],  # Vertical up
    [['M', 1, 1], ['A', 2, 2], ['S', 3, 3]],  # Diagonal right-down
    [['M', 1, -1], ['A', 2, -2], ['S', 3, -3]],  # Diagonal left-down
    [['M', -1, 1], ['A', -2, 2], ['S', -3, 3]],  # Diagonal right-up
    [['M', -1, -1], ['A', -2, -2], ['S', -3, -3]],  # Diagonal left-up
]

board = []
validity_check = []
pt2_tracker = []

for line in text:
    debug_row = re.findall('.', line)
    board.append(debug_row)

    debug = []
    pt2_row = []

    for char in debug_row:
        debug.append('.')
        pt2_row.append(0)

    validity_check.append(debug)
    pt2_tracker.append(pt2_row)


def pt1(direction_set):
    """Functionalised part 1"""
    out = 0
    for row_i, p1_row in enumerate(board):
        for col_i, p1_col in enumerate(p1_row):
            if p1_col == 'X':
                for direction in direction_set:
                    valid = True
                    coords = [[row_i, col_i, 'X']]
                    for instruction in direction:
                        r = row_i + instruction[1]
                        c = col_i + instruction[2]
                        if r < len(board) and c < len(p1_row) and r >= 0 and c >= 0:
                            if board[r][c] != instruction[0]:
                                valid = False
                            else:
                                coords.append([r, c, board[r][c]])
                        else:
                            valid = False
                    if valid:
                        out += 1
                        for pair in coords:
                            validity_check[pair[0]][pair[1]] = pair[2]
    return out


# pt1_value = pt1(pt1_directions)

for d in validity_check:
    print(''.join(d))

# Part 2
print('================================ PT2')
pt2_value = 0

"""
List of transformations to search through, assuming X is the starting point 0,0.

Each instruction takes the format: [expected letter, x axis transfomation, y axis transfomation] 
"""
pt2_directions = [
    # [['M', 0, -1], ['S', 0, 1]],  # Horizontal left-right
    # [['M', 0, 1], ['S', 0, -1]],  # Horizontal right-left
    # [['M', 1, 0], ['S', -1, 0]],  # Vertical up
    # [['M', -1, 0], ['S', 1, 0]],  # Vertical down
    [['M', -1, -1], ['S', 1, 1]],  # Diagonal right-down
    [['M', -1, 1], ['S', 1, -1]],  # Diagonal left-down
    [['M', 1, -1], ['S', -1, 1]],  # Diagonal right-up
    [['M', 1, 1], ['S', -1, -1]],  # Diagonal left-up
]


def pt2(direction_set):
    """Functionalised part 1"""
    out = 0
    for row_i, p2_row in enumerate(board):
        for col_i, p2_col in enumerate(p2_row):
            if p2_col == 'A':
                for direction in direction_set:
                    valid = True
                    coords = [[row_i, col_i, 'A']]
                    for instruction in direction:
                        r = row_i + instruction[1]
                        c = col_i + instruction[2]
                        if r < len(board) and c < len(p2_row) and r >= 0 and c >= 0:
                            if board[r][c] != instruction[0]:
                                valid = False
                            else:
                                coords.append([r, c, board[r][c]])
                        else:
                            valid = False
                    if valid:
                        out += 1
                        pt2_tracker[row_i][col_i] += 1
                        for pair in coords:
                            validity_check[pair[0]][pair[1]] = pair[2]
    return out


pt2(pt2_directions)

for row in pt2_tracker:
    print(''.join([str(x) for x in row]))
    for col in row:
        if col >= 2:
            pt2_value += 1

print('Part 1 Total: ', pt1_value)
print('Part 2 Total: ', pt2_value)
