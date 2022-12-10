


def main():
    with open("./input") as f:
        lines = f.readlines()
        total = 0
        for line in lines:
            # Remove \n
            if line[-1]=="\n":
                line = line[:-1]
            total += process_line(line)
        print(total)


def process_line(line) -> int:
    ranges = line.split(",")
    first = ranges[0].split("-")
    second = ranges[1].split("-")
    first_lower = int(first[0])
    first_upper = int(first[1])
    second_lower = int(second[0])
    second_upper = int(second[1])
    first_range = list(range(first_lower,first_upper+1))
    second_range = list(range(second_lower,second_upper+1))
    if contains(first_range,second_range):
        return 1
    return 0


def contains(a: list, b: list):
    return all([x in a for x in b]) or all([x in b for x in a])
    

if __name__ == "__main__":
    main()