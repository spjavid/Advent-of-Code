
# Reading the input string from the file
filename = "C:\\Users\\sjavi\\OneDrive\\Documents\\Advent of Code\\2024\\Day 4\\input.txt"

def read_grid_from_file(filename):
    with open(filename, 'r') as file:
        return [line.strip() for line in file]

def search_word_in_grid(grid, word):
    rows = len(grid)
    cols = len(grid[0])
    word_length = len(word)
    found_positions = []

    # Define the 8 possible directions
    directions = [
        (0, 1),  # Horizontal right
        (0, -1), # Horizontal left
        (1, 0),  # Vertical down
        (-1, 0), # Vertical up
        (1, 1),  # Diagonal down-right
        (-1, -1),# Diagonal up-left
        (1, -1), # Diagonal down-left
        (-1, 1)  # Diagonal up-right
    ]

    def search_from_position(row, col, direction):
        for i in range(word_length):
            new_row = row + i * direction[0]
            new_col = col + i * direction[1]
            if new_row < 0 or new_row >= rows or new_col < 0 or new_col >= cols:
                return False
            if grid[new_row][new_col] != word[i]:
                return False
        return True

    for row in range(rows):
        for col in range(cols):
            for direction in directions:
                if search_from_position(row, col, direction):
                    found_positions.append((row, col, direction))

    return found_positions

# Word to find
word = "XMAS"

grid = read_grid_from_file(filename)

# Search for the word in the grid
positions = search_word_in_grid(grid, word)

count = 0
# Print the results
for pos in positions:
    row, col, direction = pos
    count += 1
    print(f"Found '{word}' starting at (row={row}, col={col}) in direction {direction}")

print(f"Total count: {count}")
