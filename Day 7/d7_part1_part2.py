import re
with open("./Day 7/d7_input.txt") as f:
    inputs = f.readlines()


def part1_iterative():
    total_size = 0
    branch_size = 0
    folder_size = 0
    file_system = build_file_system()
    seen = set()

    print(file_system)


def build_file_system():
    file_system = {}
    dir = ""

    for i, input in enumerate(inputs):
        input = input.strip()

        # move out of folder
        if input[:7] == "$ cd ..":
            # we necessarily have been there
            # before fixing dir, calculate
            # add sizes of folders starting from leaf
            dir = '/'.join(dir.split("/")[:-1])
        # move into folder
        elif input[:4] == "$ cd":
            folder_name = input.split("$ cd ")[1]
            file_system[]
            dir += "/" + folder_name
            if dir not in file_system:
                file_system[folder_name] = {'size': get_folder_size(i)}

    return file_system


def get_folder_size(i):
    i += 1
    size = 0
    # somethin
    while i < len(inputs) and inputs[i][:4] != "$ cd":
        if inputs[i][0].isnumeric():
            size += int(re.findall('\d+', inputs[i])[0])
        i += 1
    return size


def get_branch_size(dir, seen):
    print(seen)
    return


part1_iterative()
