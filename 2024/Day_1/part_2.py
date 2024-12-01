from collections import Counter

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


similarity_scores = []
num_counter = Counter(second_list)

for num in first_list:
    if num not in second_list:
        continue
    elif num in second_list:
        score = num * num_counter[num]
        similarity_scores.append(score)


total_similarity = sum(similarity_scores)
print(total_similarity)