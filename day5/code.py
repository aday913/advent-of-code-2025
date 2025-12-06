input_data = "data/input.txt"
# input_data = "data/example.txt"

all_ranges = []
all_test_values = []
with open(input_data, "r") as file:
    add_to_ranges = True
    for line in file:
        if line.strip() == "":
            add_to_ranges = False
            continue

        if add_to_ranges:
            parts = line.strip().split("-")
            all_ranges.append([int(parts[0]), int(parts[1])])
        else:
            all_test_values.append(int(line.strip()))
for ran in all_ranges:
    ran.sort()

# PART ONE

num_fresh = 0
for test_value in all_test_values:
    is_fresh = False
    for r in all_ranges:
        if test_value >= r[0] and test_value <= r[1]:
            is_fresh = True
            break
    if is_fresh:
        num_fresh += 1
print(f"Number of fresh items: {num_fresh}")

# PART TWO

outer_changed_a_range = True
while outer_changed_a_range:
    final_ranges = []
    for old_ran in all_ranges:
        changed_a_range = False
        for final_ran in final_ranges:
            if old_ran[1] < final_ran[0]:
                continue
            elif old_ran[0] > final_ran[1]:
                continue
            elif old_ran[0] <= final_ran[0] and old_ran[1] >= final_ran[1]:
                # If the input range encompases the existing range totally
                print(f"Range {old_ran} completely encompases {final_ran}")
                final_ranges.remove(final_ran)
                final_ranges.append([old_ran[0], old_ran[1]])
                changed_a_range = True
                break
            elif old_ran[0] > final_ran[0] and old_ran[1] < final_ran[1]:
                print(f"Range {old_ran} already encompassed by {final_ran}, skipping")
                changed_a_range = True
                break
            elif old_ran[0] <= final_ran[0]:
                # If the input range encompases the existing range on the right
                print(f"Range {old_ran} envelops {final_ran} on the right")
                final_ranges.remove(final_ran)
                final_ranges.append([old_ran[0], final_ran[1]])
                changed_a_range = True
                break
            elif old_ran[1] >= final_ran[1]:
                # If the input range encompases the existing range on the left
                print(f"Range {old_ran} envelops {final_ran} on the left")
                final_ranges.remove(final_ran)
                final_ranges.append([final_ran[0], old_ran[1]])
                changed_a_range = True
                break
        if not changed_a_range:
            print(f"Range {old_ran} does not exist yet, adding...")
            final_ranges.append([old_ran[0], old_ran[1]])
    if all_ranges == final_ranges:
        outer_changed_a_range = False
    all_ranges = final_ranges

total = 0
print("Final ranges:")
for ran in final_ranges:
    print(f"  {ran[0]} - {ran[1]}")
    difference = 1 + (ran[1] - ran[0])
    total += difference
print(f"Total number of values possible: {total}")
