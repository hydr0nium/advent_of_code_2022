
from typing import *

def main():
    with open("./input.txt") as f:
        lines = f.readlines()
        data_list = process(lines)
        print(data_list)
        print(sum(data_list))

def process(lines: str):
    register_x = 1
    cycle = 0
    important_data = []
    for instruction in lines:
        cycle += 1
        if instruction.startswith("noop"):
            if check_state(cycle): important_data.append(cycle*register_x) 
        elif instruction.startswith("addx"):
            if check_state(cycle): important_data.append(cycle*register_x) 
            amount = int(instruction.split(" ")[1].strip("\n"))
            cycle +=1
            if check_state(cycle): important_data.append(cycle*register_x)
            register_x += amount
    return important_data
    
def check_state(cycle: int) -> bool:
    if cycle < 40 and cycle == 20:
        return True
    if cycle > 40 and (cycle+20)%40==0:
        return True
    return False

def remove_backslash_n(string: str):
    return string.strip("\n")

if __name__ == "__main__":
    main()