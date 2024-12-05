from collections import defaultdict

def parse_input(input_data):
    # Split input into rules and updates
    rules_section, updates_section = input_data.strip().split("\n\n")
    
    # Parse the rules
    rules = []
    for line in rules_section.splitlines():
        x, y = map(int, line.split('|'))
        rules.append((x, y))
    
    # Parse the updates
    updates = []
    for line in updates_section.splitlines():
        updates.append(list(map(int, line.split(','))))
    
    return rules, updates

def is_valid_order(update, rules):
    # Create a dictionary to store the dependency constraints for each page
    dependencies = defaultdict(set)
    for x, y in rules:
        dependencies[y].add(x)
    
    for i in range(len(update)):
        for j in range(i + 1, len(update)):
            if update[j] in dependencies[update[i]]:
                return False
    return True

def find_middle_page(update):
    # Find the middle page of the correctly ordered update
    n = len(update)
    return update[(n - 1) // 2]

def solve(input_data):
    rules, updates = parse_input(input_data)
    total_sum = 0
    
    # Process each update
    for update in updates:
        if is_valid_order(update, rules):
            middle_page = find_middle_page(update)
            total_sum += middle_page
    
    return total_sum

def read_input_from_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()

file_path = 'day5_input.txt'  # Replace this with the actual path to your file
input_data = read_input_from_file(file_path)

print(solve(input_data))
