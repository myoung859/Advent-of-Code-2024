import re
import itertools

f = open("day7.txt")
total_cal = 0
for line in f.readlines():
    nums = [int(i) for i in re.findall(r"\d+", line)]
    target = nums[0]
    test_nums = nums[1:]
    for ops in itertools.product(("+", "*", "||"), repeat=len(test_nums) - 1):
        result = test_nums[0]
        for i in range(0, len(ops)):
            if ops[i] == "+":
                result += test_nums[i + 1]
            elif ops[i] == "*":
                result *= test_nums[i + 1]
            elif ops[i] == "||":
                result = int(str(result) + str(test_nums[i + 1]))
        if result == target:
            total_cal += target
            break
print(total_cal)
