import re

with open("./Day 5/d5_input.txt") as f:
    manifest = f.readlines()

BOTTOM_OF_STACK_ROW = 8
FIRST_PROCEDURE_ROW = 10


def part1():
    top_item = ""
    stacks = build_initial_state(manifest)

    for i, instruction in enumerate(manifest[FIRST_PROCEDURE_ROW:]):
        instruction_int = [int(x)
                           for x in re.findall('\d+', instruction.strip())]

        origin = stacks[instruction_int[1] - 1]
        target = stacks[instruction_int[2] - 1]
        move_counter = instruction_int[0]

        while move_counter > 0:
            target.append(origin.pop())
            move_counter -= 1

    for stack in stacks:
        top_item += stack.pop()

    return print(top_item)


def part2():
    top_item = ""
    stacks = build_initial_state(manifest)

    for i, instruction in enumerate(manifest[FIRST_PROCEDURE_ROW:]):
        instruction_int = [int(x)
                           for x in re.findall('\d+', instruction.strip())]

        origin = stacks[instruction_int[1] - 1]
        target = stacks[instruction_int[2] - 1]
        crates_to_move = instruction_int[0]
        lifted = []

        for i in range(len(origin), len(origin) - crates_to_move, -1):
            lifted.append(origin.pop())

        lifted.reverse()
        for crate in lifted:
            target.append(crate)

    for stack in stacks:
        top_item += stack.pop()

    return print(top_item)


# messy lol but my dinner is ready
def build_initial_state(manifest):
    c1, c2, c3, c4, c5, c6, c7, c8, c9 = ([] for i in range(9))
    for i in range(BOTTOM_OF_STACK_ROW, -1, -1):
        if manifest[i][1].isalpha():
            c1.append(manifest[i][1])
        if manifest[i][5].isalpha():
            c2.append(manifest[i][5])
        if manifest[i][9].isalpha():
            c3.append(manifest[i][9])
        if manifest[i][13].isalpha():
            c4.append(manifest[i][13])
        if manifest[i][17].isalpha():
            c5.append(manifest[i][17])
        if manifest[i][21].isalpha():
            c6.append(manifest[i][21])
        if manifest[i][25].isalpha():
            c7.append(manifest[i][25])
        if manifest[i][29].isalpha():
            c8.append(manifest[i][29])
        if manifest[i][33].isalpha():
            c9.append(manifest[i][33])
    return [c1, c2, c3, c4, c5, c6, c7, c8, c9]


part1()
part2()