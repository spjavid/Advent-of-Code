import re  # Import the regular expressions module

def find_and_execute_functions(input_string):
    # Patterns to find 'do()', 'don't()', and 'mul()' with numbers
    do_pattern = re.compile(r'do\(\)')  # Pattern to match 'do()'
    dont_pattern = re.compile(r"don't\(\)")  # Pattern to match "don't()"
    mul_pattern = re.compile(r'mul\s*\(\s*(\d+)\s*,\s*(\d+)\s*\)')  # Pattern to match 'mul(x,y)' with numbers
    
    # Initial state: start as if there was a 'do()' at the beginning
    in_do_section = True  # Start in 'do()' section
    results = []  # List to store results of the multiplications
    
    # Current position in the string
    pos = 0  # Start at the beginning of the input string
    
    while pos < len(input_string):
        if in_do_section:
            # Find all 'mul' functions within the current 'do()' section
            mul_match = mul_pattern.search(input_string, pos)  # Search for 'mul' function
            # Continue processing 'mul' functions within the 'do()' section
            while mul_match and (dont_pattern.search(input_string, pos) is None or mul_match.start() < dont_pattern.search(input_string, pos).start()):
                x, y = map(int, mul_match.groups())  # Extract the integers and convert them to integers
                results.append(x * y)  # Multiply the numbers and store the result
                pos = mul_match.end()  # Update position to the end of the current 'mul' match
                mul_match = mul_pattern.search(input_string, pos)  # Search for the next 'mul' function
        
        # Update position and section state based on the next 'do()' or 'don't()'
        next_do = do_pattern.search(input_string, pos)  # Search for the next 'do()'
        next_dont = dont_pattern.search(input_string, pos)  # Search for the next "don't()"
        
        # Determine whether to enter 'do()' or exit to "don't()"
        if next_do and (not next_dont or next_do.start() < next_dont.start()):
            in_do_section = True  # Enter 'do()' section
            pos = next_do.end()  # Update position to the end of 'do()'
        elif next_dont and (not next_do or next_dont.start() < next_do.start()):
            in_do_section = False  # Exit to "don't()"
            pos = next_dont.end()  # Update position to the end of "don't()"
        else:
            break  # No more 'do()' or "don't()" patterns found, exit the loop

    return results  # Return the list of multiplication results

# Reading the input string from the file
filename = "C:\\Users\\sjavi\\OneDrive\\Documents\\Advent of Code\\2024\\Day 3\\input.txt"
with open(filename, 'r') as file:
    input_string = file.read()  # Read the entire content of the file into a string

# Find and execute the functions within 'do()' chunks
found_results = find_and_execute_functions(input_string)
total_sum = sum(found_results)  # Calculate the sum of all multiplication results

print("Individual results of the 'mul' functions:", found_results)
print("Sum of all results:", total_sum)
