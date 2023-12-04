def winning_numbers_value (file_path):
    # Open the specified file in read mode
    with open(file_path, 'r') as file:
        # Read all lines from the file and store them in a list
        game_strings = file.readlines()
        
        total_score = get_card_numbers(game_strings)
        
        
    return  total_score

def get_card_numbers(game_strings):
    total_points = 0
    for game_string in game_strings:
        score = 0
        colon_index = game_string.index(":")
        bar_index = game_string.index("|")
        
        set1_string = game_string[colon_index + 1:bar_index].strip()
        set2_string = game_string[bar_index + 1:].strip()
        
        winning_numbers = list(map(int, set1_string.split()))
        card_numbers = list(map(int, set2_string.split()))
        
        #print("Winning Numbers:", winning_numbers)
        #print("Card Numbers:", card_numbers)
        for num in winning_numbers:
                if num in card_numbers:
                    # Double the score for each occurrence
                    if score == 0:
                        score = 1
                    elif score >=1:
                        score *= 2 
                else:
                    # Set the score to 1 for the first occurrence
                    continue
        
        occurrences_count = {num: card_numbers.count(num) for num in winning_numbers}

        print("Occurrences Count:", occurrences_count)
        print(f"{score}")
        total_points = total_points + score
        
    return total_points
    
        


file_path = "C:\\Users\\sjavi\\OneDrive\\Documents\\Advent of Code\\2023\\Day 4\\Day04.txt"

# Call the sum_game_numbers_from_file function with the provided file path
total_points = winning_numbers_value(file_path)

# Print the result
print(f"The total points is: {total_points}")