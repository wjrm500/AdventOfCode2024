import os
import re

script_dir = os.path.dirname(os.path.abspath(__file__))

with open(f"{script_dir}/day_3_input.txt") as f:
    text = f.read()

text = "do()" + text + "don't()"
dos = re.finditer("do\(\)", text)
donts = re.finditer("don't\(\)", text)

do_starts = [("do", m.start(0)) for m in dos]
dont_starts = [("don't", m.start(0)) for m in donts]
do_dont_starts = do_starts + dont_starts
do_dont_starts.sort(key=lambda x: x[1])
enabled_spans = [[0, 0]]
enabled = True
for do_dont, start in do_dont_starts:
    if enabled:
        enabled_spans[-1][1] = start
    if not enabled and do_dont == "do":
        enabled_spans.append([start, start])
    enabled = do_dont == "do"

multiplication_matches = re.finditer(r"mul\(\d{1,3},\d{1,3}\)", text)
total = 0
for multiplication_match in multiplication_matches:
    multi_start = multiplication_match.start(0)
    for enabled_span in enabled_spans:
        if enabled_span[0] <= multi_start <= enabled_span[1]:
            enabled = True
            break
    else:
        enabled = False 
    if enabled:
        multiplication = multiplication_match.group(0)
        nums = multiplication.lstrip("mul(").rstrip(")").split(",")
        total += int(nums[0]) * int(nums[1])
print(total)
# Answer: 89,823,704 - Correct