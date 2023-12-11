def calculate_next(file_path):
    grand_total = 0
    with open(file_path, 'r') as file:
        input = file.readlines()
            
    for line, lines in enumerate(input):
        grand_total += find_value(lines)
    print(f"{grand_total}")
    return 0

def find_value(input):
    values = [int(token) for token in input.split()]
    values = Reverse(values)
    print(f"{values}")
    total = values[len(values)-1]
    
    while not all(val == 0 for val in values):
        values = find_differences(values)
        print(f"{values}")
        total += values[len(values)-1]
    #print(f"{total}")
    return total
      
def find_differences(input):
    overlapping_pairs = [(input[i], input[i + 1]) for i in range(len(input) - 1)]    
    differences = [b - a for a, b in overlapping_pairs]
    return differences

def Reverse(lst):
   new_lst = lst[::-1]
   return new_lst

file_path = "C:\\Users\\sjavi\\OneDrive\\Documents\\Advent of Code\\2023\\Day 9\\Day09.txt"       
calculate_next(file_path)