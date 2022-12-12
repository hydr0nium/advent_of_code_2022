from typing import *
import re
from math import floor
import numpy as np

# If you read this on github and understand why it works you are a legend.

ROUNDS = 10000
PRIMES_LOOKUP = {17: 0,
                7: 1,
                13: 2,
                2: 3,
                19: 4,
                3: 5,
                5: 6,
                11: 7}
PRIMES = [17, 7, 13, 2, 19, 3, 5, 11]


class Item():

    def __init__(self, id: int, worry_list: List[int]):
        self._id = id
        self._worry = worry_list

    def set_worry(self, new_values: List[int]):
        self._worry = new_values

    def get_worry(self) -> List[int]:
        return self._worry

    def __str__(self) -> str:
        return str(self._worry)


class Monkey():

    def __init__(self, id: int, starting_items: List[Item], divisor: int, monkey_id_true: int, monkey_id_false, operation: str, how_much: str):
        self._id: int = id
        self._items: List[Item] = starting_items
        self._divisor: int = int(divisor) 
        self._is_true: int = monkey_id_true
        self._is_false: int = monkey_id_false
        self._operation: int = operation
        self._how_much: str = how_much
        self._inspected = 0
    
    def operation(self, item: Item):
        if  self._operation == "*":
            if self._how_much == "old":
                list = item.get_worry()
                ret = []
                for index,worry in enumerate(list):
                    ret.append((worry*worry)%PRIMES[index])
                item.set_worry(ret)
            else:
                how_much = int(self._how_much)
                self._mult(int(how_much), item)
            return
        if  self._operation == "+":
            if self._how_much == "old":
                list = item.get_worry()
                ret = []
                for index,worry in enumerate(list):
                    ret.append((worry+worry)%PRIMES[index])
                item.set_worry(ret)
            else:
                how_much = int(self._how_much)
                self._add(int(how_much), item)
            return

    def test(self, item: Item) -> int:
        if item.get_worry()[PRIMES_LOOKUP[self._divisor]] == 0:    
            return self._is_true
        return self._is_false

    def process_items(self, all_monkeys: List['Monkey']):
        for item in self._items:
            self._inspected += 1
            self.operation(item)
            monkey_to = int(self.test(item))
            all_monkeys[monkey_to].add_item(item)
        self._items = []

    def add_item(self, item):
        self._items.append(item)

    def _mult(self, how_much, item: Item):
        new = []
        for index,worry in enumerate(item.get_worry()):
            new.append((worry*how_much)%(PRIMES[index]))
        item.set_worry(new)

    def _add(self, how_much, item: Item):
        new = []
        for index,worry in enumerate(item.get_worry()):
            new.append((worry+how_much)%(PRIMES[index]))
        item.set_worry(new)
    
    def get_inspected(self):
        return self._inspected

    def print_items(self):
        list = []
        for item in self._items:
            list.append(item.get_worry())
        print(list)

    def __str__(self) -> str:
        if len(self._items) >= 1:
            items = ""
            for item in self._items[:-1]:
                items += str(item) + ", "
            items += str(self._items[-1])
        else:
            items = ""
        return f'''
            Monkey {self._id}:
             Starting items: {items}
             Operation: new = old {self._operation} {self._how_much}
             Test: divisible by {self._divisor}
              If true: throw to monkey {self._is_true}
              If false: throw to monkey {self._is_false}
        
        '''


def main():
    with open("C:/Users/demia/Documents/Advent_of_Code/monkey_in_the_middle/input.txt") as f:
        monkeys: List[Monkey] = []
        while True:
            lines = []
            line = f.readline()
            if line == '':
                break
            lines.append(line)
            while True:
                line = f.readline()
                if line == "\n":
                    break
                if line == '':
                    break
                lines.append(line)
            monkeys.append(process(lines))
            if line == '':
                break

        for round in range(ROUNDS):
            for monkey in monkeys:
                monkey.process_items(monkeys)
        inspections = []
        for monkey in monkeys:
            
            inspections.append(monkey.get_inspected())
        inspections.sort(reverse=True)
        print(inspections)
        print(inspections[0]*inspections[1])


def process(monkey: List[str]) -> Monkey:
    id = monkey[0].split(" ")[1].split(":")[0]
    pattern = re.compile(r"\d+")
    worries = re.findall(pattern, monkey[1])
    items = []
    for item_id, worry in enumerate(worries):
        worry_list = []
        for prime in PRIMES:
            worry_list.append(int(worry)%prime)
        item = Item(item_id, worry_list)
        items.append(item)
    pattern = re.compile(r" \+|\* ")
    operation = re.search(pattern, monkey[2]).group().strip()
    pattern = re.compile(r"(:?\*|\+ ).+$")
    how_much = re.search(pattern, monkey[2]).group().strip().split(" ")[1].strip("\n")
    pattern = re.compile(r"\d+")
    divisor = re.search(pattern, monkey[3]).group()
    if_true = re.search(pattern, monkey[4]).group()
    if_false = re.search(pattern, monkey[5]).group()
    monkey_obj = Monkey(id,items,divisor,if_true,if_false,operation,how_much)
    return monkey_obj


def remove_backslash_n(string: str):
    return string.strip("\n")

if __name__ == "__main__":
    main()