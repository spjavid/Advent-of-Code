import re

# Function to find, extract, and multiply all occurrences of the function
def find_and_execute_functions(input_string, function_name):
    # Create a regex pattern to find the specific function with numbers as arguments
    pattern = re.compile(re.escape(function_name) + r'\s*\(\s*(\d+)\s*,\s*(\d+)\s*\)')
    
    # Find all occurrences of the function and extract arguments
    matches = pattern.findall(input_string)
    
    results = []
    for match in matches:
        x, y = map(int, match)  # Extract the integers and convert them to integers
        result = x * y
        results.append(result)
    
    return results

# Reading the input string from the file
filename = "C:\\Users\\sjavi\\OneDrive\\Documents\\Advent of Code\\2024\\Day 3\\input.txt"
with open(filename, 'r') as file:
    input_string = file.read()

# Function name to search for
function_name = "mul"

# Find and execute the functions
found_results = find_and_execute_functions(input_string, function_name)
total_sum = sum(found_results)

print("Individual results of the 'mul' functions:", found_results)
print("Sum of all results:", total_sum)
