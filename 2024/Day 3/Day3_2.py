import re

def find_and_execute_functions(input_string):
    # Patterns to find 'do()', 'don't()', and 'mul()' with numbers
    do_pattern = re.compile(r'do\(\)')
    dont_pattern = re.compile(r"don't\(\)")
    mul_pattern = re.compile(r'mul\s*\(\s*(\d+)\s*,\s*(\d+)\s*\)')
    
    # Initial state: start as if there was a 'do()' at the beginning
    in_do_section = True
    results = []
    pos = 0
    
    while pos < len(input_string):
        # Check for 'do()' or 'don't()' before processing 'mul' functions
        do_match = do_pattern.search(input_string, pos)
        dont_match = dont_pattern.search(input_string, pos)
        
        # Determine the next transition point
        if do_match and (not dont_match or do_match.start() < dont_match.start()):
            if in_do_section:
                # Process all 'mul' functions before this 'do()'
                while True:
                    mul_match = mul_pattern.search(input_string, pos, do_match.start())
                    if mul_match:
                        x, y = map(int, mul_match.groups())
                        result = x * y
                        results.append(result)
                        pos = mul_match.end()
                    else:
                        break
            in_do_section = True
            pos = do_match.end()
        elif dont_match and (not do_match or dont_match.start() < do_match.start()):
            if in_do_section:
                # Process all 'mul' functions before this 'don't()'
                while True:
                    mul_match = mul_pattern.search(input_string, pos, dont_match.start())
                    if mul_match:
                        x, y = map(int, mul_match.groups())
                        result = x * y
                        results.append(result)
                        pos = mul_match.end()
                    else:
                        break
            in_do_section = False
            pos = dont_match.end()
        else:
            if in_do_section:
                # Process all remaining 'mul' functions at the end of the string
                while True:
                    mul_match = mul_pattern.search(input_string, pos)
                    if mul_match:
                        x, y = map(int, mul_match.groups())
                        result = x * y
                        results.append(result)
                        pos = mul_match.end()
                    else:
                        break
            break
    
    return results

# Reading the input string from the file
filename = "C:\\Users\\sjavi\\OneDrive\\Documents\\Advent of Code\\2024\\Day 3\\input.txt"
with open(filename, 'r') as file:
    input_string = file.read()

# Find and execute the functions within 'do()' chunks
found_results = find_and_execute_functions(input_string)
total_sum = sum(found_results)

print("Individual results of the 'mul' functions:", found_results)
print("Sum of all results:", total_sum)
