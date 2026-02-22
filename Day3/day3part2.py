import re

total = 0
do_switch = True
# slight complication with this one. There are newlines in the real input txt.
with open("day3.txt", "r") as f:
    for line in f.readlines():
        ops = re.findall(r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)", line)
        for op in ops:
            if op == "do()":
                do_switch = True
            elif op == "don't()":
                do_switch = False
            elif do_switch:  # it's a mul() and do() is more recent than don't()
                nums = re.findall(r"\d+", op)
                total += int(nums[0]) * int(nums[1])
print(total)
