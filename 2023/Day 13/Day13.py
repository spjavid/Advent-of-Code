import numpy as np

def process_grid(grid):
    #grid_array = np.array([[1 if cell == '#' else 0 for cell in row] for row in grid])
    grid_array = np.array(grid)
    reflection_row, reflection_col = find_mirror(grid_array)
    
    print(f"Reflection point is at: Row {reflection_row}")
    print(f"Reflection point is at: Col {reflection_col}")
    
    col_calc = len(grid[0])-reflection_row
    row_calc = len(grid)-reflection_col

    print(grid_array)
    print('\n')

    return 0  # calculation not used

def find_mirror(grid_array):
    rows, cols = grid_array.shape

    # Check for vertical mirrors (column mirrors)
    for col in range(1, cols):
        left_side = grid_array[:, :col]
        right_side = np.fliplr(grid_array[:, col:])

        # Ensure the shorter side is padded with '.' to match the longer side
        min_len = min(left_side.shape[1], right_side.shape[1])
        left_side_padded = np.pad(left_side[:, :min_len], ((0, 0), (0, abs(left_side.shape[1] - min_len))), constant_values='.')
        right_side_padded = np.pad(right_side[:, :min_len], ((0, 0), (0, abs(right_side.shape[1] - min_len))), constant_values='.')

        if np.array_equal(left_side_padded, right_side_padded):
            return 0, col

    # Check for horizontal mirrors (row mirrors)
    for row in range(1, rows):
        upper_side = grid_array[:row, :]
        lower_side = np.flipud(grid_array[row:, :])

        # Ensure the shorter side is padded with '.' to match the longer side
        min_len = min(upper_side.shape[0], lower_side.shape[0])
        upper_side_padded = np.pad(upper_side[:min_len, :], ((0, abs(upper_side.shape[0] - min_len)), (0, 0)), constant_values='.')
        lower_side_padded = np.pad(lower_side[:min_len, :], ((0, abs(lower_side.shape[0] - min_len)), (0, 0)), constant_values='.')

        if np.array_equal(upper_side_padded, lower_side_padded):
            return row,0

    return 0,0

def read_and_process_file(file_path):
    current_grid = []
    all_grids = []
    total = 0

    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()

            if not line:
                if current_grid:
                    all_grids.append(current_grid)
                    total += process_grid(current_grid)
                    current_grid = []

            else:
                current_grid.append(list(line))

    if current_grid:
        all_grids.append(current_grid)
        total += process_grid(current_grid)

    return all_grids

# Example usage:
file_path = "C:\\Users\\sjavi\\OneDrive\\Documents\\Advent of Code\\2023\\Day 13\\Test.txt"
all_grids = read_and_process_file(file_path)
