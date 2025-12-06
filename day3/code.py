# input_data = "data/input.txt"
input_data = 'data/example.txt'

# PART ONE

sum = 0

with open(input_data, "r") as file:
    for line in file:
        print(f"Processing line: {line.strip()}")
        outer_check = 9
        while outer_check > 0:
            print(f"Looking for outer digit: {outer_check}")
            if str(outer_check) in line.strip():
                outer_check_index = line.strip().find(str(outer_check))
                if outer_check_index + 1 >= len(line.strip()):
                    outer_check -= 1
                    continue
                if outer_check_index == len(line.strip()) - 1:
                    outer_check -= 1
                    continue
                rest_of_the_line = line.strip()[outer_check_index + 1 :]

                inner_check = 9
                while inner_check > 0:
                    print(f"  Looking for inner digit: {inner_check} in {rest_of_the_line}")
                    if str(inner_check) in rest_of_the_line:
                        sum += int(f"{outer_check}{inner_check}")
                        print(f"Found pair: {outer_check}{inner_check}")
                        break
                    else:
                        inner_check -= 1
                else:
                    continue
                break
            else:
                outer_check -= 1
print(sum)

# PART TWO

# Honestly I'm going to try to use the combinations tool to brute force this one
# QUEUE ME TRYING THE BRUTE FORCE METHOD THAT TOOK MINUTES JUST FOR THE FIRST LINE ;___;

# from itertools import combinations
#
# sum = 0
#
# with open(input_data, "r") as file:
#     for line in file:
#         print(f"Processing line: {line.strip()}")
#         maximum = 0
#         for combo in combinations(line.strip(), 12):
#             if int("".join(combo)) > maximum:
#                 maximum = int("".join(combo))
#                 print(f"  New maximum found: {maximum} with combo {combo}")
#         sum += maximum
#
# print(sum)

# Okay let's instead try to find the maximum value possible in the string instead

sum = 0

with open(input_data, "r") as file:
    for line in file:
        line = line.strip()
        print(f"Processing line: {line}")
        maximum = 999999999999
        while maximum > 0:
            print(f"  Trying maximum: {maximum}")
            for char in str(maximum):
                if char in line:
                    maximum_str_index = line.find(char)
                    line = line[maximum_str_index + 1 :]
            else:
                maximum -= 1
                continue
        sum += maximum

print(sum)


