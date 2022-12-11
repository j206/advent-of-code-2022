with open("./Day 10/d10_input_sample.txt") as f:
    instructions = [l.strip().split(" ") for l in f.readlines()]


def part2():
    sprite = 1
    cycle = 0
    queue = set()
    crt = ""

    for i, instruction in enumerate(instructions):
        # 1st, check if cycle is within -sprite- and draw it
        # 2nd, if instruction is addx, check if we need to move -sprite, ADVANCE CYCLE
        # 2nd, if instruction is noop, check if we need to move -sprite-, ADVANCE CYCLE
        # todo: its broken lol
        if instruction[0] == "addx":
            sprite = check_queue_for_completion(i, sprite, queue)

            crt = draw_pixel(crt, cycle, sprite)

            cycle += 1
            if cycle > 39:
                cycle = 0


        elif instruction[0] == "noop":
            sprite = check_queue_for_completion(i, sprite, queue)
            crt = draw_pixel(crt, cycle, sprite)
            cycle += 1
            if cycle > 39:
                cycle = 0
            queue.add(i)

    print(f"{cycle} | {sprite} | {sprite -1 <= cycle <= sprite + 1}")

    crt = format_crt(crt)
    return print(crt)


def check_queue_for_completion(i, sprite, queue):
    if (i - 1) in queue:
        sprite += int(instructions[i - 1][1])
        queue.remove(i - 1)
    return sprite


def draw_pixel(crt, cycle, sprite):
    if sprite - 1 <= cycle <= sprite + 1:
        crt += "#"
    else:
        crt += "."
    return crt

# https://stackoverflow.com/questions/65102013/


def format_crt(crt):
    new_input = ""
    for i, char in enumerate(crt):
        if i % 40 == 0:
            new_input += "\n"
        new_input += char
    return new_input


part2()
