from collections import defaultdict, deque

filename = "C:\\Users\\sjavi\\OneDrive\\Documents\\Advent of Code\\2024\\Day 5\\input.txt"

def read_file(filename):
    pairs = []
    sequences = []
    with open(filename, 'r') as file:
        lines = file.readlines()
        for line in lines:
            line = line.strip()
            if '|' in line:
                try:
                    a, b = map(int, line.split('|'))
                    pairs.append((a, b))
                except ValueError:
                    continue  # Skip lines that don't have valid pairs
            elif line:
                try:
                    sequences.append(list(map(int, line.split(','))))
                except ValueError:
                    continue  # Skip lines that don't have valid sequences
    return pairs, sequences

def build_graph(pairs):
    graph = defaultdict(list)
    in_degree = defaultdict(int)
    
    for a, b in pairs:
        graph[a].append(b)
        in_degree[b] += 1
        if a not in in_degree:
            in_degree[a] = 0
    
    return graph, in_degree

def topological_sort(graph, in_degree):
    queue = deque([node for node in in_degree if in_degree[node] == 0])
    order = []
    
    while queue:
        node = queue.popleft()
        order.append(node)
        
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    
    if len(order) != len(in_degree):
        raise ValueError("Graph has a cycle, no valid ordering exists")
    print(f"Order: {order}")
    
    return order

def is_valid_sequence(sequence, order):
    order_indices = {value: index for index, value in enumerate(order)}
    last_index = -1
    for num in sequence:
        if num in order_indices:
            if order_indices[num] < last_index:
                return False
            last_index = order_indices[num]
    return True

def validate_sequences(sequence, order):
    valid_sequences = []
    invalid_sequences = []
    if is_valid_sequence(sequence, order):
        valid_sequences.append(sequence)
    else:
        invalid_sequences.append(sequence)
    return valid_sequences, invalid_sequences

def calculate_midpoints(valid_sequences):
    running_total = 0
    for sequence in valid_sequences:
        n = len(sequence)
        running_total += (sequence[n//2])
    return running_total

def calculate_midpoints2(sequence):
    running_total = 0
    n = len(sequence)
    running_total += (sequence[n//2])
    return running_total

def filter_pairs(sequence, pairs):
    # Create a set from the sequence for O(1) lookups
    sequence_set = set(sequence)
    
    # Filter pairs based on the presence of both numbers in the sequence
    filtered_pairs = [(a, b) for a, b in pairs if a in sequence_set and b in sequence_set]
    
    return filtered_pairs

def flatten_list_of_lists(list_of_lists):
    """Flatten a list of lists into a single list."""
    return [item for sublist in list_of_lists for item in sublist]

def fix_sequence(sequence, order):
    order_indices = {value: index for index, value in enumerate(order)}
    valid_sequence = sorted(sequence, key=lambda x: order_indices[x])
    return valid_sequence

pairs, sequences = read_file(filename)

def main(pairs, sequences):
    answer = 0
    answer2 = 0
    for sequence in sequences:
        graph, in_degree = build_graph(filter_pairs(sequence,pairs))
        order = topological_sort(graph, in_degree)
        valid_sequences, invalid_sequences = validate_sequences(sequence, order)
        if len(invalid_sequences) > 0:
            flattened_sequence = flatten_list_of_lists(invalid_sequences)
            fixed_sequence = fix_sequence(flattened_sequence,order)
            answer2 += calculate_midpoints2(fixed_sequence)
        answer += calculate_midpoints(valid_sequences)
    print(f"Valid Sequence Total: {answer}")
    print(f"Invalid Sequence Total After Fixing: {answer2}")

main(pairs,sequences)
