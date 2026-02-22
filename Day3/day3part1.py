import re

total = 0
# slight complication with this one. There are newlines in the real input txt.
with open("day3.txt", "r") as f:
    for line in f.readlines():
        ops = re.findall(r"mul\(\d{1,3},\d{1,3}\)", line)
        for op in ops:
            nums = re.findall(r"\d+", op)
            total += int(nums[0]) * int(nums[1])
print(total)
