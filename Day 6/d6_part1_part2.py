with open("./Day 6/d6_input.txt") as f:
    data = f.readlines()[0]


def part1():
    window = [data[0], data[1], data[2], data[3]]

    i = 0
    while i < len(data):
        # to check for equality of items in array, compare length of array with length of set
        if (len(set(window)) == len(window)):
            return print(i + 4)
        window.remove(data[i])
        window.append(data[i + 4])
        i += 1


def part2():
    window = [data[x] for x in range(0, 15)]

    i = 0
    while i < len(data):
        if (len(set(window)) == len(window)):
            return print(i + 14)
        window.remove(data[i])
        window.append(data[i + 14])
        i += 1


part1()
part2()
