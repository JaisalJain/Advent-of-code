from collections import Counter

# Input lists
left_list = []
right_list = []

# Opening day1_input.txt and splitting left and right lists
with open('day1_input.txt', 'r') as locations:
    for lines in locations:
        split_lines = lines.replace('\n', "").split()  
        left_list.append(int(split_lines[0]))
        right_list.append(int(split_lines[1]))

# Count the occurrences of each number in the right list
right_counts = Counter(right_list)

# Calculating the total similarity score
similarity_score = sum(left_number * right_counts.get(left_number, 0) 
                       for left_number in left_list)

# Output the similarity score
print("Similarity Score:", similarity_score)
