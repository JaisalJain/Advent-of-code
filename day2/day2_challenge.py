# Function to validate if a report is safe
def validate(report):
    # Check if the report is increasing
    increase = all(i > j for i, j in zip(report, report[1:]))
    
    # Check if the report is decreasing
    decrease = all(i < j for i, j in zip(report, report[1:]))
    
    # Check if the difference between levels is between 1 and 3
    difference = all(abs(i - j) <= 3 and abs(i - j) >= 1 for i, j in zip(report, report[1:]))
    
    return (increase or decrease) and difference

# Function to attempt fixing a report by removing one element and checking if it becomes valid
def fix(report):
    for i in range(len(report)):
        tmp = report[:] 
        del tmp[i]  
        if validate(tmp):  # Check if the modified report is safe
            return True
    return False 
  
# Function to count the number of safe reports
def part1(reports):
    safe = 0
    for report in reports:
        if validate(report):
            safe += 1
    return safe

# Function to count the number of safe or fixable reports
def part2(reports):
    safe = 0
    # Loop through all reports
    for report in reports:
        if validate(report):
            safe += 1  # Count valid reports
        elif fix(report):
            safe += 1  # Count reports that can be fixed
    return safe

# Read the reports from the input file and store them as lists of integers
reports = []
with open('day2_input.txt', 'r') as locations:
    for line in locations:
        line = map(lambda x: int(x), line.strip().split())
        reports.append(list(line))

print(f"Part 1 : {part1(reports)}")  
print(f"Part 2 : {part2(reports)}")  
