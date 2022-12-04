with open("./Day 3/d3_input.txt") as f:
    rucksacks = f.readlines()


def build_dictionary():
    priority_values = {}
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    for i, letter in enumerate(lower_case, 1):
        priority_values[letter] = i

    for i, letter in enumerate(upper_case, 27):
        priority_values[letter] = i

    return priority_values


def part1():
    sum = 0
    values = build_dictionary()

    for rucksack in rucksacks:
        rucksack = rucksack.strip()
        midpoint = int(len(rucksack) / 2)

        # iterate front half items to hashset
        front_items = {}
        for item in rucksack[:midpoint]:
            front_items[item] = front_items.get(item, 0) + 1

        # iterate back half items, check if in front half set, get value for item, add to sum
        seen = set()
        for item in rucksack[midpoint:]:
            if item in front_items and item not in seen:
                sum += values[item]
                seen.add(item)
    return print(sum)


def part2():
    sum = 0
    values = build_dictionary()
    i = 0

    while i < len(rucksacks):
        counter += 1
        first = rucksacks[i].strip()
        second = rucksacks[i + 1].strip()
        third = rucksacks[i + 2].strip()
        first_set = set()
        second_set = set()

        for item in first:
            first_set.add(item)

        for item in second:
            if item in first_set:
                second_set.add(item)

        for item in third:
            if item in second_set:
                sum += values[item]
                break
        i += 3
    return print(sum)

part1()
part2()
