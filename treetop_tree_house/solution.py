
from typing import *
import re

def main():
    with open("./input.txt") as f:
        lines = f.readlines()
        treemap: List[str] = []
        split_pattern = re.compile(r".")
        for line in lines:
            line = re.findall(split_pattern, line)
            line = [int(x) for x in line]
            treemap.append(line)
        sum = process_part_1(treemap)
        print(sum)
        best = process_part_2(treemap)
        print(best)


# treemap[y][x]        --[x]->
#       -------------------------------------------------------
#      |
#   |  | 
# y[x] |                    TREENUMBERS
#   |  |
#   v  |
#      |

def process_part_1(treemap: List[str]) -> int:
    sum = 0
    for y in range(len(treemap)):
        for x in range(len(treemap[0])):
            if visible(treemap, x, y):
                sum += 1
    return sum

def visible(treemap: List[str], x: int, y: int) -> bool:
    x_max = len(treemap[0])-1
    y_max = len(treemap)-1
    tree_height = treemap[y][x]
    if x==0 or y==0 or x==x_max or y==y_max:
        return True
    last = 0

    if all([tree_height>treemap[y][x_run_left] for x_run_left in range(0,x)]):
        return True
    if all([tree_height>treemap[y_run_top][x] for y_run_top in range(0,y)]):
        return True
    if all([tree_height>treemap[y][x_run_right] for x_run_right in range(x+1,x_max+1)]):
        return True
    if all([tree_height>treemap[y_run_bottom][x] for y_run_bottom in range(y+1,y_max+1)]):
        return True
    return False

def scenic_score(treemap: List[str], x:int, y:int):
    x_max = len(treemap[0])
    y_max = len(treemap)
    tree_height = treemap[y][x]
    score_left = 0
    score_right = 0
    score_top = 0
    score_down = 0
    
    count = 0
    #print(f"Tree at {x} {y}")
    for x_run_left in range(x-1,-1,-1):
        if treemap[y][x_run_left]>=tree_height:
            count +=1
            break
        count +=1
    score_left += count

    count = 0
    for y_run_top in range(y-1,-1,-1):
        if treemap[y_run_top][x]>=tree_height:
            count +=1
            break
        count +=1
    score_top += count

    count = 0
    for x_run_right in range(x+1,x_max):
        if treemap[y][x_run_right]>=tree_height:
            count +=1
            break
        count +=1
    score_right += count

    count = 0
    for y_run_down in range(y+1,y_max):
        if treemap[y_run_down][x]>=tree_height:
            count +=1
            break
        count +=1
    score_down += count
    #print(f"{score_top}*{score_left}*{score_down}*{score_right}")
    return score_right*score_left*score_down*score_top

def process_part_2(treemap: List[str]) -> int:
    best = scenic_score(treemap, 0, 0)
    for y in range(len(treemap)):
        for x in range(len(treemap[0])):
            scenic_score_val = scenic_score(treemap, x, y)
            #print(f"Scenic Score: {scenic_score_val}")
            if scenic_score_val>best:
                best = scenic_score_val
    return best


def remove_backslash_n(string: str):
    return string.strip("\n")

if __name__ == "__main__":
    main()