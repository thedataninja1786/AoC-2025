with open("data/day5.txt","r") as f:
    data = f.read()

# part 1
ranges = data.split("\n\n")[0].splitlines()
ingredients = list(map(int,data.split("\n\n")[1].splitlines()))

fresh_ranges = [] 
for l in ranges:
    x,xx = l.split("-")[0], l.split("-")[1]
    x = int(x)
    xx = int(xx)
    fresh_ranges.append(range(x,xx+1))

available = set()
for ingr in ingredients:
    for rng in fresh_ranges:
        if ingr in rng:
            available.add(ingr)
    
print(len(available))

# Part 2 
res = 0
new_ranges = []
for l in ranges:
    x,xx = l.split("-")[0], l.split("-")[1]
    new_ranges.append((int(x),int(xx)))

# sweeping line algo
comb_ranges = []
new_ranges.sort()

x,y = new_ranges.pop(0)
while new_ranges:
    xx,yy = new_ranges.pop(0)
    if xx <= y <= yy or y > yy:
        y = max(y,yy)
    else:
        comb_ranges.append((x,y))
        x,y = xx,yy

if (x,y) not in comb_ranges:
    comb_ranges.append((x,y))

for x,y in comb_ranges:
    res += y - x + 1

print(res)
