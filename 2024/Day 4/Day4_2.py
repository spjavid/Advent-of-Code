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
    
    a_positions = {}

    for start_row, start_col, direction in found_positions:
        # Calculate the position of 'A' (second letter) in the "MAS" pattern
        a_row = start_row + direction[0]
        a_col = start_col + direction[1]

        # Store the direction of each 'A' point for intersection checking
        if (a_row, a_col) not in a_positions:
            a_positions[(a_row, a_col)] = []
        a_positions[(a_row, a_col)].append((start_row, start_col, direction))

    # Find intersecting 'A' points
    intersecting_patterns = []

    for a_pos, mas_patterns in a_positions.items():
        if len(mas_patterns) > 1:
            for pattern in mas_patterns:
                intersecting_patterns.append(pattern)

    print(f"{len(intersecting_patterns)}")

    return intersecting_patterns

def create_found_grid(grid, word_positions, word):
    found_grid = [[' ' for _ in range(len(grid[0]))] for _ in range(len(grid))]
    a_count = 0
    
    # Mark found word positions
    for row, col, direction in word_positions:
        for i in range(len(word)):
            new_row = row + i * direction[0]
            new_col = col + i * direction[1]
            found_grid[new_row][new_col] = grid[new_row][new_col]
            if(found_grid[new_row][new_col] == 'A'):
                a_count += .5
    print(f"Total As: {a_count}")
    return found_grid


def print_grid(grid):
    for row in grid:
        print(''.join(row))

grid = read_grid_from_file(filename)
word = "MAS"

# Search for the word in the grid
positions = search_word_in_grid(grid, word)

count = 0
# Print the results
for pos in positions:
    row, col, direction = pos
    count += 1
    #print(f"Found '{word}' starting at (row={row}, col={col}) in direction {direction}")

print(f"Total count: {count}")

# Create and print the grid with found words
found_grid = create_found_grid(grid, positions, word)
#print("Grid with found 'MAS' words:")
#print_grid(found_grid)
