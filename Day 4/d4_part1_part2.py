with open("./Day 4/d4_input.txt") as f:
    assignments = f.readlines()


def part1():
    # in how many pairs does one range fully contain the other?
    contained_count = 0

    for assignment in assignments:
        p1_start, p1_end, p2_start, p2_end = format_assignment(assignment)

        if (p1_start <= p2_start and p1_end >= p2_end) or (p2_start <= p1_start and p2_end >= p1_end):
            contained_count += 1

    return print(contained_count)


def part2():
    # in how many pairs do ranges overlap, even partially?
    overlapped_count = 0

    for assignment in assignments:
        p1_start, p1_end, p2_start, p2_end = format_assignment(assignment)

        if check_overlap(p1_start, p1_end, p2_start, p2_end):
            overlapped_count += 1
    return print(overlapped_count)

def format_assignment(assignment):
    assignment_string = assignment.strip().replace(",", "-").split("-")
    assignment_int = [int(x) for x in assignment_string]
    p1_start, p1_end = assignment_int[0], assignment_int[1]
    p2_start, p2_end = assignment_int[2], assignment_int[3]
    return p1_start, p1_end, p2_start, p2_end


def check_overlap(p1_start, p1_end, p2_start, p2_end):
    # check if p2 starts during p1, and vice versa
    if (p1_start <= p2_start <= p1_end) or (p2_start <= p1_start <= p2_end):
        return True
    # check if p2 ends during p1, and vice versa
    elif (p1_start <= p2_end <= p1_end) or (p2_start <= p1_end <= p2_end):
        return True
    # check if p1 completely overlaps p2, and vice versa
    elif (p1_start <= p2_start and p1_end >= p2_end) or (p2_start <= p1_start and p2_end >= p1_end):
        return True
    else:
        return False

        
part1()
part2()

