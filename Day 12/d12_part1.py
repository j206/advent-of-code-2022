with open("./Day 12/d12_input.txt") as f:
    map = [l.strip() for l in f.readlines()]


def part1():
    start, end = find_start(map)

    return


def dfs(i, j, steps, seen):
    if not are_neighbors_navigable(i, j, seen):
        return


def are_neighbors_navigable(i, j, seen):
    # Check if up/down/left/right is out of bounds or already visited
    if ((map[i][j - 1] in seen or map[i][j - 1] < 0 or ord(map[i][j - 1]) - ord(map[i][j]) > 1) or
            (map[i][j + 1] in seen or map[i][j + 1] > len(map[i]) or ord(map[i][j + 1]) - ord(map[i][j]) > 1) or
            (map[i - 1][j] in seen or map[i - 1][j] < 0 or ord(map[i - 1][j]) - ord(map[i][j]) > 1) or
            (map[i + 1][j] in seen or map[i + 1][j] > len(map) or ord(map[i + 1][j]) - ord(map[i][j]) > 1)):
        return False
    return True


def find_start(map):
    # brutal O(n^2)
    for i in range(len(map)):
        for j in range(len(map[i])):
            if map[i][j] == "S":
                start = [i, j]

    for i in range(len(map)):
        for j in range(len(map[i])):
            if map[i][j] == "E":
                end = [i, j]

    return start, end


part1()

# check all sides
# if side is navigable, increase count and run dfs again
