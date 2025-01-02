
reports = []

with open("puzzle_2_input.txt", "r") as file:
    for line in file:
        levels = line.split()
        reports.append(levels)

    file.close()


def safe_reports(input):

    safe_reps = []
    for report in input:
        if report == sorted(report, reverse = True):
            safety = all(int(num1) - int(num2) in range(1,4) for num1, num2 in zip(report[:-1], report[1:]))
            safe_reps.append(safety)

        elif report == sorted(report, reverse = False):
            safety = all(int(num2) - int(num1) in range(1,4) for num1, num2 in zip(report[:-1], report[1:]))
            safe_reps.append(safety)

        else:
            safe_reps.append(False)

    # print(safe_reps)
    return safe_reps.count(True)

print(safe_reports(reports))

