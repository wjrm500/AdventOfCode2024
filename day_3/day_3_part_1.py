import os
import re

script_dir = os.path.dirname(os.path.abspath(__file__))

with open(f"{script_dir}/day_3_input.txt") as f:
    text = f.read()
multiplications = re.findall(r"mul\(\d{1,3},\d{1,3}\)", text)
total = 0
for multiplication in multiplications:
    nums = multiplication.lstrip("mul(").rstrip(")").split(",")
    total += int(nums[0]) * int(nums[1])
print(total)
# Answer: 167,090,022 - Correct