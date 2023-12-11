import math
def calculate_path(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    grid = expand_grid(lines)
    coordinates = find_coords(grid)
    total_distance = find_dist(coordinates)
    print(f"Total distance for all possible pairs: {total_distance}")

def expand_grid(grid):

    grid = [list(line.rstrip().strip()) for line in grid]

    columns_to_duplicate = [j for j in range(len(grid[0])) if all(grid[i][j] == grid[i - 1][j] for i in range(1, len(grid)))]

    rows_to_duplicate = [i for i in range(1, len(grid)) if all(value == '.' for value in grid[i])]

    new_grid = [row.copy() for row in grid]
    for i in reversed(rows_to_duplicate):
        new_grid.insert(i + 1, ['.'] * len(new_grid[0]))

    for row in new_grid:
        for j in reversed(columns_to_duplicate):
            row.insert(j + 1, '.')
    return new_grid

def find_coords(grid):
    points = {}
    iterator = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "#":
                grid[i][j] = iterator
                points[iterator] = (i+1,j+1)
                iterator += 1
    return points
                
def find_dist(coordinates):
    total_distance = 0
    num_coordinates = len(coordinates)

    for i in range(num_coordinates):
        for j in range(i + 1, num_coordinates):
            Px, Py = coordinates[i]
            Qx, Qy = coordinates[j]
            distance = abs(Px - Qx) + abs(Py - Qy)
            total_distance += distance
            print(f"Distance between points {i} and {j}: {distance}")

    return total_distance

file_path = "C:\\Users\\sjavi\\OneDrive\\Documents\\Advent of Code\\2023\\Day 11\\Test.txt"       
calculate_path(file_path)
