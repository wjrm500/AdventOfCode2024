import itertools
import os
from collections import defaultdict

script_dir = os.path.dirname(os.path.abspath(__file__))

with open(f"{script_dir}/day_8_input.txt") as f:
    lines = f.readlines()
    lines = [line.rstrip("\n") for line in lines]

class Antinode:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __eq__(self, other: "Antinode"):
        return (self.x, self.y) == (other.x, other.y)
    
    def __hash__(self):
        return hash((self.x, self.y))

class Antenna:
    def __init__(self, symbol, x, y):
        self.symbol = symbol
        self.x = x
        self.y = y
    
    def __repr__(self):
        return f"({self.x}, {self.y})"
    
    def get_antinodes(self, other: "Antenna") -> tuple[Antinode, Antinode]:
        return (
            Antinode(self.x - (other.x - self.x), self.y - (other.y - self.y)),
            Antinode(other.x + (other.x - self.x), other.y + (other.y - self.y)),
        )


antenni: list[Antenna] = []
x_lim = len(lines[0])
y_lim = len(lines)
for i in range(x_lim):
    line = lines[i]
    for j in range(y_lim):
        if (symbol := line[j]) == ".":
            continue
        antenna = Antenna(symbol, x=j, y=i)
        antenni.append(antenna)

antenni_by_symbol = defaultdict(list)
for antenna in antenni:
    if antenna.symbol:
        antenni_by_symbol[antenna.symbol].append(antenna)

antenna_pairs: list[tuple[Antenna]] = []
for symbol, antenna in antenni_by_symbol.items():
    antenna_pairs.extend(itertools.combinations(antenna, 2))

all_antinodes = set()
for antenna_1, antenna_2 in antenna_pairs:
    for antinode in antenna_1.get_antinodes(antenna_2):
        if antinode.x < 0 or antinode.x >= x_lim:
            continue
        if antinode.y < 0 or antinode.y >= y_lim:
            continue
        all_antinodes.add(antinode)
    
print(len(all_antinodes))
# Answer: 228 - Correct