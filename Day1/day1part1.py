import re

first_column = []
second_column = []

with open("day1.txt", "r") as f:
    for line in f.readlines():
        nums = re.findall(r"\d+", line)
        first_column.append(int(nums[0]))
        second_column.append(int(nums[1]))

first_column.sort()
second_column.sort()


total = sum([abs(i - j) for i, j in zip(first_column, second_column)])
print(total)
