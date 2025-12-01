data = """L68
L30
R48
L5
R60
L55
L1
L99
R14
L82""".splitlines()


with open("data/day1.txt","r") as f:
    data = f.read().splitlines()


def move(d,x):
    if d == "L":
        return -x
    return x

# Part 1
position = 50
res = 0
for l in data:
    d,x = l[0],int(l[1:])
    position = (position + move(d,x)) % 100
    if position == 0:
        res += 1
    
print(res)

# Part 2 
res = 0 
position = 50
for l in data:

    d,x = l[0],int(l[1:])
    for _ in range(x):
        diff = move(d,1)

        position = (position + diff) % 100
        if position == 0:
            res += 1

print(res)
    