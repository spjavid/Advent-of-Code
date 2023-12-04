def sum_numbers_adjacent_to_symbols(lines):
    # Convert lines into a grid of characters
    grid = [list(line) for line in lines]

    # Initialize total sum and set of visited positions
    total_sum = 0
    visited_positions = set()

    # Function to check if a position is valid
    def is_valid_position(row, col):
        return 0 <= row < len(grid) and 0 <= col < len(grid[row])

    def check_diagonals(row, col):
        for i in range(-1, 2):
            for j in range(-1, 2):
                new_row, new_col = row + i, col + j
                if (
                    is_valid_position(new_row, new_col) and
                    not grid[new_row][new_col].isdigit() and
                    grid[new_row][new_col] != '.'
                ):
                    return True
        return False
                    
    # Function to explore connected numbers starting from a given position
    def explore_connected_numbers(start_row, start_col):
        connected_sum = 0
        stack = [(start_row, start_col)]
        adjacent = False

        while stack:
            current_row, current_col = stack.pop()
            if (current_row, current_col) not in visited_positions:
                visited_positions.add((current_row, current_col))
                char = grid[current_row][current_col]

                if char.isdigit():
                    connected_sum = connected_sum * 10 + int(char)
                    for i in range(-1, 2):
                        for j in range(-1, 2):
                            new_row, new_col = current_row + i, current_col + j
                            if (
                                is_valid_position(new_row, new_col) and
                                grid[new_row][new_col].isdigit() and
                                grid[new_row][new_col] != '.'
                            ):
                                stack.append((new_row, new_col))
                            adjacent = adjacent or check_diagonals(new_row,new_col)
        if adjacent:
            return connected_sum
        return 0

    # Iterate through the grid to find symbols and numbers
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] != '.' and (row, col) not in visited_positions:
                total_sum += explore_connected_numbers(row, col)

    return total_sum

# Read lines from the input text file
with open("Day03.txt", "r") as file:
    input_lines = file.readlines()

# Calculate and print the result
result_sum = sum_numbers_adjacent_to_symbols(input_lines)
print("Sum of numbers adjacent to symbols (excluding '.' symbols):", result_sum)
