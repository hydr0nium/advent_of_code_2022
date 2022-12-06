
from typing import *

distinct_char_num = 4

def main():
    with open("./input.txt") as f:
        lines = f.readlines()
        for line in lines:
            print(process(line))
            global distinct_char_num
            distinct_char_num = 14
            print(process(line))


def process(line: str):
    for pos in range(len(line[:-distinct_char_num:])):
        subline = line[pos:pos+distinct_char_num]
        if no_duplicate(subline):
            return pos+distinct_char_num
    raise Exception("No non duplicated len substring found")

def no_duplicate(subline):
    return len(set(subline))==distinct_char_num

def remove_backslash_n(string: str):
    return string.strip("\n")

if __name__ == "__main__":
    main()