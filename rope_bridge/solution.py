
# Return true if head and tail are ontop of each other or in the distance of 1 of each other
def near(tail,head):
    first = abs(head[0]-tail[0])
    second = abs(head[1]-tail[1])
    if abs(head[0]-tail[0])<=1 and abs(head[1]-tail[1])<=1:
        return True
    return False

def make_move(head, tail, move):
    m = move
    direction = move[0]
    if direction == "R":
        head = (head[0] + 1, head[1])
    elif direction == "L":
        head = (head[0] - 1, head[1])
    elif direction == "U":
        head = (head[0], head[1] + 1)
    elif direction == "D":
        head = (head[0], head[1] - 1)
    if not near(tail,head):
        if head[0] == tail[0]:
            if head[1] > tail[1]:
                tail = (tail[0], tail[1] + 1)
            elif head[1] < tail[1]:
                tail = (tail[0], tail[1] - 1)
        elif head[1] == tail[1]:
            if head[0] > tail[0]:
                tail = (tail[0] + 1, tail[1])
            elif head[0] < tail[0]:
                tail = (tail[0] - 1, tail[1])
        elif head[1] > tail[1] and head[0] > tail[0]:
            tail = (tail[0] + 1, tail[1])
            tail = (tail[0], tail[1] + 1)
        elif head[1] > tail[1] and head[0] < tail[0]:
            tail = (tail[0], tail[1] + 1)
            tail = (tail[0] - 1, tail[1])
        elif head[1] < tail [1] and head[0] < tail[0]:
            tail = (tail[0] - 1, tail[1])
            tail = (tail[0], tail[1] - 1)
        elif head[1] < tail[1] and head[0] > tail[0]:
            tail = (tail[0], tail[1] - 1)
            tail = (tail[0] + 1, tail[1])
    return head,tail

def move_head(head, move):
    m = move
    direction = move[0]
    if direction == "R":
        head = (head[0] + 1, head[1])
    elif direction == "L":
        head = (head[0] - 1, head[1])
    elif direction == "U":
        head = (head[0], head[1] + 1)
    elif direction == "D":
        head = (head[0], head[1] - 1)
    return head

def move_tail(head, tail):
    if not near(tail,head):
        if head[0] == tail[0]:
            if head[1] > tail[1]:
                tail = (tail[0], tail[1] + 1)
            elif head[1] < tail[1]:
                tail = (tail[0], tail[1] - 1)
        elif head[1] == tail[1]:
            if head[0] > tail[0]:
                tail = (tail[0] + 1, tail[1])
            elif head[0] < tail[0]:
                tail = (tail[0] - 1, tail[1])
        elif head[1] > tail[1] and head[0] > tail[0]:
            tail = (tail[0] + 1, tail[1])
            tail = (tail[0], tail[1] + 1)
        elif head[1] > tail[1] and head[0] < tail[0]:
            tail = (tail[0], tail[1] + 1)
            tail = (tail[0] - 1, tail[1])
        elif head[1] < tail [1] and head[0] < tail[0]:
            tail = (tail[0] - 1, tail[1])
            tail = (tail[0], tail[1] - 1)
        elif head[1] < tail[1] and head[0] > tail[0]:
            tail = (tail[0], tail[1] - 1)
            tail = (tail[0] + 1, tail[1])
    return tail


# Parse the input
with open("input.txt") as f:
    moves = f.read().strip().split("\n")
moves = [m.split() for m in moves]


# PART 1 
# Initialize the head and tail positions
head = (0, 0)
tail= (0, 0)
visited = {(0, 0)}

# Loop through the moves and update the head and tail positions
for move in moves:
    
    distance = int(move[1])
    # Update the head position
    for i in range(distance):
        head, tail = make_move(head, tail, move)
        visited.add(tail)


# Print the result
print(f"PART 1: The tail visited {len(visited)} distinct squares, including the starting square.")

# PART 2
# Initialize the head and tail positions
head = (0, 0)
tail= (0, 0)
tail_list = [(0, 0),(0, 0),(0, 0),(0, 0),(0, 0),(0, 0),(0, 0),(0, 0),(0, 0),(0, 0)]
visited = {(0, 0)}

# Loop through the moves and update the head and tail positions
for move in moves:
    direction = move[0]
    distance = int(move[1])
    # Update the head position
    for i in range(distance):
        head = move_head(head, move)
        last = head
        for i in range(1,len(tail_list)):
            tail = tail_list[i]
            tail = move_tail(last,tail)
            tail_list[i] = tail
            if i == 9:    
                visited.add(tail)
            last = tail

# Print the result
print(f"PART 2: The tail visited {len(visited)} distinct squares, including the starting square.")