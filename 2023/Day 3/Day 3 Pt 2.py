def calculate_sum_of_products_adjacent_to_star(lines):
    grid = [list(line) for line in lines]

    def is_valid_position(row, col):
        return 0 <= row < len(grid) and 0 <= col < len(grid[row])

    def get_adjacent_numbers(row, col):
        numbers = []
        for i in range(-1, 2):
            for j in range(-1, 2):
                new_row, new_col = row + i, col + j
                if (
                    is_valid_position(new_row, new_col) and
                    grid[new_row][new_col].isdigit()
                ):
                    numbers.append(int(grid[new_row][new_col]))
                    # Mark the position as visited
                    grid[new_row][new_col] = '.'
        return numbers

    total_sum = 0

    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] == '*':
                numbers = get_adjacent_numbers(row, col)
                if len(numbers) > 1:  # Ensure there are at least two adjacent numbers
                    product = 1
                    for num in numbers:
                        product *= num
                        print(f"{product}")
                    total_sum += product

    return total_sum

# Provided input
lines = [
    "467..114..",
    "...*......",
    "..35..633.",
    "......#...",
    "617*......",
    ".....+.58.",
    "..592.....",
    "......755.",
    "...$.*....",
    ".664.598..",
]

# Calculate and print the total sum of products adjacent to '*'
result_sum = calculate_sum_of_products_adjacent_to_star(lines)
print("Total sum of products adjacent to '*' in the given input:", result_sum)
