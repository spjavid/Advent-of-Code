from functools import cache
def picross(file_path):
    with open(file_path, 'r') as file:
        lines = [x.split() for x in file.read().splitlines()]
    
    total_arrangements = {}
    
    for line, (lava, springs) in enumerate(lines):
        numbers = tuple(map(int, springs.split(",")))
        extended_lava = "?".join([lava]*5)
        extended_springs = numbers * 5
        total_arrangements[line] = recurse(extended_lava,extended_springs)
    

    print(sum(x for x in total_arrangements.values()))

from functools import cache

@cache
def recurse(lava, springs, result=0):
    # Base case: If there are no more springs to place, check if '#' is not in the remaining lava.
    if not springs:
        return '#' not in lava

    # Extract the current spring position and update the remaining springs.
    current, springs = springs[0], springs[1:]

    # Iterate over possible starting positions for the next spring.
    for i in range(len(lava) - sum(springs) - len(springs) - current + 1):
        # Check if there is a '#' in the substring before the potential starting position.
        if "#" in lava[:i]:
            break

        # Calculate the next position for the spring.
        next_position = i + current

        # Check conditions for a valid next position.
        if next_position <= len(lava) and \
           '.' not in lava[i : next_position] and \
           lava[next_position : next_position + 1] != "#":

            # Recursively explore the next state with the updated lava and remaining springs.
            result += recurse(lava[next_position + 1:], springs)

    return result

        
file_path = "C:\\Users\\sjavi\\OneDrive\\Documents\\Advent of Code\\2023\\Day 12\\Day12.txt"       
picross(file_path)