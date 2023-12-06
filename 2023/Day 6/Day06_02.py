def find_race_record(file_path):
    paired_numbers = []
    
    with open(file_path, 'r') as file:
        race_info = file.readlines()
        
        for line in race_info:
            numbers = extract_numbers(line)
            paired_numbers.append(numbers)

    #paired_numbers = list(zip(*paired_numbers))

    win_count = [0] * len(paired_numbers)

    wins = 0
    race_distance = paired_numbers[1]
    max_race_time = paired_numbers[0]
    race_time   = max_race_time - 1

    while race_time > 0:
        distance = race_time * (max_race_time-race_time)
        race_time -= 1
        if distance > race_distance:
            wins += 1

    print(f"{wins}")
    


def extract_numbers(line):
    numbers =  [int(num) for num in line.split() if num.isdigit()]
    combined_number = int(''.join(map(str,numbers)))
    return combined_number
        
file_path = "C:\\Users\\sjavi\\OneDrive\\Documents\\Advent of Code\\2023\\Day 6\\Day06.txt"       
find_race_record(file_path)

