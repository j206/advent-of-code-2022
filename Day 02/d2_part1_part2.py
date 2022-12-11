with open("./Day 2/d2_input.txt") as f:
    rounds = f.readlines()


p1_wins = {"A Z": [1, 3], "B X": [2, 1], "C Y": [3, 2]}
p2_wins = {"C X": [3, 1], "A Y": [1, 2], "B Z": [2, 3]}
draws = {"A X": 1, "B Y": 2, "C Z": 3}


def part1():
    # RPS
    # Win = 6 + val, Draw = 3 + val, Lose = 0 + val
    # very overengineered solution lol
    p1_score = 0
    p2_score = 0

    for round in rounds:
        round = round.strip()
        if round in p1_wins:
            p1_score += 6 + p1_wins[round][0]
            p2_score += p1_wins[round][1]
        elif round in p2_wins:
            p1_score += p2_wins[round][0]
            p2_score += 6 + p2_wins[round][1]
        elif round in draws:
            p1_score += 3 + draws[round]
            p2_score += 3 + draws[round]
    return print([p1_score, p2_score])


def part2():
    p2_score = 0

    for round in rounds:
        round = round.strip()
        # X = LOSE
        if round[2] == "X":
            if round[0] == "A": p2_score += 3
            if round[0] == "B": p2_score += 1
            if round[0] == "C": p2_score += 2
        # Y = DRAW
        if round[2] == "Y":
            if round[0] == "A": p2_score += 3 + 1
            if round[0] == "B": p2_score += 3 + 2
            if round[0] == "C": p2_score += 3 + 3
        # Z = WIN
        if round[2] == "Z":
            if round[0] == "A": p2_score += 6 + 2
            if round[0] == "B": p2_score += 6 + 3
            if round[0] == "C": p2_score += 6 + 1
    return print(p2_score)

part1()
part2()