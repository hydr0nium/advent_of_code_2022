


reverse_lookup = {"A": "Rock", "B": "Paper", "C": "Scissors", "X": "Rock", "Y": "Paper", "Z": "Scissors" }
score_lookup = {"Rock": 1, "Paper": 2, "Scissors": 3}
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
    hand_me = reverse_lookup[hands[1]]
    if (hand_oppenent==hand_me):
        return score_lookup[hand_me] + 3
    if (beats_lookup[hand_me]==hand_oppenent):
        return score_lookup[hand_me] + 6
    return score_lookup[hand_me]



if __name__ == "__main__":
    main()