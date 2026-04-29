import re
import copy

# 47|53, means that if an update includes both page number 47 and page number 53, then page number 47 must be printed at some point before page number 53
# to break rule: 47 must be after 53


def parse_rules(rules, old_input):
    input = copy.deepcopy(old_input)
    for c in range(len(input)):
        if input[c] in rules:
            for page in rules[input[c]]:
                if page in input[c + 1 :]:
                    swap = input[c]
                    s_index = input.index(page)
                    input[c] = input[s_index]
                    input[s_index] = swap

    return input


def check_rules(rules, input):
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
        if not check_rules(rules, input):
            parsed_input = copy.deepcopy(input)
            while not check_rules(rules, parsed_input):
                parsed_input = parse_rules(rules, copy.deepcopy(parsed_input))
            total += parsed_input[len(parsed_input) // 2]

f.close()

print(total)
