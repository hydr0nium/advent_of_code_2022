import string
import typing

lower = string.ascii_lowercase
upper = string.ascii_uppercase

def is_in(source: str, destination: str) -> str:
    for letter in source:
        if letter in destination:
            return letter
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
        for line in lines:
            # Remove \n
            if line[-1]=="\n":
                line = line[:-1]
            val = process_input(line)
            total += val
        print(total)

def process_input(line: str) -> int:
    
    if(len(line)%2!=0):
        raise Exception("Line len is not even",line,len(line))

    length = len(line)//2
    first_half = line[:length]
    second_half = line[length::]
    common_letter = is_in(first_half,second_half)
    if common_letter==None:
        raise Exception(first_half,second_half)
    letter_value = letter_val(common_letter)
    return letter_value

if __name__ == "__main__":
    main()