import re
import copy

total = 0
with open("day2.txt", "r") as f:
    for line in f.readlines():
        nums = [int(i) for i in re.findall(r"\d+", line)]
        for k in range(len(nums)):
            # note that if the list was already safe, popping the first element will also be a safe list
            # so just taking one element at a time shouldn't miss a previously safe list
            new_nums = copy.deepcopy(nums)
            new_nums.pop(k)
            diffs = [new_nums[i + 1] - new_nums[i] for i in range(len(new_nums) - 1)]
            if (all(i > 0 for i in diffs) or all(i < 0 for i in diffs)) and all(
                1 <= abs(i) <= 3 for i in diffs
            ):
                total += 1
                break
print(total)
