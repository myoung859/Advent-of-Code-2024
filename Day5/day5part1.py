import re
import copy

# 47|53, means that if an update includes both page number 47 and page number 53, then page number 47 must be printed at some point before page number 53
# to break rule: 47 must be after 53


def parse_rules(rules, input):
    for c, i in enumerate(input):
        if i in rules:
            for page in rules[i]:
                if page in input[c:]:
                    return False
    return True


f = open("day5.txt", "r")
rules = {}
total = 0

for line in f.readlines():
    if "|" in line:
        match = re.findall(r"\d+", line)
        first_num = int(match[0])
        second_num = int(match[1])
        if second_num in rules:
            rules[second_num].append(first_num)
        else:
            rules[second_num] = [first_num]
    elif "," in line:
        match = re.findall(r"\d+", line)
        input = [int(i) for i in match]
        if parse_rules(rules, input):
            total += input[len(input) // 2]
f.close()

print(total)
