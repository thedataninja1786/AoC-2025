from functools import lru_cache

data = """.......S.......
...............
.......^.......
...............
......^.^......
...............
.....^.^.^.....
...............
....^.^...^....
...............
...^.^...^.^...
...............
..^...^.....^..
...............
.^.^.^.^.^...^.
..............."""

with open("data/day7.txt","r") as f:
    data = f.read()

start = None
grid = []

for l in data.splitlines():
    grid.append(list(l))

N,M = len(grid), len(grid[0])


f = False
for i in range(N):
    for j in range(M):
        if grid[i][j] == "S":
            start = (i,j)
            f = True
            break 
    if f: break 

# Part 1
res = set()
coords = set([start])
while coords:
    new_coords = set()
    for x,y in coords:
        while x < N:
            if x + 1 == N:
                break 
            x += 1
            if x + 1 < N and grid[x][y] == "^":
                res.add((x+1,y))
                if y - 1 >= 0:
                    new_coords.add((x,y-1))
                if y + 1 < M:
                    new_coords.add((x,y+1))
                break 

    coords = new_coords.copy() 

print(len(res))

# Part 2 
@lru_cache
def dfs(i, j):
    if i == N - 1:
        return 1

    while i + 1 < N:
        i += 1
        if grid[i][j] == "^":
            paths = 0
            for nj in (j - 1, j + 1):
                if 0 <= nj < M:
                    paths += dfs(i, nj)
            return paths
        
    # reached end without hitting a spliter
    return 1

print(dfs(start[0],start[1]))
            
    
    
    


