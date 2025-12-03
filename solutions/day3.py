
data = """987654321111111
811111111111119
234234234234278
818181911112111"""

with open("data/day3.txt","r") as f:
    data = f.read()

# Part 1
res = 0 
for l in data.splitlines():
    l = [int(x) for x in l]
    r = 0
    for i in range(1,len(l)):
        r = max(r,int(str(max(l[:i])) + str(max(l[i:]))))
    res += r

print(res)

# Part 2
res = 0
for l in data.splitlines():
    l = [int(x) for x in l]
    stack = []
    while l:
        x = l.pop(0)
        while stack and stack[-1] < x and 12 - len(stack) <= len(l):
            stack.pop()
        stack.append(x)
    

    s = int("".join(str(x) for x in stack[:12]))
    res += s
    
print(res)

        
        
        
