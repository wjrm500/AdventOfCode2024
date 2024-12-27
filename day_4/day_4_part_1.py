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

def flipped_matrices(matrix):
    return [
        matrix,
        np.flip(matrix, 0),
        np.flip(matrix, 1),
        np.flip(matrix, (0, 1)),
    ]

def tranposed_matrices(matrix):
    return [
        matrix,
        np.flip(matrix, 1), # Horizontally flipped
        np.transpose(matrix), # Transposed
        np.flip(np.transpose(matrix), 1), # Transposed and horizontally flipped
    ]

def find_straight_xmas_count(matrix):
    count = 0
    for flipped_matrix in tranposed_matrices(matrix):
        for line in flipped_matrix:
            count += "".join(line).count("XMAS")
    return count

def find_southeast_diagonal_xmas_count(matrix):
    count = 0
    for i in range(len(matrix) - 3):
        x_line = matrix[i]
        m_line = matrix[i + 1]
        a_line = matrix[i + 2]
        s_line = matrix[i + 3]
        for j in range(len(x_line) - 3):
            possible_x = x_line[j]
            if possible_x == "X":
                if m_line[j + 1] == "M":
                    if a_line[j + 2] == "A":
                        if s_line[j + 3] == "S":
                            count += 1
    return count

def find_diagonal_xmas_count(matrix):
    count = 0
    for flipped_matrix in flipped_matrices(matrix):
        count += find_southeast_diagonal_xmas_count(flipped_matrix)
    return count

def find_xmas_count(matrix):
    return find_straight_xmas_count(matrix) + find_diagonal_xmas_count(matrix)

print(find_xmas_count(matrix))
# Answer: 2500 - Correct