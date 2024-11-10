# https://adventofcode.com/2022/day/1

def find_highest_calories():
    calories = []
    individual_elf = []

    with open("input_data.txt", "r") as file:
        for line in file:
            line = line.strip()

            if not line:
                calories.append(individual_elf)
                individual_elf = []
            else:
                individual_elf.append(int(line))


    sum_calories = [sum(elf) for elf in calories]
    return max(sum_calories)



