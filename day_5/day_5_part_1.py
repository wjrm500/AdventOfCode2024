import math
import os
from collections import defaultdict

script_dir = os.path.dirname(os.path.abspath(__file__))

with open(f"{script_dir}/day_5_input.txt") as f:
    text = f.read()

rule_text, update_text = text.split("\n\n")

rules = defaultdict(list)
for rule in rule_text.split("\n"):
    k, v  = rule.split("|")
    rules[k].append(v)

updates = update_text.split("\n")
updates = [update.split(",") for update in updates]

def update_correct(update):
    for i in range(len(update)):
        for j in range(len(update) - i - 1):
            before_page = update[i]
            after_page = update[i + j + 1]
            should_be_after = rules[after_page]
            if before_page in should_be_after:
                return False
    return True

def middle_number(update):
    return int(update[math.floor(len(update) / 2)])

total = 0
for update in updates:
    if update_correct(update):
        total += middle_number(update)
print(total)
# Answer: 6,384 - Correct