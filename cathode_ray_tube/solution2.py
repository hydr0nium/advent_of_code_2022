
from typing import *

def main():
    with open("./input.txt") as f:
        lines = f.readlines()
        process(lines)

def process(lines: str):
    sprite_pos = 1
    cycle = 0
    draw_pixel(cycle, sprite_pos)
    for instruction in lines:
        cycle += 1
        new_line(cycle)
        if instruction.startswith("noop"):
            draw_pixel(cycle, sprite_pos)
        elif instruction.startswith("addx"):
            draw_pixel(cycle, sprite_pos) 
            amount = int(instruction.split(" ")[1].strip("\n"))
            cycle +=1
            new_line(cycle)
            draw_pixel(cycle, sprite_pos)
            sprite_pos += amount
    
def new_line(cycle: int) -> bool:
    if cycle%40==0:
        print("\n", end="")

def draw_pixel(cycle: int, sprite_pos):
    cycle = cycle%40-1
    pixel = "."
    if cycle == sprite_pos or cycle == sprite_pos-1 or cycle == sprite_pos+1:
        pixel = "#"
    print(pixel, end="")


def remove_backslash_n(string: str):
    return string.strip("\n")

if __name__ == "__main__":
    main()