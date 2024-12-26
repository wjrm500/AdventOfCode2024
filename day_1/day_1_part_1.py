import os

script_dir = os.path.dirname(os.path.abspath(__file__))

with open(f"{script_dir}/day_1_input.txt") as f:
    text = f.readlines()
xs, ys = [], []
for line in text:
    line = line.rstrip("\n")
    x, y = map(int, line.split())
    xs.append(x)
    ys.append(y)
xs.sort()
ys.sort()
zipped = zip(xs, ys)
total = 0
for x, y in zipped:
    total += abs(y - x)
print(total)
# Answer: 2,769,675 - Correct