import numpy as np

file_path = "C:\\Users\\sjavi\\OneDrive\\Documents\\Advent of Code\\2024\\Day 1\\input.txt"       

data = np.loadtxt(file_path)

column1 = data[:, 0] 
column2 = data[:, 1]

sorted_column1 = np.sort(column1)
sorted_column2 = np.sort(column2)

def function():
    running_total = 0
    # print("Sorted Column 1:", sorted_column1)
    # print("Sorted Column 2:", sorted_column2)

    for i in range(len(sorted_column1)):
        difference = abs(sorted_column1[i] - sorted_column2[i])
        running_total += difference 
        # print(f"Difference at position {i}: {difference}, Running Total: {running_total}")

    # print("Final Running Total of Differences:", running_total)

    # Counting occurrences in Column 2
    count_dict = {}
    for number in sorted_column2:
        if number in count_dict:
            count_dict[number] += 1
        else:
            count_dict[number] = 1

    # Printing the occurrences
    print("Occurrences in Column 2:")
    for number, count in count_dict.items():
        print(f"{number}: {count}")

    # Initialize a new running total for the product sum
    running_total_product = 0

    # Iterating through Column 1, multiplying by the count in Column 2, and updating the running total
    for number in sorted_column1:
        if number in count_dict:
            product = number * count_dict[number]
            running_total_product += product
            print(f"{number} * {count_dict[number]} = {product}, Running Total: {running_total_product}")

    print("Final Running Total of Products:", running_total_product)


function()