def winning_numbers_value(file_path):
    # Open the specified file in read mode
    with open(file_path, 'r') as file:
        # Read all lines from the file and store them in a list
        game_strings = file.readlines()
        # Initialize a dictionary to keep track of the number of cards for each game set
        line_counts = {index: 1 for index in range(len(game_strings))}
        # Call the function to calculate the total number of cards
        total_cards = get_card_numbers(game_strings, line_counts)

    # Return the total number of cards
    return total_cards

def get_card_numbers(game_strings, line_counts):
    # Initialize the total number of cards
    total_cards = 0
    
    # Iterate through each game set in the list of game strings
    for game_set, game in enumerate(game_strings):
        # Initialize the count of matches for the current game set
        matches = 0
        # Find the indices of the colon and pipe characters
        colon_index = game.index(":")
        pipe_index = game.index("|")

        # Directly convert the split strings to integers
        winning_numbers = list(map(int, game[colon_index + 1:pipe_index].strip().split()))
        card_numbers = list(map(int, game[pipe_index + 1:].strip().split()))

        # Check for matches between winning and card numbers
        for num in winning_numbers:
            if num in card_numbers:
                matches += 1

        # Update line counts for subsequent games based on the number of matches
        for card_increase in range(game_set + 1, game_set + matches + 1):
            line_counts[card_increase] += line_counts[game_set]

        # Update the total number of cards
        total_cards = sum(line_counts.values())

    # Return the total number of cards
    return total_cards

# Specify the file path
file_path = "C:\\Users\\sjavi\\OneDrive\\Documents\\Advent of Code\\2023\\Day 4\\Day04.txt"
# Call the winning_numbers_value function with the provided file path
total_cards = winning_numbers_value(file_path)
# Print the result
print(f"The number of cards is: {total_cards}")
