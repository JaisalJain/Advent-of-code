file_path = 'day6_input.txt'
with open(file_path, 'r') as file:
    maze = [list(line.strip()) for line in file.readlines()]

DIRECTIONS = {'^': (-1, 0), '>': (0, 1), 'v': (1, 0), '<': (0, -1)}
TURN_RIGHT = {'^': '>', '>': 'v', 'v': '<', '<': '^'}

rows, cols = len(maze), len(maze[0])
guard_pos = None
guard_dir = None

for r in range(rows):
    for c in range(cols):
        if maze[r][c] in DIRECTIONS:
            guard_pos = (r, c)
            guard_dir = maze[r][c]
            maze[r][c] = '.'  # Clear the starting position
            break
    if guard_pos:
        break

# Track the positions visited
visited_positions = set()
visited_positions.add(guard_pos)

# Simulate the guard's movement
while True:
    next_r, next_c = guard_pos[0] + DIRECTIONS[guard_dir][0], guard_pos[1] + DIRECTIONS[guard_dir][1]

    if not (0 <= next_r < rows and 0 <= next_c < cols):  # Guard leaves the mapped area
        break

    if maze[next_r][next_c] == '#':  # Obstacle ahead, turn right
        guard_dir = TURN_RIGHT[guard_dir]
    else:  # Move forward
        guard_pos = (next_r, next_c)
        visited_positions.add(guard_pos)


print(len(visited_positions))
