
from typing import *
import re
import pprint

def main():
    with open("./input.txt") as f:
        lines = f.readlines()
        everything = ""
        grid = {} # grid of format grid[(x,y)]
        for line in lines:
            everything += line
        pattern_y = re.compile("\d+,(\d+)")
        pattern_x = re.compile("(\d+),\d+")
        max_x = max(map(lambda x: int(x.strip("\n").strip()),re.findall(pattern_x,everything)))
        max_y = max(map(lambda x: int(x.strip("\n").strip()),re.findall(pattern_y,everything)))
        min_x = min(map(lambda x: int(x.strip("\n").strip()),re.findall(pattern_x,everything)))
        print(everything)
        print(max_x, max_y)
        # Init all with air
        for x in range(max_x+2):
            for y in range(max_y+2):
                grid[(x,y)] = "."
        # Init Stones
        for line in lines:
            process(line, grid)
        # Spawn Sand
        sand_spawn = 0
        while True:
            grid[(500,0)] = "o"
            if move_sand(grid, 500, 0, max_y=max_y):
                break
            sand_spawn += 1
        print_grid(grid, max_x+2, max_y+2, min_x)
        print(sand_spawn)

def print_grid(grid, x_max, y_max, min_x:int):
    for y in range(y_max):
        for x in range(x_max):
            if x>min_x-2:
                print(grid[(x,y)], end="")
        print("\n", end="")


def move_sand(grid: dict, x: int, y: int, max_y):
    if y > max_y:
        return True
    if grid[(x, y+1)] == ".":
        grid[(x, y)] = "."
        grid[(x, y+1)] = "o"
        return move_sand(grid, x, y+1, max_y)
    if grid[(x-1, y+1)] == ".":
        grid[(x, y)] = "."
        grid[(x-1, y+1)] = "o"
        return move_sand(grid, x-1, y+1, max_y)
    if grid[(x+1, y+1)] == ".":
        grid[(x, y)] = "."
        grid[(x+1, y+1)] = "o"
        return move_sand(grid, x+1, y+1, max_y)
    return False
        


def process(line: str, grid: dict):
    coords = line.split("->")
    for i in range(len(coords)-1):
        coord = coords[i]
        x_1 = int(coord.split(",")[0].strip("\n").strip())
        y_1 = int(coord.split(",")[1].strip("\n").strip())
        coord = coords[i+1]
        x_2 = int(coord.split(",")[0].strip("\n").strip())
        y_2 = int(coord.split(",")[1].strip("\n").strip())
        if x_1 == x_2:
            draw_y(grid, y_1, y_2, x_1)
        elif y_1 == y_2:
            draw_x(grid, x_1, x_2, y_1)
    pass

def draw_x(grid, x_1, x_2, y):
    if x_1 > x_2:
        x_2, x_1 = x_1, x_2
    assert(x_1 < x_2)
    for x in range(x_1, x_2+1):
        grid[(x,y)] = "#"

def draw_y(grid, y_1, y_2, x):
    if y_1 > y_2:
        y_2, y_1 = y_1, y_2
    assert(y_1 < y_2)
    for y in range(y_1, y_2+1):
        grid[(x,y)] = "#"



if __name__ == "__main__":
    main()