with open("./input") as f:
    file = f.readlines()
    list = []
    summe = 0
    for line in file:
        if line == "\n":
            list.append(summe)
            summe = 0
            continue
        summe += int(line[:-1])
    list.sort(reverse=True)
    print(sum(list[:3]))
    print(max(list))
