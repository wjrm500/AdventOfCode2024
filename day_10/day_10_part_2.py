import os
from collections import defaultdict

script_dir = os.path.dirname(os.path.abspath(__file__))

with open(f"{script_dir}/day_10_input.txt") as f:
    lines = f.readlines()
    lines = [line.rstrip("\n") for line in lines]

score = 0
def trailhead_score(map: list[list[int]], trailhead: tuple[int, int]):
    global score
    current_altitude = map[trailhead[0]][trailhead[1]]
    if current_altitude == 9:
        score += 1
        return
    new_positions = [
        (trailhead[0] - 1, trailhead[1]), # North
        (trailhead[0], trailhead[1] + 1), # East
        (trailhead[0] + 1, trailhead[1]), # South
        (trailhead[0], trailhead[1] - 1), # West
    ]
    for new_y, new_x in new_positions:
        if new_y < 0 or new_y >= len(map):
            continue
        if new_x < 0 or new_x >= len(map[0]):
            continue
        new_altitude = map[new_y][new_x]
        if new_altitude == current_altitude + 1:
            trailhead_score(map, (new_y, new_x))

map = [[int(num if num != "." else -1) for num in line] for line in lines]
for i in range(len(map)):
    line = map[i]
    for j in range(len(line)):
        altitude = line[j]
        if altitude == 0:
            trailhead_score(map, (i, j))
print(score)
# Answer: 1,494 - Correct