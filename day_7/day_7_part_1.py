import functools
import itertools
import os

script_dir = os.path.dirname(os.path.abspath(__file__))

with open(f"{script_dir}/day_7_input.txt") as f:
    lines = f.readlines()

@functools.cache
def get_possible_operator_sets(num_operators: int) -> list[list[str]]:
    possible_operator_sets = set()
    for i in range(num_operators + 1):
        s = ("+" * i) + ("*" * (num_operators - i))
        for permutation in itertools.permutations(s, num_operators):
            possible_operator_sets.add(permutation)
    return [[y for y in x] for x in possible_operator_sets] # Listify

def evaluate(operands: list[int], operator_set: list[str]) -> int:
    cumulative_value = operands[0]
    for i in range(1, len(operands)):
        value = operands[i]
        operator = operator_set[i - 1]
        cumulative_value = eval(f"{cumulative_value}{operator}{value}")
    return cumulative_value

def result_possible(expected_result: int, operands: list[int]) -> bool:
    num_operators = len(operands) - 1
    possible_operator_sets = get_possible_operator_sets(num_operators)
    for operator_set in possible_operator_sets:
        evaluated_result = evaluate(operands, operator_set)
        if evaluated_result == expected_result:
            return True
    return False

total = 0
for line in lines:
    expected_result, operands = line.split(": ")
    expected_result = int(expected_result)
    operands = list(map(int, operands.split()))
    if result_possible(expected_result, operands):
        total += expected_result
print(total)
# Answer: 975,671,981,569 - Correct