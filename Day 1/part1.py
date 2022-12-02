import os
with open("./Day 1/input.txt") as f:
    lines = f.readlines()

def part1():
    # how many total calories is that elf carrying?
    elf_count = max_entries = max_calories = current_entries = current_calories = 0
    for line in lines:
        if len(line) != 1:
            elf_count += 1
            current_entries = current_entries + 1
            current_calories += int(line.strip())

            if current_entries > max_entries:
                max_entries = current_entries
            if current_calories > max_calories:
                max_calories = current_calories
        else:
            current_entries = 0
            current_calories = 0
    return print(elf_count, max_entries, max_calories)


def part2():
    # how many calories are the top 3 calorie-carrying elves carrying?
    return
