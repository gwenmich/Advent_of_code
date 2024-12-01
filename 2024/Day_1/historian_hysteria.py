# https://adventofcode.com/2024/day/1

first_list = []
second_list = []

with open("puzzle_1_input.txt", "r") as file:
    for line in file:
        numbers = line.split()
        first_num = int(numbers[0])
        second_num = int(numbers[1])
        first_list.append(first_num)
        second_list.append(second_num)

    file.close()

# find difference between smallest numbers of each list
first_list.sort()
second_list.sort()

total_differences = []
i = 0
for num in first_list:
    difference = abs(num - second_list[i])
    total_differences.append(difference)
    i += 1

total_distance = sum(total_differences)

print(total_distance)
