def find_lowest_location (file_path):
    sections = ["seed-to-soil map:",
                "soil-to-fertilizer map:",
                "fertilizer-to-water map:",
                "water-to-light map:",
                "light-to-temperature map:",
                "temperature-to-humidity map:",
                "humidity-to-location map:"
    ]
    
    seeds = get_seeds(file_path)
    seeds = expand_seed(seeds)
    # for example, take 929142010 and add 467769747 to it, then you have your min and max
    # find the overlap between that range and the map that you're comparing it too
    # only do calculations on the overlap, otherwise just keep the regular number
    # do one 'range' at a time instead of all of them
    lowest_location = 0
    
#    for section_name in sections:
#        section = return_section_map(file_path, section_name)
#        seeds = mapping(seeds,section)
    
#    lowest_location = min(seeds)
    print(f"{lowest_location}")
    return  lowest_location

def expand_seed(seeds):
    expand_seed =[]
    if len(seeds) % 2 == 0:
        # Create pairs by iterating through the list with a step of 2
        pairs = [(seeds[i], seeds[i + 1]) for i in range(0, len(seeds), 2)]

        # Modify the original list based on the pairs
        #for start, extension in pairs:
            # Extend the list with the specified number of values
        #    expand_seed.extend(range(start, start + extension))
        print(f"{pairs}")
    return expand_seed

def return_section_map(file_path,section):
    start = False
    start_line = 0
    end_line = 0
    with open(file_path, 'r') as file:
        input = file.readlines()
        
        for line_number, line in enumerate(input):
            if section in line:
                start = True
                start_line = line_number
                #print(f"The section start is at {line_number}")
            if start == True and line == '\n':
                end_line = line_number
                #print(f"End found at {line_number}")
                break
            
        filtered_lines = input[start_line+1:end_line]
        
        section_map = []
        
        for line_number, line in enumerate(filtered_lines):
            numbers = [int(num) for num in line.strip().split()]
            section_map.append(numbers)
    
    return section_map

def mapping(seeds, section):
    output = []
    
    for seed_number, current_seed in enumerate(seeds):
        value = current_seed
        for row in section:
            if current_seed >= row[1] and current_seed <= (row[1] + row[2]):
                if row[0] < row[1]:
                    value = current_seed - abs(row[0]-row[1])
                else:
                    value = current_seed + abs(row[1]-row[0])
                output.append(value)
                break  # No need to check further rows if the seed is found in one row
        else:
            # If the seed doesn't fall into any range, append the original seed value
            output.append(current_seed)

    return output

# Assuming Seeds are found on first line, returns a the list of seeds.
def get_seeds(file_path):
    with open(file_path, 'r') as file:
        seed_str = file.readline().strip().split(':')
        seed_str = seed_str[1].strip().split(' ')
        seeds = [int(seed) for seed in seed_str]
    return seeds

file_path = "C:\\Users\\sjavi\\OneDrive\\Documents\\Advent of Code\\2023\\Day 5\\Day05.txt"

# Call the sum_game_numbers_from_file function with the provided file path
find_lowest_location(file_path)