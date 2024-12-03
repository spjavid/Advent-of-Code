from pprint import pprint

def find_load(file_path):
    with open(file_path, 'r') as file:
        grid = [list(line) for line in file]
    
    grid = tilt(grid)
    pprint(grid)

def tilt(grid):
    row = len(grid)
    col = len(grid[0])
    
    for i in range (row-1):
        for j in range (col):
            if grid[i][j] == 'O' and grid[i][j] != '#':
                grid[i][j] = 'O'
                grid[i+1][j] = '.'
    return grid
                
                


file_path = "C:\\Users\\sjavi\\OneDrive\\Documents\\Advent of Code\\2023\\Day 14\\Test.txt"       
find_load(file_path)
