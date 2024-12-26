import os

from collections import defaultdict

script_dir = os.path.dirname(os.path.abspath(__file__))

with open(f"{script_dir}/day_1_input.txt") as f:
    text = f.readlines()
xs, ys = [], defaultdict(int)
for line in text:
    line = line.rstrip("\n")
    x, y = map(int, line.split())
    xs.append(x)
    ys[y] += 1
similarity_score = 0
for x in xs:
    similarity_score += x * ys[x]
print(similarity_score)
# Answer: 24,643,097 - Correct