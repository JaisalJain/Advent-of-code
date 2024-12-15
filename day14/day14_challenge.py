import re

data_file = open("C:\\Users\\mites\\Desktop\\Advent_of_code\\day14_input.txt", 'r')

part = 2
#wide, height = 11, 7
wide, height = 101, 103

def solve(part):
    if part == 1:

        robots = {}
        for line in data_file:
            pattern = re.compile("p=(\d+),(\d+) v=(-?)(\d+),(-?)(\d+)")
            match = pattern.match(line)
            x, y, sx, vx, sy, vy = match.group(1,2,3,4,5,6)
            x, y = int(x), int(y)
            vx = int(vx) if sx == '' else -int(vx)
            vy = int(vy) if sy == '' else -int(vy)
            if (x,y) not in robots.keys() :
                robots[(x,y)] = [(vx,vy)]
            else :                
                robots[(x,y)].append((vx,vy))
        data_file.close()
        
        for seconds in range(100) :
            new_robots = {}
            for (x,y) in robots.keys() :
                for (vx,vy) in robots[(x,y)] :
                    new_x = (x + vx) % wide
                    new_y = (y + vy) % height
                    if (new_x,new_y) not in new_robots.keys() :
                        new_robots[(new_x,new_y)] = [(vx,vy)]
                    else :
                        new_robots[(new_x,new_y)].append((vx,vy))
            robots = new_robots
        
        total = 0
        for x in range(wide//2) :
            for y in range(height//2) :
                if (x,y) in robots.keys() :
                    total += len(robots[(x,y)])
        quadrant = 0
        for x in range(wide//2+1,wide) :
            for y in range(height//2) :
                if (x,y) in robots.keys() :
                    quadrant += len(robots[(x,y)])
        total *= quadrant
        quadrant = 0
        for x in range(wide//2) :
            for y in range(height//2+1, height) :
                if (x,y) in robots.keys() :
                    quadrant += len(robots[(x,y)])
        total *= quadrant
        quadrant = 0
        for x in range(wide//2+1,wide) :
            for y in range(height//2+1, height) :
                if (x,y) in robots.keys() :
                    quadrant += len(robots[(x,y)])
        total *= quadrant
        return total  

    elif part == 2:
        
        robots = {}
        map = [['.' for x in range(wide)] for y in range(height)]
        for line in data_file:
            pattern = re.compile("p=(\d+),(\d+) v=(-?)(\d+),(-?)(\d+)")
            match = pattern.match(line)
            x, y, sx, vx, sy, vy = match.group(1,2,3,4,5,6)
            x, y = int(x), int(y)
            vx = int(vx) if sx == '' else -int(vx)
            vy = int(vy) if sy == '' else -int(vy)
            if (x,y) not in robots.keys() :
                robots[(x,y)] = [(vx,vy)]
                map[y][x] = 1
            else :                
                robots[(x,y)].append((vx,vy))
                map[y][x] += 1
        data_file.close()
        
        print('\n'.join([''.join([str(cell) for cell in row]) for row in map]))
        seconds = 0
        # The supposition is that to form the Easter Egg, each robot must be in a separate position (=> not more than 1s in the map)
        while '2' in '\n'.join([''.join([str(cell) for cell in row]) for row in map]) :
            new_robots = {}
            map = [['.' for x in range(wide)] for y in range(height)]
            for (x,y) in robots.keys() :
                    
                for (vx,vy) in robots[(x,y)] :
                    new_x = (x + vx) % wide
                    new_y = (y + vy) % height
                    if (new_x,new_y) not in new_robots.keys() :
                        new_robots[(new_x,new_y)] = [(vx,vy)]
                        map[new_y][new_x] = 1
                    else :
                        new_robots[(new_x,new_y)].append((vx,vy))
                        map[new_y][new_x] += 1
            robots = new_robots
            seconds += 1
        print()
        print('\n'.join([''.join([str(cell) for cell in row]) for row in map]))
        
        total = seconds
        return total 

    else:
        data_file.close()
        return 'Invalid part'


print(solve(part))
