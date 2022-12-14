
from typing import *
import re
import pprint
max_x = 0
max_y = 0
min_x = 0
SHIFT = 300
def main():
    with open("./input.txt") as f:
        lines = f.readlines()
        everything = ""
        grid = {} # grid of format grid[(x,y)]
        for line in lines:
            everything += line
        pattern_y = re.compile("\d+,(\d+)")
        pattern_x = re.compile("(\d+),\d+")
        global max_x
        global max_y
        global min_x
        max_x = max(map(lambda x: int(x.strip("\n").strip()),re.findall(pattern_x,everything)))
        max_y = max(map(lambda x: int(x.strip("\n").strip()),re.findall(pattern_y,everything)))
        min_x = min(map(lambda x: int(x.strip("\n").strip()),re.findall(pattern_x,everything)))
        print(everything)
        print(max_x, max_y)
        # Init all with air
        for x in range(max_x+SHIFT):
            for y in range(max_y+SHIFT):
                grid[(x,y)] = "."
        # Init Stones
        for line in lines:
            process(line, grid)
        for x in range(max_x+SHIFT):
            grid[(x,max_y+2)] = "#"
        # Spawn Sand
        sand_spawn = 0
        print_grid(grid)
        while True:
            grid[(500,0)] = "o"
            x, y = move_sand(grid, 500, 0)
            if x==500 and y==0:
                sand_spawn += 1
                break
            sand_spawn += 1
        print_grid(grid)
        print(sand_spawn)

def print_grid(grid):
    global max_x
    global max_y
    global min_x
    print("--------------------")
    for y in range(max_y+SHIFT):
        for x in range(max_x+SHIFT):
            if x>min_x-SHIFT:
                print(grid[(x,y)], end="")
        print("\n", end="")
    print("---------------------")


def move_sand(grid: dict, x: int, y: int):
    try: 
        if grid[(x, y+1)] == ".":
            grid[(x, y)] = "."
            grid[(x, y+1)] = "o"
            return move_sand(grid, x, y+1)
        if grid[(x-1, y+1)] == ".":
            grid[(x, y)] = "."
            grid[(x-1, y+1)] = "o"
            return move_sand(grid, x-1, y+1)
        if grid[(x+1, y+1)] == ".":
            grid[(x, y)] = "."
            grid[(x+1, y+1)] = "o"
            return move_sand(grid, x+1, y+1)
        return x, y
    except:
        print_grid(grid)


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