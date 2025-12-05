data = """..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@."""

with open("data/day4.txt","r") as f:
    data = f.read()

grid = []
for l in data.splitlines():
    grid.append([x for x in l])

# Part 1
def check(i,j):
    cnt = 0 
    for x in range(-1,2):
        for y in range(-1,2):
            dx = i + x
            dy = j + y
            if dx == i and dy == j:
                continue
            
            if (0<=dx<len(grid)) and (0<=dy<len(grid[0])) and grid[dx][dy] == "@":
                cnt += 1
    
    return cnt < 4

rolls = 0
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] != "@": continue
        if check(i,j):
            rolls += 1

print(rolls)

# Part 2
res = 0
while True:
    rolls = []
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] != "@":
                continue
            if check(i,j):
                rolls.append((i,j))
    
    for i,j in rolls:
        grid[i][j] = "."
    
    res += len(rolls)
    if not rolls:
        break 

print(res)