with open("./Day 8/d8_input.txt") as f:
    rows = [[int(x) for x in list(l.strip())] for l in f.readlines()]


def part1():
    visible = 0
    
    for i, row in enumerate(rows):
        for j, col in enumerate(row):
            if i == 0 or i == len(rows) - 1 or j == 0 or j == len(row) - 1:
                visible += 1

            elif is_visible(rows[i][j], i, len(rows), j, len(row)):
                visible += 1

    return print(visible)


def is_visible(current, i, max_i, j, max_j):
    left, right, up, down = 1, 1, 1, 1
    sides_visible = 4

    while (j - left) >= 0:
        if rows[i][j - left] >= current:
            sides_visible -= 1
            break
        left += 1

    while (j + right) < max_j:
        if rows[i][j + right] >= current:
            sides_visible -= 1
            break
        right += 1

    while (i - up) >= 0:
        if rows[i - up][j] >= current:
            sides_visible -= 1
            break
        up += 1

    while (i + down) < max_i:
        if rows[i + down][j] >= current:
            sides_visible -= 1
            break
        down += 1

    return sides_visible


part1()
