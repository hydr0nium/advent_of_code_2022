
reverse_lookup = {"A": "Rock", "B": "Paper", "C": "Scissors"}
score_round_end_lookup = {"X": 0, "Y": 3, "Z": 6}
score_lookup = {"Rock": 1, "Paper": 2, "Scissors": 3}
beaten_by_lookup = {"Rock": "Paper", "Scissors": "Rock", "Paper": "Scissors"}
beats_lookup = {"Rock": "Scissors", "Scissors": "Paper", "Paper": "Rock"}


def main():
    with open("./input") as f:
        lines = f.readlines()
        total = 0
        for line in lines:
            total += calc_round_score(line)
        print(total)


def calc_round_score(line):
    # Remove \n
    line = line[:-1]

    hands = line.split(" ")
    hand_oppenent = reverse_lookup[hands[0]]
    round_type_score = score_round_end_lookup[hands[1]]
    if (round_type_score==0):
        return score_lookup[beats_lookup[hand_oppenent]]
    if (round_type_score==3):
        # Because I play the same hand I can lookup the oppenents hand
        return score_lookup[hand_oppenent] + 3
    return score_lookup[beaten_by_lookup[hand_oppenent]] + 6



if __name__ == "__main__":
    main()