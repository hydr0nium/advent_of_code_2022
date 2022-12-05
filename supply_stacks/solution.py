import queue as qu
from typing import *
import re

class Cargo:
    
    def __init__(self, cargos: list):
        self.cargos = cargos


    def move(self, amount: int, source: int, dest: int):
        source = source-1
        dest = dest-1
        for _ in range(amount):
            crate = self.cargos[source].get()
            self.cargos[dest].put(crate)
            
    def move2(self, amount: int, source: int, dest: int):
        source = source-1
        dest = dest-1
        cache = []
        for _ in range(amount):
            cache.append(self.cargos[source].get())
        cache = cache[::-1]
        for crate in cache:
            self.cargos[dest].put(crate)

    def get_tops(self) -> str:
        ret = []
        for q in self.cargos:
            ret.append(q.get())
        print("".join(ret))

    def print(self):
        i = 1
        for stack in self.cargos:
            print(i, stack.queue)
            i += 1


def main():
    with open("./input") as f:
        lines = f.readlines()
        stacks = read_in(lines[:10])
        cargo = Cargo(stacks)
        for line in lines[10::]:
            process_1(cargo, line)
        cargo.get_tops()
    with open("./input") as f:
        lines = f.readlines()
        stacks = read_in(lines[:10])
        cargo = Cargo(stacks)
        for line in lines[10::]:
            process_2(cargo, line)
        cargo.get_tops()


def process_1(cargo, line: str):
    numbers = re.findall(r"( \d+ | \d)", line)
    amount = int(numbers[0].strip())
    source = int(numbers[1].strip())
    dest = int(numbers[2].strip())
    cargo.move(amount, source, dest)

def process_2(cargo, line: str):
    numbers = re.findall(r"( \d+ | \d)", line)
    amount = int(numbers[0].strip())
    source = int(numbers[1].strip())
    dest = int(numbers[2].strip())
    cargo.move2(amount, source, dest)


def read_in(lines):
    ret = []
    for _ in range(9):
        ret.append(qu.LifoQueue())
    lines = lines[:-2]
    for line in lines[::-1]:
        i = 0
        row = re.findall(r"(.{4}|.{3}\n)", line)
        for crate in row:
            if crate != "    ":
                ret[i].put(crate[1])
            i += 1
    return ret


if __name__ == "__main__":
    main()