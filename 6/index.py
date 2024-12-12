import sys
import re

from typing import Tuple

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

board = []
board_pt2 = []
start_pos = (0, 0)

for row_i, line in enumerate(text):
    row = re.findall('.', line)
    board_pt2.append(row)
    board.append(line)
    for col_i, col in enumerate(line):
        if col == '^':
            start_pos = (row_i, col_i)

for r in board:
    print(r)
print(start_pos)


def encode(coords: Tuple[int, int]):
    return f'{coords[0]}-{coords[1]}'


def increment(pos: Tuple[int, int], facing_direction: int):
    match facing_direction:
        case 0:
            return (pos[0] - 1, pos[1])
        case 1:
            return (pos[0], pos[1] + 1)
        case 2:
            return (pos[0] + 1, pos[1])
        case 3:
            return (pos[0], pos[1] - 1)
        case _:
            print('ERROR: unknown direction', pos, facing_direction)
            return pos


def oob(coords: Tuple[int, int]):
    width = len(board[0]) - 1
    height = len(board) - 1
    if coords[0] > height or coords[0] < 0 or coords[1] > width or coords[1] < 0:
        return True
    return False


def pt1(start_position: Tuple[int, int]):
    curr_pos = start_position
    finished = False
    direction = 0
    visited_pt1 = {f'{start_position[0]}-{start_position[1]}': True}

    while not finished:
        next_coords = increment(curr_pos, direction)
        if oob(next_coords):
            finished = True
        else:
            if board_pt2[next_coords[0]][next_coords[1]] == '#':
                direction = (direction + 1) % 4
            else:
                visited_pt1[encode(next_coords)] = True
                curr_pos = next_coords
    return len(visited_pt1)


pt1_value = pt1(start_pos)

# Part 2
print('================================ PT2')
pt2_value = 0


def wall_or_box(coords):
    """
    For a given set of coordinates, returns a code representing the cell as a wall, box, or empty.

    key:
    0: Out of bounds (wall)
    1: No obstruction
    2: Objstruction
    """
    if oob(coords):
        return 0
    next_cell = board[coords[0]][coords[1]]
    if next_cell == '#':
        return 2
    return 1


def pt2(start_position: Tuple[int, int]):
    curr_pos = start_position
    finished = False
    direction = 0
    steps = [(*curr_pos, direction)]
    visited_pt2 = {f'{start_position[0]}-{start_position[1]}': [direction]}

    while not finished:
        next_coords = increment(curr_pos, direction)
        if oob(next_coords):
            finished = True
        else:
            if board_pt2[next_coords[0]][next_coords[1]] == '#':
                direction = (direction + 1) % 4
            else:
                encoded = encode(next_coords)
                if encoded in visited_pt2:
                    visited_pt2[encoded] = [*visited_pt2[encoded], direction]
                else:
                    visited_pt2[encoded] = [direction]
                curr_pos = next_coords
                # steps.append(next_coords)
                steps.append((*next_coords, direction))

    # possibles = []
    # for idx, step in enumerate(steps):
    #     rh_direction = (step[2] + 1) % 4
    #     right_hand_cell = increment(step, rh_direction)
    #     rh_cell_encoded = encode(right_hand_cell)

    #     next_cell = None
    #     if idx + 1 < len(steps):
    #         next_cell = steps[idx + 1]

    #     if rh_cell_encoded in visited_pt2:
    #         if rh_direction in visited_pt2[rh_cell_encoded] and next_cell != '#':
    #             print(f'rhs of: {step} is: {right_hand_cell}')
    #             print(f'    direction of cell to right is: {rh_direction}, visitied[]: {visited_pt2[rh_cell_encoded]}')
    #             if next_cell:
    #                 possibles.append(next_cell)

    possibles = []
    for step in steps:
        rh_direction = (step[2] + 1) % 4
        rh_cell_coords = increment(step, rh_direction)
        right_hand_cell_type = wall_or_box(rh_cell_coords)

        while right_hand_cell_type == 1:
            rh_cell_coords = increment(rh_cell_coords, rh_direction)
            right_hand_cell_type = wall_or_box(rh_cell_coords)

        if right_hand_cell_type == 2:
            obstacle = increment(step, step[2])
            if not oob(obstacle):
                possibles.append(obstacle)

    # print(possibles)
    # print(len(possibles))

    confirmed_loops = []

    for obstacle in possibles:
        # print(f'---------- trying obstacle {obstacle}')
        temp_board = []
        temp_curr_pos = start_position
        temp_direction = 0
        temp_steps = [(*temp_curr_pos, temp_direction)]
        visited_temp = {f'{start_position[0]}-{start_position[1]}': [temp_direction]}

        for line in text:
            # print(line)
            row = re.findall('.', line)
            temp_board.append(row)

        temp_board[obstacle[0]][obstacle[1]] = '#'
        # print('===')

        # for l in temp_board:
        # print(''.join(l))

        finished = False
        loop = False
        while not finished:
            next_coords = increment(temp_curr_pos, temp_direction)
            if oob(next_coords):
                # print(f'...finishing oob at {next_coords}')
                finished = True
            else:
                encoded = f'{encode(next_coords)}-{temp_direction}'
                if encoded in visited_temp:
                    # print('...finishing loop')
                    loop = True
                    finished = True
                if temp_board[next_coords[0]][next_coords[1]] == '#':
                    temp_direction = (temp_direction + 1) % 4
                else:
                    visited_temp[encoded] = True
                    temp_curr_pos = next_coords
                    temp_steps.append((*next_coords, temp_direction))
        if loop:
            confirmed_loops.append(obstacle)

    # print(confirmed_loops)
    return len(confirmed_loops)


pt2_value = pt2(start_pos)


print('Part 1 Total: ', pt1_value)
print('Part 2 Total: ', pt2_value)
