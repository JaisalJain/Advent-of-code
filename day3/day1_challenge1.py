import re

with open("day3_input.txt", "r") as inputfile:
    text = inputfile.read()

#x and y are 1 to 3 digit numbers
pattern = r"mul\((\d{1,3}),(\d{1,3})\)"

matches = re.findall(pattern, text)

# Calculate the sum of products of the matched pairs of numbers
total = sum(int(x) * int(y) for x, y in matches)

print(total)
