# Function to count X-MAS patterns in the grid
def count_xmas(grid):
    rows, cols = len(grid), len(grid[0])
    count = 0
    
    for r in range(1, rows-1):
        for c in range(1, cols-1):
            # Center must be 'A'
            if grid[r][c] == 'A':
                # Check the four possible patterns
                if ((grid[r-1][c-1], grid[r-1][c+1], grid[r+1][c-1], grid[r+1][c+1]) in 
                    [('M', 'S', 'M', 'S'), ('S', 'M', 'S', 'M'), ('M', 'M', 'S', 'S'), ('S', 'S', 'M', 'M')]):
                    count += 1
                    
    return count

with open("day4_input.txt", "r") as file:
    grid = [line.strip() for line in file]

# Output the result
print(count_xmas(grid))
