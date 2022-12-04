with open("./Day 1/d1_input.txt") as f:
    lines = f.readlines()


def part1():
    # how many total calories is that elf carrying?
    max_calories = current_calories = 0
    for line in lines:
        if len(line) != 1:
            current_calories += int(line.strip())

            if current_calories > max_calories:
                max_calories = current_calories
        else:
            current_calories = 0
    return print("part 1: ", max_calories)


def part2():
    # how many calories are the top 3 calorie-carrying elves carrying?
    current_calories = 0
    top_three = [0, 0, 0]
    for line in lines:
        if len(line) != 1:
            current_calories += int(line.strip())
        else:
            if current_calories > min(top_three):
                top_three.remove(min(top_three))
                top_three.append(current_calories)

            current_calories = 0
    return print("part 2: ", sum(top_three))


part1()
part2()
