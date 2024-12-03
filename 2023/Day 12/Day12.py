from itertools import product
import re

def picross(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    
    total_arrangements = 0
    
    for line in lines:
        numbers = re.findall(r'\d+', line)
        numbers = [int(value) for value in numbers]
        symbols = [char for char in line.strip() if not char.isdigit()]
        total_arrangements += count_iterations(numbers, symbols)
    
    print(f"{total_arrangements}")

def generate_combinations(input_string):
    question_mark_indices = [i for i, char in enumerate(input_string) if char == '?']
    combinations = []

    for binary_combination in product("01", repeat=len(question_mark_indices)):
        temp_string = list(input_string)
        for index, value in zip(question_mark_indices, binary_combination):
            temp_string[index] = '#' if value == '1' else '.'
        combinations.append("".join(temp_string))
    return combinations

def count_groups(input_string):
    counts = []
    current_count = 0

    for char in input_string:
        if char == '#':
            current_count += 1
        elif current_count > 0:
            counts.append(current_count)
            current_count = 0

    if current_count > 0:
        counts.append(current_count)
    return counts

def count_iterations(numbers,symbols):
    count = 0
    combinations = generate_combinations(symbols)
    for combination in combinations:
        comparison = count_groups(combination)
        if comparison == numbers:
            print(combination)
            count += 1
    print(count) 
    return count
    
        
file_path = "C:\\Users\\sjavi\\OneDrive\\Documents\\Advent of Code\\2023\\Day 12\\Test.txt"       
picross(file_path)