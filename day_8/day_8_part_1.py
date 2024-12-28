import itertools
import math
import os
from collections import defaultdict

import numpy as np

script_dir = os.path.dirname(os.path.abspath(__file__))

with open(f"{script_dir}/day_8_input.txt") as f:
    lines = f.readlines()
    lines = [line.rstrip("\n") for line in lines]

class Locus:
    def __init__(self, antenna, x, y):
        self.antenna = antenna
        self.x = x
        self.y = y
        self.antinode = False
    
    def __repr__(self):
        return f"({self.x}, {self.y})"
    
    def antinode_positions(self, other: "Locus"):
        return (
            (self.x - (other.x - self.x), self.y - (other.y - self.y)),
            (other.x + (other.x - self.x), other.y + (other.y - self.y)),
        )

loci: list[Locus] = []
x_lim = len(lines[0])
y_lim = len(lines)
for i in range(x_lim):
    line = lines[i]
    for j in range(y_lim):
        antenna = line[j] if line[j] != "." else None
        locus = Locus(antenna, x=j, y=i)
        loci.append(locus)

loci_by_antenna = defaultdict(list)
for locus in loci:
    if locus.antenna:
        loci_by_antenna[locus.antenna].append(locus)

loci_pairs: list[tuple[Locus]] = []
for antenna, loci in loci_by_antenna.items():
    loci_pairs.extend(itertools.combinations(loci, 2))

all_antinode_positions = set()
for locus_1, locus_2 in loci_pairs:
    for antinode_position in locus_1.antinode_positions(locus_2):
        antinode_x = antinode_position[0]
        antinode_y = antinode_position[1]
        if antinode_x < 0 or antinode_x >= x_lim:
            continue
        if antinode_y < 0 or antinode_y >= y_lim:
            continue
        all_antinode_positions.add(antinode_position)
    
print(len(all_antinode_positions))
# Answer: 228 - Correct