from pprint import pprint

def calculate_path(file_path):
    with open(file_path, 'r') as file:
        input = file.readlines()
    grid = [list(line) for line in input]
    
    for j in range(len(grid)):
        if all(grid[i][j] == grid[i - 1][j] for i in range(1, len(grid))):
            print("True")
            
    pprint(grid)

file_path = "C:\\Users\\sjavi\\OneDrive\\Documents\\Advent of Code\\2023\\Day 11\\Test.txt"       
calculate_path(file_path)