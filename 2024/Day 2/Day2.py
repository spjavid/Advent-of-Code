import numpy as np

filename = "C:\\Users\\sjavi\\OneDrive\\Documents\\Advent of Code\\2024\\Day 2\\input.txt"

# Reading the data from the file

rows = []
with open(filename, 'r') as file:
    for line in file:
        row = list(map(int, line.split()))
        rows.append(row)

removed_numbers = []

# Function to perform the increment/decrement check with the specified difference conditions
def check_row(row):
    is_incrementing = all(1 <= (row[i+1] - row[i]) <= 3 for i in range(len(row)-1))
    is_decrementing = all(1 <= (row[i] - row[i+1]) <= 3 for i in range(len(row)-1))
    return is_incrementing or is_decrementing

# Function to attempt removing one failing number and rechecking
def check_row_with_removal(row):
    for i in range(len(row)):
        temp_row = row[:i] + row[i+1:]  # Create a new row without the i-th element
        if check_row(temp_row):
            return True, row[i]  # Return True and the removed number if the check passes
    return False, None  # Return False and None if no single removal can make the row pass
safe_count = 0

# Processing each row and printing results
for i, row in enumerate(rows):
    if check_row(row):
        safe_count += 1
        print(f"Row {i+1}: {row} (Safe)")
    else:
        passed, removed_number = check_row_with_removal(row)
        if passed:
            safe_count += 1
            removed_numbers.append(removed_number)
            print(f"Row {i+1}: {row} (Safe after removing {removed_number})")
        else:
            print(f"Row {i+1}: {row} (Not Safe)")

print(f"Safe Rows: {safe_count}")
if removed_numbers:
    print(f"Removed Numbers: {removed_numbers}")