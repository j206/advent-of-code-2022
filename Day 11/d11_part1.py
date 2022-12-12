import re
import math

with open("./Day 11/d11_input.txt") as f:
    lines = [l.strip() for l in f.readlines()]


class Monkey:
    def __init__(self, items, operation, test, count):
        self.items = items
        self.operation = operation
        self.test = test
        self.count = count


def part1():
    crew = assemble_crew(lines)
    round = 1

    while round <= 20:
        for id in range(len(crew)):
            while len(crew[id].items) > 0:
                # Monkey inspection
                crew[id].items[0] = item_inspection(
                    crew[id], crew[id].items[0])
                crew[id].count += 1

                # # Monkey worry check and item toss
                if crew[id].items[0] % crew[id].test["divisible_by"] == 0:
                    target = crew[id].test["true_target"]
                    crew[target].items.append(crew[id].items.pop(0))
                else:
                    target = crew[id].test["false_target"]
                    crew[target].items.append(crew[id].items.pop(0))
        round += 1

    return print(get_monkey_business(crew))


def assemble_crew(lines):
    crew = []
    for i, line in enumerate(lines):
        if line[:6] == "Monkey":
            # Set starting items
            items = [int(x) for x in re.findall('\d+', lines[i + 1])]

            # Set operation
            operator = re.search('(\+|\-|\/|\*)', lines[i + 2]).group(0)
            value = lines[i + 2].split(" ")[-1]
            operation = {
                "operator": operator,
                "value": value
            }

            # Set test
            divisible_by = int(lines[i + 3].split(" ")[-1])
            true_target = int(lines[i + 4].split(" ")[-1])
            false_target = int(lines[i + 5].split(" ")[-1])
            test = {
                "divisible_by": divisible_by,
                "true_target": true_target,
                "false_target": false_target
            }

            monkey = Monkey(items, operation, test, 0)
            crew.append(monkey)

    return crew


def item_inspection(monkey, item):
    do_math = {
        "+": (lambda x, y: x + y),
        "-": (lambda x, y: x - y),
        "/": (lambda x, y: x / y),
        "*": (lambda x, y: x * y),
    }

    if monkey.operation["value"] == "old":
        value = monkey.items[0]
    else:
        value = int(monkey.operation["value"])

    new_worry_level = do_math[monkey.operation["operator"]](
        item, value)
    new_worry_level = math.floor(new_worry_level / 3)

    return new_worry_level


def get_monkey_business(crew):
    power_levels = [monkey.count for monkey in crew]
    number1 = max(power_levels)
    power_levels.remove(number1)
    number2 = max(power_levels)
    return number1 * number2


part1()
