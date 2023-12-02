import regex as re

def get_first_and_last_number(line):
    word_to_digit = {
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9'
    }

    # Use regular expression to find all digits and number words in the line with overlap
    number_matches = re.findall(r'\d+|' + '|'.join(word_to_digit.keys()), line, flags=re.IGNORECASE | re.DOTALL, overlapped=True)

    first_number = None
    last_number = None

    for match in number_matches:
        # Convert word representations to numeric form
        numeric_number = word_to_digit.get(match.lower(), match)

        # Update the first number for each number encountered (consider the first numeric occurrence)
        if first_number is None and numeric_number.isdigit():
            first_number = numeric_number

        # Update the last number for each number encountered
        last_number = numeric_number

    # If there is no numeric number, consider the first word representation as the last number
    if last_number is None and word_to_digit.get(number_matches[-1].lower()):
        last_number = word_to_digit[number_matches[-1].lower()]

    # Return the pair of first and last numeric numbers
    return int(first_number), int(last_number)

def main():
    running_sum = 0

    # Open the file "Day01.txt" for reading
    with open("Day01.txt", "r") as file:
        # Read the file line by line
        for line in file:
            # Get the pair of first and last numbers for each line
            result = get_first_and_last_number(line)

            # Ensure the appended number is never more than two digits
            appended_number = int(str(result[0])[:1] + str(result[1])[-1])
            running_sum += appended_number

            # Print the result for each line
            print(f"Line: {line.strip()}, Appended Number: {appended_number}")

    # Print the final result: Running Sum of Appended Numbers
    print(f"\nRunning Sum of Appended Numbers: {running_sum}")

if __name__ == "__main__":
    main()
