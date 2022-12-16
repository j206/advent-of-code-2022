def initialize():
    with open("./Day 14/d14_input.txt") as f:
        rock_paths = [l.strip() for l in f.readlines()]
    rock_paths = [x.split(" -> ") for x in rock_paths]
    rock_paths = [[x.split(",") for x in pair] for pair in rock_paths]
    rock_paths = [[[int(num) for num in pair] for pair in line]
                  for line in rock_paths]
    return rock_paths


rock_paths = initialize()

# Drop column is x == 12

def part1():
    draw_cave_map(rock_paths)
    return


def draw_cave_map(rock_paths):
    map, x_offset, drop_point = draw_empty_map(rock_paths)

    for line in rock_paths:
        start_x, start_y = line[0][0] - x_offset, line[0][1]
        print(start_x, start_y)

    return


def draw_empty_map(rock_paths):
    min_x = rock_paths[0][0][0]
    max_x = 0
    min_y = 0
    max_y = 0
    empty_map = []

    for line in rock_paths:
        for coordinate in line:
            if coordinate[0] < min_x:
                min_x = coordinate[0]
            if coordinate[0] > max_x:
                max_x = coordinate[0]
            if coordinate[1] > max_y:
                max_y = coordinate[1]

    drop_point = 500 - (min_x)
    x_offset = min_x

    for i in range(min_y, max_y):
        empty_map.append("." * (max_x - min_x))

    return empty_map, x_offset, drop_point


def print_map(map):
    for line in map:
        print(line)


part1()
