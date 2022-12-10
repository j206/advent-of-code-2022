with open("./Day 9/d9_input.txt") as f:
    instructions = [l.strip() for l in f.readlines()]


def part1():
    head = [0, 0]
    tail = [0, 0]
    visited = set()

    for step in instructions:
        step = step.split(" ")
        direction, steps = step[0], int(step[1])
        head, tail = move(direction, steps, head, tail, visited)
    return print(len(visited))


def move(direction, steps, head, tail, visited):
    while steps > 0:
        # handle head
        if direction == "U":
            head[1] += 1
        elif direction == "D":
            head[1] -= 1
        elif direction == "L":
            head[0] -= 1
        else:
            head[0] += 1

        # handle tail
        tail = handle_tail(direction, head, tail)
        visited.add(tuple(tail))

        steps -= 1
    return head, tail


def handle_tail(direction, head, tail):
    # intercardinal shifts
    # Up-Left
    if ((head[0] - tail[0] == -2 and head[1] - tail[1] == 1) or
            (head[0] - tail[0] == -1 and head[1] - tail[1] == 2)):
        tail[0] -= 1
        tail[1] += 1
    # Up-Right
    elif ((head[0] - tail[0] == 1 and head[1] - tail[1] == 2) or
            (head[0] - tail[0] == 2 and head[1] - tail[1] == 1)):
        tail[0] += 1
        tail[1] += 1
    # Down-Right
    elif ((head[0] - tail[0] == 2 and head[1] - tail[1] == -1) or
            (head[0] - tail[0] == 1 and head[1] - tail[1] == -2)):
        tail[0] += 1
        tail[1] -= 1
    # Down-Left
    elif ((head[0] - tail[0] == -2 and head[1] - tail[1] == -1) or
            (head[0] - tail[0] == -1 and head[1] - tail[1] == -2)):
        tail[0] -= 1
        tail[1] -= 1

    # cardinal shifts
    elif (abs(head[0] - tail[0]) == 2 or abs(head[1] - tail[1]) == 2):
        if direction == "U":
            tail[1] += 1
        elif direction == "D":
            tail[1] -= 1
        elif direction == "L":
            tail[0] -= 1
        else:
            tail[0] += 1
    return tail


part1()
# 246 too low
# 3257 too low
# 3258 too low
