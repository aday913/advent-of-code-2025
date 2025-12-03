input_data = "data/input.txt"
# input_data = 'data/example.txt'

# PART ONE

sum = 0

with open(input_data, "r") as file:
    raw_data = file.read().strip()

    ranges = raw_data.split(",")

    for r in ranges:
        start, end = map(int, r.split("-"))
        print(f"Processing range: {start} to {end}")

        for number in range(start, end + 1):
            string_number = str(number)
            test_string = ""
            index = 0

            while index < len(string_number) - 1:
                test_string += string_number[index]
                if f"{test_string}{test_string}" == string_number:
                    print(f"Found double: {string_number}")
                    sum += number
                index += 1
print(sum)
sum_1 = sum

# PART TWO

sum = 0

with open(input_data, "r") as file:
    raw_data = file.read().strip()

    ranges = raw_data.split(",")

    for r in ranges:
        start, end = map(int, r.split("-"))
        print(f"Processing range: {start} to {end}")

        all_invalids = []
        for number in range(start, end + 1):
            string_number = str(number)
            test_string = ""
            index = 0

            while index < len(string_number) - 1:
                test_string += string_number[index]
                check_string = test_string
                while len(check_string) < len(string_number):
                    check_string += test_string
                    if check_string == string_number:
                        if string_number in all_invalids:
                            continue
                        all_invalids.append(string_number)
                        print(
                            f"Found pattern: {test_string} in {string_number}: {check_string}"
                        )
                        sum += number
                index += 1
print(sum)
sum_2 = sum

print("============ END ===========")
print(f"Part 1 Sum: {sum_1}")
print(f"Part 2 Sum: {sum_2}")
