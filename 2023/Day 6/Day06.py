def find_race_record(file_path):
    paired_numbers = []
    
    with open(file_path, 'r') as file:
        race_info = file.readlines()
        
        for line in race_info:
            numbers = extract_numbers(line)
            paired_numbers.append(numbers)

    paired_numbers = list(zip(*paired_numbers))

    win_count = [0] * len(paired_numbers)
    for race_pairs, races in enumerate(paired_numbers):
        wins = 0
        race_distance = races[1]
        max_race_time = races[0]
        race_time   = max_race_time - 1

        while race_time > 0:
            distance = race_time * (max_race_time-race_time)
            race_time -= 1
            if distance > race_distance:
                wins += 1
        win_count[race_pairs] = wins

    
    total = 1
    for value in win_count:
        total = total * value
    print(f"{total}")
    


def extract_numbers(line):
        return [int(num) for num in line.split() if num.isdigit()]
        
file_path = "C:\\Users\\sjavi\\OneDrive\\Documents\\Advent of Code\\2023\\Day 6\\Day06.txt"       
find_race_record(file_path)

