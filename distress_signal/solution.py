
from typing import *

correct_order = -1

def main():
    with open("C:/Users/demia/Documents/Advent_of_Code/distress_signal/input.txt") as f:
        packet_number = 1
        packet_list = []
        while True:
            left = f.readline()
            right = f.readline()
            left = left.strip("\n")
            right = right.strip("\n")
            if not left.startswith("[") or not right.startswith("["):
                raise SyntaxError(f"FUCK YOU\n{left}\n{right}")
            left = eval(left)
            right = eval(right)
            process(left, right)
            if correct_order:
                packet_list.append(packet_number)
            EOF = f.readline()
            if EOF == "":
                break
            packet_number += 1
        print(packet_list)
        print(f"The sum is: {sum(packet_list)}")


    
def process(left: List, right: List):
    if len(left) > len(right):
        ret = False
    if len(left) <= len(right):
        ret = True 
    for left_val,right_val in zip(left,right):
        if isinstance(left_val, int) and isinstance(right_val, int):
            if handle_ints(left_val, right_val):
                return
        elif isinstance(left_val, List) ^ isinstance(right_val, List):
            if handle_list_int(left_val, right_val):
                return
        elif isinstance(left_val, List) and isinstance(right_val, List):
            if handle_lists(left_val, right_val):
                return
    global correct_order
    correct_order = ret

def handle_ints(left: int, right: int) -> bool:
    global correct_order
    if left < right:
        correct_order = True
        return True
    if left > right:
        correct_order = False
        return True
    return False

def handle_list_int(left, right) -> bool:
    if not isinstance(left, List):
        left = [left]
    if not isinstance(right, List):
        right = [right]
    return handle_lists(left, right)

def handle_lists(left: List, right: List) -> bool:
    if len(left) > len(right):
        con = 0
        ret = 0
    if len(left) < len(right):
        con = 0
        ret = 1
    if len(left) == len(right):
        con = 1
    for left_val,right_val in zip(left,right):
        if isinstance(left_val, int) and isinstance(right_val, int):
            if handle_ints(left_val, right_val):
                return True
        elif isinstance(left_val, List) ^ isinstance(right_val, List):
            if handle_list_int(left_val, right_val):
                return True
        elif isinstance(left_val, List) and isinstance(right_val, List):
            if handle_lists(left_val, right_val):
                return True
    if con == 1:
        return False
    global correct_order
    correct_order = ret
    return True

if __name__ == "__main__":
    main()