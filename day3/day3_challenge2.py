import re

with open("day3_input.txt", "r") as inputfile:
    text = inputfile.read()

pattern = r"(do\(\)|don't\(\))|mul\((\d{1,3}),(\d{1,3})\)"

matches = re.findall(pattern, text)

mul_enabled = True
total = 0

# Loop through each match found in the text
for match in matches:
    # If the match is "do()", enable multiplication
    if match[0] == "do()":
        mul_enabled = True
    # If the match is "don't()", disable multiplication
    elif match[0] == "don't()":
        mul_enabled = False
    else:
        # Only process multiplication if it's enabled
        if mul_enabled:
            x, y = int(match[1]), int(match[2])
            total += x * y

print(total)
