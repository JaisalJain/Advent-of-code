# Input lists 
left_list = []
right_list = []

# Opening input.txt and splitting left and right lists
with open('day1_input.txt', 'r') as locations:
    for lines in locations:
        split_lines = lines.replace('\n', "").split()  
        left_list.append(int(split_lines[0]))
        right_list.append(int(split_lines[1]))

# Sorting the lists
left_sorted = sorted(left_list)
right_sorted = sorted(right_list)

# Calculating total distance
total_distance = sum(abs(l - r) for l, r in zip(left_sorted, right_sorted))

# Output
print("Total Distance:", total_distance)
