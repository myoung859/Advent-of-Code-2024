import re


total = 0
with open("day2.txt", "r") as f:
    for line in f.readlines():
        nums = [int(i) for i in re.findall(r"\d+", line)]
        diffs = [nums[i + 1] - nums[i] for i in range(len(nums) - 1)]
        if (all(i > 0 for i in diffs) or all(i < 0 for i in diffs)) and all(
            1 <= abs(i) <= 3 for i in diffs
        ):
            total += 1
print(total)
