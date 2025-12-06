input_data = "data/input.txt"
# input_data = "data/example.txt"

import time

def green(text):
    # return text
    return f"\033[92m{text}\033[00m"


def red(text):
    # return text
    return f"\033[91m{text}\033[00m"


def strip_color(text):
    return text.replace("\033[92m", "").replace("\033[91m", "").replace("\033[00m", "")


sum = 0
map = []

with open(input_data, "r") as file:
    for line in file:
        map.append(line.strip())

num_rows = len(map)
num_cols = len(map[0])


def check_nearby(row, col, map):
    if map[row][col] in [".", red("X")]:
        return None

    directions = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]

    num_rolls = 0
    for dr, dc in directions:
        new_row = row + dr
        new_col = col + dc

        if new_row < 0 or new_row >= num_rows or new_col < 0 or new_col >= num_cols:
            continue

        if map[new_row][new_col] == "@":
            num_rolls += 1
    return num_rolls


def check_nearby_v2(row, col, local_map):
    if strip_color(local_map[row][col]) in [".", "X"]:
        return None

    directions = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]

    num_rolls = 0
    for dr, dc in directions:
        new_row = row + dr
        new_col = col + dc

        if new_row < 0 or new_row >= num_rows or new_col < 0 or new_col >= num_cols:
            continue

        if strip_color(local_map[new_row][new_col]) == "@":
            num_rolls += 1
    return num_rolls


# PART ONE


num_available = 0
new_map = []

for row in range(num_rows):
    new_row = ""
    for col in range(num_cols):
        nearby_rolls = check_nearby(row, col, map)
        if nearby_rolls == None:
            new_row += "."
            continue

        if nearby_rolls < 4:
            new_row += red("X")
            num_available += 1
        else:
            new_row += green("@")
    new_map.append(new_row)
for line in new_map:
    print(line)
print("--------------------------------------------")
print(f"Number of available rolls: {num_available}")

# PART TWO

total_num_available = 0
could_remove_rolls = True
new_map = map

while could_remove_rolls:
    num_available = 0
    current_map = new_map
    new_map = []
    for row in range(num_rows):
        new_row = ""
        for col in range(num_cols):
            nearby_rolls = check_nearby_v2(row, col, current_map)
            if nearby_rolls == None:
                new_row += current_map[row][col]
                continue

            if nearby_rolls < 4:
                new_row += "X"
                num_available += 1
            else:
                new_row += "@"
        new_map.append(new_row)
    visual_map = []
    for line in new_map:
        visual_map.append(
            "".join(
                [
                    green(char) if char == "@" else red(char) if char == "X" else char
                    for char in line
                ]
            )
        )
    for line in visual_map:
        print(line)
    if num_available == 0:
        could_remove_rolls = False
    else:
        total_num_available += num_available
    time.sleep(.5)
    print("---")
print("--------------------------------------------")
print(f"Total number of available rolls: {total_num_available}")
