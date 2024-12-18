import sys
import re

from typing import Tuple, List

# Needed to import from folder directory. Replace with your own project.
# Probably a better way to do this that doesn't involve revealing my own file structure but whatever, you're not my mum.
sys.path.append(r'C:\dev\advent-of-code-2024')

# from utils.maths import quicksort
from utils.read_input import read_input, read_input_raw

# raw_text = read_input_raw('./9/example2.txt')
# text = read_input('./9/example2.txt')
raw_text = read_input_raw('./9/example.txt')
text = read_input('./9/example.txt')
# raw_text = read_input_raw('./9/input.txt')
# text = read_input('./9/input.txt')

# Part 1
pt1_value = 0


def pt1():
    """Wrapper for part 1 to lexically contain variables."""
    value = 0
    idx1 = 0

    sequence = []
    file_id = 0
    type_flag = 0

    while idx1 < len(text[0]):
        num = int(text[0][idx1])
        # print('----')
        # print('file_id, num: ', file_id, num)
        if type_flag == 0:
            # print('creating range for ', file_id, ' this many times: ', num)
            for i in range(num):
                sequence.append(str(file_id))
            type_flag = 1
            file_id += 1
        elif type_flag == 1:
            # print('creating spaces: ', num)
            for i in range(num):
                sequence.append('.')
            type_flag = 0
        idx1 += 1

    sequence_str = ''.join(sequence)
    print(sequence)

    pointer = len(sequence) - 1

    while pointer >= 0 and not re.search('^\d+\.+$', sequence_str):
        move_ptr = 0
        while sequence[move_ptr] != '.' and move_ptr <= len(sequence) - 1:
            move_ptr += 1
        sequence[pointer], sequence[move_ptr] = sequence[move_ptr], sequence[pointer]
        sequence_str = ''.join(sequence)
        # print(sequence_str)
        pointer -= 1

    print(sequence_str)
    for char_i, char in enumerate(sequence):
        if char == '.':
            break
        result = int(char) * char_i
        # print(char_i, ' * ', char, ' = ',result)
        value += result
    return value


pt1_value = pt1()

# Part 2
print('================================ PT2')
pt2_value = 0


def pt2():
    """Wrapper for part 2 to lexically contain variables."""
    value = 0
    idx1 = 0

    sequence = []
    file_id = 0
    type_flag = 0

    while idx1 < len(text[0]):
        num = int(text[0][idx1])
        if type_flag == 0:
            for i in range(num):
                sequence.append(str(file_id))
            type_flag = 1
            file_id += 1
        elif type_flag == 1:
            for i in range(num):
                sequence.append('.')
            type_flag = 0
        idx1 += 1

    sequence_str = ''.join(sequence)
    print(sequence)
    
    blocks = re.findall(r'0+|1+|2+|3+|4+|5+|6+|7+|8+|9+|\.+', sequence_str)
    print(blocks)

    block_len = len(blocks)

    print('TEST', [(x.start(0), x.end(0)) for x in re.finditer(r'0+|1+|2+|3+|4+|5+|6+|7+|8+|9+|\.+', sequence_str)])

    for idx in range(block_len):
        block = blocks[block_len - idx - 1]
        if re.match(r'\.+', block):
            continue
        print('----------')
        print('block', block, 'idx', idx)
        pointer = 0
        done = False
        while pointer < len(blocks) and pointer < block_len - idx and not done:
            if re.match(r'\.+', blocks[pointer]) and len(blocks[pointer]) >= len(block):
                print('space found at: ', pointer, ' swaping: ', blocks[block_len - idx - 1], blocks[pointer])
                blocks[block_len - idx - 1], blocks[pointer] = blocks[pointer], blocks[block_len - idx - 1]
                done = True
                sequence_str = ''.join(blocks)
                blocks = re.findall(r'0+|1+|2+|3+|4+|5+|6+|7+|8+|9+|\.+', sequence_str)
                print(blocks)
            pointer += 1
    
    print(blocks)

    print(sequence_str)
    for char_i, char in enumerate(re.findall('.', sequence_str)):
        if char == '.':
            break
        result = int(char) * char_i
        # print(char_i, ' * ', char, ' = ',result)
        value += result
    return value


pt2_value = pt2()

print('Part 1 Total: ', pt1_value)
print('Part 2 Total: ', pt2_value)
