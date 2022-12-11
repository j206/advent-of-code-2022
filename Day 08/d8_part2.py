with open("./Day 8/d8_input.txt") as f:
    rows = [[int(x) for x in list(l.strip())] for l in f.readlines()]


def part2():
    max_scenic_score = 0

    for i, row in enumerate(rows):
        for j, col in enumerate(row):
            # we don't care about edges
            if i == 0 or i == len(rows) - 1 or j == 0 or j == len(row) - 1:
                continue
            scenic_score = get_scenic_score(
                rows[i][j], i, len(rows), j, len(row))
            if scenic_score > max_scenic_score:
                max_scenic_score = scenic_score

    return print(max_scenic_score)


def get_scenic_score(current, i, max_i, j, max_j):
    left, right, up, down = 1, 1, 1, 1
    left_score, right_score, up_score, down_score = 0, 0, 0, 0

    while (j - left) >= 0:
        left_score += 1
        if rows[i][j - left] >= current:
            break
        left += 1

    while (j + right) < max_j:
        right_score += 1
        if rows[i][j + right] >= current:
            break
        right += 1

    while (i - up) >= 0:
        up_score += 1
        if rows[i - up][j] >= current:
            break
        up += 1

    while (i + down) < max_i:
        down_score += 1
        if rows[i + down][j] >= current:
            break
        down += 1

    return left_score * right_score * up_score * down_score


part2()
