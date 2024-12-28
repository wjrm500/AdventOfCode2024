import os

from itertools import cycle

script_dir = os.path.dirname(os.path.abspath(__file__))

with open(f"{script_dir}/day_6_input.txt") as f:
    lines = f.readlines()

matrix = [[point for point in line] for line in lines]

guard_position = None
for i in range(len(matrix)):
    line = matrix[i]
    for j in range(len(line)):
        point = line[j]
        if point == "^":
            guard_position = (i, j)

x_lim = len(matrix[0])
y_lim = len(matrix)

def go_north(guard_position):
    guard_position = (guard_position[0] - 1, guard_position[1])
    if guard_position[0] < 0:
        raise Exception("Guard wandered off map")
    return guard_position

def go_east(guard_position):
    guard_position = (guard_position[0], guard_position[1] + 1)
    if guard_position[1] >= x_lim:
        raise Exception("Guard wandered off map")
    return guard_position

def go_south(guard_position):
    guard_position = (guard_position[0] + 1, guard_position[1])
    if guard_position[0] >= y_lim:
        raise Exception("Guard wandered off map")
    return guard_position

def go_west(guard_position):
    guard_position = (guard_position[0], guard_position[1] - 1)
    if guard_position[1] < 0:
        raise Exception("Guard wandered off map")
    return guard_position

go_func_mapping = {
    "N": go_north,
    "E": go_east,
    "S": go_south,
    "W": go_west,
}

positions_visited = set([guard_position])
try:
    directions = cycle(["N", "E", "S", "W"])
    for direction in directions:
        go_func = go_func_mapping[direction]
        while True:
            positions_visited.add(guard_position)
            new_guard_position = go_func(guard_position)
            if matrix[new_guard_position[0]][new_guard_position[1]] == "#":
                break
            guard_position = new_guard_position
except:
    print(len(positions_visited))
    SHOW_MATRIX = 0
    if SHOW_MATRIX:
        for i in range(len(matrix)):
            line = matrix[i]
            for j in range(len(line)):
                point = line[j]
                if (i, j) in positions_visited:
                    point = "X"
                print(point, end="")
            print("")
# Answer: 4,982 - Correct