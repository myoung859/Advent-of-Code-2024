import re

first_column = []
second_column = []

with open("day1.txt", "r") as f:
    for line in f.readlines():
        nums = re.findall(r"\d+", line)
        first_column.append(int(nums[0]))
        second_column.append(int(nums[1]))


total = 0
for num in first_column:
    total += num * sum([1 for i in second_column if i == num])

print(total)
