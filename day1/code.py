input_data = "data/input.txt"
# input_data = 'data/example.txt'

# PART ONE

value = 50
zeros_part_1 = 0

with open(input_data, "r") as file:
    for line in file:
        direction, number = line.strip()[0], int(line.strip()[1:])
        print("------------")
        print(direction, number)

        if direction.lower() == "r":
            print(f"Adding {number} to {value}")
            value += number
        elif direction.lower() == "l":
            print(f"Subtracting {number} from {value}")
            value -= number

        print(f"Pre-formatted value: {value}")
        while value > 99:
            value -= 100
        while value < 0:
            value += 100

        if value == 0:
            zeros_part_1 += 1
        print(f"Post-formatted value: {value}")
print(zeros_part_1)

# PART TWO

# Needed to change the fundamental algo as we wanted to catch every time the "0" is clicked

value = 50
zeros_part_2 = 0

with open(input_data, "r") as file:
    for line in file:
        direction, number = line.strip()[0], int(line.strip()[1:])
        print("------------")
        print(direction, number)

        if direction.lower() == "r":
            print(f"Adding {number} to {value}")
            while number > 0:
                value += 1
                number -= 1
                if value > 99:
                    value = 0
                if value == 0:
                    zeros_part_2 += 1
        elif direction.lower() == "l":
            print(f"Subtracting {number} from {value}")
            while number > 0:
                value -= 1
                number -= 1
                if value < 0:
                    value = 99
                if value == 0:
                    zeros_part_2 += 1
print(zeros_part_2)

print("============ END ===========")
print(f"Part 1 Zeros: {zeros_part_1}")
print(f"Part 2 Zeros: {zeros_part_2}")
