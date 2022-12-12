from typing import *
import re
from math import floor

ROUNDS = 20

class Item():

    def __init__(self, id: int, worry_level: int):
        self._id = id
        self._worry = worry_level

    def set_worry(self, new_value: int):
        self._worry = new_value

    def get_worry(self) -> int:
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
                how_much = item.get_worry()
            else:
                how_much = int(self._how_much)
            self._mult(how_much, item)
            return
        if  self._operation == "+":
            if self._how_much == "old":
                how_much = item.get_worry()
            else:
                how_much = int(self._how_much)
            self._add(how_much, item)
            return

    def test(self, item: Item) -> int:
        if  item.get_worry() % self._divisor == 0:
            return self._is_true
        return self._is_false

    def process_items(self, all_monkeys: List['Monkey']):
        for item in self._items:
            self._inspected += 1
            self.operation(item)
            item.set_worry(floor(item.get_worry()/3))
            monkey_to = int(self.test(item))
            all_monkeys[monkey_to].add_item(item)
        self._items = []

    def add_item(self, item):
        self._items.append(item)

    def _mult(self, how_much, item: Item):
        old = item.get_worry()
        item.set_worry(old * how_much)

    def _add(self, how_much, item: Item):
        old = item.get_worry()
        item.set_worry(old + how_much)
    
    def get_inspected(self):
        return self._inspected

    def __str__(self) -> str:
        items = ""
        for item in self._items[:-1]:
            items += item.__str__() + ", "
        items += self._items[-1].__str__()
        return f'''
            Monkey {self._id}:
             Starting items: {items}
             Operation: new = old {self._operation} {self._how_much}
             Test: divisible by {self._divisor}
              If true: throw to monkey {self._is_true}
              If false: throw to monkey {self._is_false}
        
        '''


def main():
    with open("./input.txt") as f:
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
        for _ in range(ROUNDS):
            for monkey in monkeys:
                monkey.process_items(monkeys)
        inspections = []
        for monkey in monkeys:
            inspections.append(monkey.get_inspected())
        inspections.sort(reverse=True)
        print(inspections[0]*inspections[1])


def process(monkey: List[str]) -> Monkey:
    id = monkey[0].split(" ")[1].split(":")[0]
    pattern = re.compile(r"\d+")
    worries = re.findall(pattern, monkey[1])
    items = []
    for item_id, worry in enumerate(worries):
        item = Item(item_id, int(worry))
        items.append(item)
    pattern = re.compile(r" \+|\* ")
    operation = re.search(pattern, monkey[2]).group().strip()
    pattern = re.compile(r"(:?\*|\+ ).+$")
    how_much = re.search(pattern, monkey[2]).group().strip().split(" ")[1].strip("\n")
    pattern = re.compile(r"\d+")
    divisor = re.search(pattern, monkey[3]).group()
    if_true = re.search(pattern, monkey[4]).group()
    if_false = re.search(pattern, monkey[5]).group()
    monkey_obj = Monkey(id, items,divisor,if_true,if_false,operation,how_much)
    return monkey_obj


def remove_backslash_n(string: str):
    return string.strip("\n")

if __name__ == "__main__":
    main()