def path(file_path):
    target = "ZZZ"
    start = "AAA"
    current = ""
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
    
    current = start
    
    test_number = 10000000
    
    for i in range(test_number):
        current_char = input[i % len(input)]
        if current_char == 'L':
            current = find_left(current,line_dict)
            count += 1
        elif current_char == 'R':
            current = find_right(current,line_dict)
            count += 1
        if target == current:
            break
            
        #print(f"Choice: {current_char}")
    print(f"{count}")

# Return the line number that begins with the string
def find_line(key,file):
    for line, lines in enumerate(file):
        if key in file:
            return line

# Find the left value in the pair on a given line
def find_left(key,file):
    index = file[key]
    return index[0]

# Fidn the right value in the pair on a given line
def find_right(key,file):
    index = file[key]
    return index[1]

file_path = "C:\\Users\\sjavi\\OneDrive\\Documents\\Advent of Code\\2023\\Day 8\\Day08.txt"       
path(file_path)