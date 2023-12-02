# Assigning values to variables representing the counts of different colors
number_red = 12
number_green = 13
number_blue = 14

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

            print(f"Color counts for part {part_number} of 'Game {game_number}': {color_counts}")

            # Compare color counts to predefined values
            if ('red' in color_counts and color_counts['red'] > number_red) \
                    or ('green' in color_counts and color_counts['green'] > number_green) \
                    or ('blue' in color_counts and color_counts['blue'] > number_blue):
                print(f"Game {game_number} is invalid. Reading next game.")
                valid_game = False  # Mark the entire game as invalid
                break  # Exit the loop for processing parts in this game if an invalid part is found
            else:
                # Valid part, continue processing the next part
                continue

        # Add the game number to the total sum if the entire game is valid
        if valid_game:
            print(f"All parts of game {game_number} are valid. Adding {game_number} to {total_sum}.")
            total_sum += game_number

    # Return the calculated total sum of game numbers
    return total_sum

# Example usage:
# Specify the file path to the input text file containing game strings
file_path = 'Day02.txt'

# Call the sum_game_numbers_from_file function with the provided file path
total_game_numbers = sum_game_numbers_from_file(file_path)

# Print the result
print(f"The sum of Game Numbers is: {total_game_numbers}")
