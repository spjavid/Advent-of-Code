import sys
# Redirect standard output to "Output.txt"
sys.stdout = open("Output.txt", "w")

def sum_numbers_adjacent_to_symbols(lines):
    grid = [list(line) for line in lines]

    total_sum = 0
    visited_positions = set()

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
                    with open("Output.txt", "a") as output_file:
                        print(f"({grid[new_row][new_col]},", end='', file=output_file, flush=True)
                    return True
        return False

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
                    adjacent = adjacent or check_diagonals(current_row, current_col)
                    if (
                        is_valid_position(current_row, current_col+1) and
                        grid[current_row][current_col+1].isdigit() and
                        grid[current_row][current_col+1] != '.'
                    ):
                        stack.append((current_row, current_col+1))
                    
        if adjacent:
            with open("Output.txt", "a") as output_file:
                print(f"{connected_sum})", file=output_file, flush=True)
            return connected_sum
        return 0

    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] != '.' and (row, col) not in visited_positions:
                total_sum += explore_connected_numbers(row, col)

    return total_sum


with open("C:\\Users\\sjavi\\OneDrive\\Documents\\Advent of Code\\2023\\Day 3\\Day03_2.txt", "r") as file:
    input_lines = file.readlines()

# Calculate and print the result
result_sum = sum_numbers_adjacent_to_symbols(input_lines)
print("Sum of numbers adjacent to symbols (excluding '.' symbols):", result_sum)

# Close the file and restore standard output
sys.stdout.close()
sys.stdout = sys.__stdout__
