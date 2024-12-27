import os

script_dir = os.path.dirname(os.path.abspath(__file__))

with open(f"{script_dir}/day_2_input.txt") as f:
    reports = f.readlines()
reports = [list(map(int, report.split())) for report in reports]

def is_report_safe(report):
    if len(report) < 2:
        return False
    if report[0] == report[1]:
        return False
    increasing = report[1] > report[0]
    previous_level = None
    for level in report:
        if previous_level is not None:
            if increasing and level <= previous_level:
                return False
            if not increasing and level >= previous_level:
                return False
            dist = abs(level - previous_level)
            if dist > 3:
                return False
        previous_level = level
    return True

if __name__ == "__main__":
    num_safe_reports = 0
    for report in reports:
        report_safe = is_report_safe(report)
        if report_safe:
            num_safe_reports += 1 
    print(num_safe_reports)
    # Answer: 680 - Correct