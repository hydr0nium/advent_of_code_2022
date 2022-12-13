
from typing import *
import functools as ft

correct_order = -1

def main():
    with open("./input.txt") as f:
        packet_number = 1
        packet_list = []
        while True:
            packet = f.readline()
            if packet == "":
                break
            if packet == "\n":
                continue
            if not packet.startswith("["):
                raise SyntaxError(f"FUCK YOU\n{packet}")
            packet = eval(packet)
            packet_list.append(packet)
        packet_list.append([[2]])
        packet_list.append([[6]])
        sorted_packets: List = sorted(packet_list, key=ft.cmp_to_key(cmp_func))
        print(sorted_packets)
        index1 = sorted_packets.index([[2]])+1
        index2 = sorted_packets.index([[6]])+1
        print(f"The decoder key is: {index1*index2}")

def cmp_func(a, b):
    process(a,b)
    if correct_order:
        return -1
    if not correct_order:
        return 1
    raise ValueError("Comparison Failed")
    
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