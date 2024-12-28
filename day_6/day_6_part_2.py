import copy
import os
from collections import defaultdict
from itertools import cycle

script_dir = os.path.dirname(os.path.abspath(__file__))

with open(f"{script_dir}/day_6_input.txt") as f:
    lines = f.readlines()

matrix = [[point for point in line] for line in lines]

def go_north(guard_position, x_lim, y_lim):
    guard_position = (guard_position[0] - 1, guard_position[1])
    if guard_position[0] < 0:
        raise Exception("Guard wandered off map")
    return guard_position

def go_east(guard_position, x_lim, y_lim):
    guard_position = (guard_position[0], guard_position[1] + 1)
    if guard_position[1] >= x_lim:
        raise Exception("Guard wandered off map")
    return guard_position

def go_south(guard_position, x_lim, y_lim):
    guard_position = (guard_position[0] + 1, guard_position[1])
    if guard_position[0] >= y_lim:
        raise Exception("Guard wandered off map")
    return guard_position

def go_west(guard_position, x_lim, y_lim):
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

def find_guard_position(matrix):
    for i in range(len(matrix)):
        line = matrix[i]
        for j in range(len(line)):
            point = line[j]
            if point == "^":
                return (i, j)
    raise Exception("Guard does not exist")

def guard_route(matrix, guard_position):
    x_lim = len(matrix[0])
    y_lim = len(matrix)
    positions_visited = set([guard_position])
    directions = cycle(["N", "E", "S", "W"])
    for direction in directions:
        go_func = go_func_mapping[direction]
        while True:
            positions_visited.add(guard_position)
            try:
                new_guard_position = go_func(guard_position, x_lim, y_lim)
            except:
                return positions_visited
            if matrix[new_guard_position[0]][new_guard_position[1]] == "#":
                break
            guard_position = new_guard_position

def loops_with_obstacle(matrix, guard_position, obstacle_position):
    x_lim = len(matrix[0])
    y_lim = len(matrix)
    positions_visited = defaultdict(set)
    directions = cycle(["N", "E", "S", "W"])
    for direction in directions:
        go_func = go_func_mapping[direction]
        while True:
            if direction in positions_visited[guard_position]:
                return True
            positions_visited[guard_position].add(direction)
            try:
                new_guard_position = go_func(guard_position, x_lim, y_lim)
            except:
                return False
            if matrix[new_guard_position[0]][new_guard_position[1]] in ("#", "O"):
                break
            guard_position = new_guard_position

count = 0
guard_position = find_guard_position(matrix)
for obstacle_position in guard_route(matrix, guard_position):
    if obstacle_position == guard_position:
        continue
    matrix[obstacle_position[0]][obstacle_position[1]] = "O"
    if loops_with_obstacle(matrix, guard_position, obstacle_position):
        count += 1
    matrix[obstacle_position[0]][obstacle_position[1]] = "."
print(count)
# Answer: 1,663 - Correct