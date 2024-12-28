import os

import numpy as np

script_dir = os.path.dirname(os.path.abspath(__file__))

with open(f"{script_dir}/day_4_input.txt") as f:
    lines = f.readlines()

matrix = []
for line in lines:
    line = line.rstrip("\n")
    matrix.append([letter for letter in line])
matrix = np.array(matrix)

count = 0
for i in range(1, len(matrix) - 1):
    line = matrix[i]
    for j in range(1, len(line) - 1):
        letter = line[j]
        if letter == "A":
            line_above = matrix[i - 1]
            line_below = matrix[i + 1]
            top_left_letter = line_above[j - 1]
            bottom_right_letter = line_below[j + 1]
            top_left_bottom_right = top_left_letter + bottom_right_letter
            if top_left_bottom_right not in ["MS", "SM"]:
                continue
            top_right_letter = line_above[j + 1]
            bottom_left_letter = line_below[j - 1]
            top_right_bottom_left = top_right_letter + bottom_left_letter
            if top_right_bottom_left not in ["MS", "SM"]:
                continue
            count += 1
            
print(count)
# Answer: 1,933 - Correct