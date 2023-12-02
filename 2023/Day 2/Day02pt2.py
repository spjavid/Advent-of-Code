
# Function to calculate the sum of game numbers from a given file
def sum_game_numbers_from_file(file_path):
    # Open the specified file in read mode
    with open(file_path, 'r') as file:
        # Read all lines from the file and store them in a list
        game_strings = file.readlines()

    # Initialize a variable to store the total sum of game numbers
    total_sum = 0

    
# Iterate through each game string in the list
    for game_string in game_strings:
        min_red, min_blue, min_green = 0,0,0
        # Extract the game number from the string and convert it to an integer
        game_number = int(game_string.split(':')[0].split()[-1])
        game_pulls = str(game_string.split(':')[1])
        game_set = game_pulls.split(';')

        valid_game = True  # Flag to track the validity of the entire game

        for part_number, part in enumerate(game_set, start=1):
            color_counts = {}
            color_items = part.split(',')

            for color_item in color_items:
                count, color = color_item.strip().split()
                count = int(count)
                color_counts[color] = count

                min_red = max(min_red, color_counts.get('red', 0))
                min_green = max(min_green, color_counts.get('green', 0))
                min_blue = max(min_blue, color_counts.get('blue', 0))

        total_sum += ((min_blue)*(min_green)*(min_red))


    # Return the calculated total sum of game numbers
    return total_sum

# Example usage:
# Specify the file path to the input text file containing game strings
file_path = 'Day02.txt'

# Call the sum_game_numbers_from_file function with the provided file path
total_game_numbers = sum_game_numbers_from_file(file_path)

# Print the result
print(f"The sum of Game Numbers is: {total_game_numbers}")
