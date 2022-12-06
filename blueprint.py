
from typing import *

def main():
    with open("./input.txt") as f:
        lines = f.readlines()
        for line in lines:
            process(line)

def process(line: str):
    pass

def remove_backslash_n(string: str):
    return string.strip("\n")

if __name__ == "__main__":
    main()