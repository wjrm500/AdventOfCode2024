import os

from day_2_part_1 import is_report_safe 

script_dir = os.path.dirname(os.path.abspath(__file__))

with open(f"{script_dir}/day_2_input.txt") as f:
    reports = f.readlines()
reports = [list(map(int, report.split())) for report in reports]

def is_report_safe_with_dampener(report):
    if is_report_safe(report):
        return True
    for dampened_index in range(len(report)):
        dampened_report = [level for index, level in enumerate(report) if index != dampened_index]
        if is_report_safe(dampened_report):
            return True
    return False

num_safe_reports_with_dampener = 0
for i, report in enumerate(reports):
    report_safe_with_dampener = is_report_safe_with_dampener(report)
    if report_safe_with_dampener:
        num_safe_reports_with_dampener += 1 
print(num_safe_reports_with_dampener)
# Answer: 710 - Correct