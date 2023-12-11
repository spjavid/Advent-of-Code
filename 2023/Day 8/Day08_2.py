import math

def path(file_path):
    target = "Z"
    start = "AAA"
    current = ''
    count = 0
    line_dict = {}
    
    
    with open(file_path, 'r') as file:
        input = file.readline().strip()
        data = file.readlines()
    
    for line in data[1:]:
        key, value = line.split('=')
        key = key.strip()
        value = tuple(part.strip() for part in value.strip()[1:-1].split(','))  # Extract characters on each side of the comma
        line_dict[key] = value
    
    all_starts = find_starts(line_dict)
    ends_in_z = [0] * len(all_starts)
    
    current = get_keys_at_line_numbers(line_dict,all_starts)
    i = 0
    while not all(ends_in_z):
        for line, start in enumerate(current):
            current_char = input[i % len(input)]
            if current_char == 'L':
                current[line] = find_left(current[line],line_dict)
            elif current_char == 'R':
                current[line] = find_right(current[line],line_dict)
            #print(f"{current[line]}")
            if str(current[line]).endswith('Z'):
                ends_in_z[line] = i+1
        i += 1
       

    print(f"{math.lcm(*ends_in_z)}")
    #print(f"{i}")

# Return the line number that begins with the string
def find_line(key,file):
    for line, lines in enumerate(file):
        if key in file:
            return line
        
def find_starts(file):
    starting_lines = []
    for line, lines in enumerate(file):
        if lines[-1] == 'A':
            print(f"Starting point at: {line}")
            starting_lines.append(line)
    return starting_lines

# Find the left value in the pair on a given line
def find_left(key,file):
    index = file[key]
    return index[0]

# Fidn the right value in the pair on a given line
def find_right(key,file):
    index = file[key]
    return index[1]

def get_keys_at_line_numbers(my_dict, line_numbers):
    keys_at_line_numbers = [list(my_dict.keys())[line_num] for line_num in line_numbers if 0 <= line_num < len(my_dict)]
    return keys_at_line_numbers

file_path = "C:\\Users\\sjavi\\OneDrive\\Documents\\Advent of Code\\2023\\Day 8\\Day08.txt"       
path(file_path)