with open("./Day 10/d10_input.txt") as f:
    instructions = [l.strip().split(" ") for l in f.readlines()]


def part1():
    x = 1
    cycle = 0
    signal_strength = 0
    queue = set()

    for i, instruction in enumerate(instructions):
        cycle += 1
        x = check_queue_for_completion(i, x, queue)

        # handle signal strength
        if (cycle % 40) == 20:
            signal_strength += (x * cycle)

        if instruction[0] == "addx":
            cycle += 1
            queue.add(i)

            # handle signal strength again
            if (cycle % 40) == 20:
                signal_strength += (x * cycle)

    return print(signal_strength)


def check_queue_for_completion(i, x, queue):
    if (i - 1) in queue:
        x += int(instructions[i - 1][1])
        queue.remove(i - 1)
    return x


part1()
