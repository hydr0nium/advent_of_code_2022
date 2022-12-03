import string
import typing

lower = string.ascii_lowercase
upper = string.ascii_uppercase

def is_in(string_a: str, string_b: str, string_c: str) -> int:
    for letter in string_a:
        if letter in string_b and letter in string_c:
            return letter_val(letter)
    return None

def letter_val(letter: str) -> int:
    if(ord(letter)<=90):
        return ord(letter)-38
    if(ord(letter)>90):
        return ord(letter)-96

def main():
    with open("./input") as f:
        lines = f.readlines()
        total = 0
        for i in range(0,len(lines),3):
            line_1 = lines[i]
            line_2 = lines[i+1]
            line_3 = lines[i+2]
            if line_1[-1]=="\n":
                line_1 = line_1[:-1]
            if line_2[-1]=="\n":
                line_2 = line_2[:-1]
            if line_3[-1]=="\n":
                line_3 = line_3[:-1]
            val = is_in(line_1,line_2,line_3)
            total += val
        print(total)

def process_input(line: str) -> int:
    pass

if __name__ == "__main__":
    main()