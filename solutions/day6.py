import math

data = """123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +
"""

with open("data/day6.txt","r") as f:
    data = f.read()

# Part 1
ops = []
ls = []
for l in data.splitlines():
    ls.append(l.split())

ops = ls.pop()

lsT= []
for j in range(len(ls[0])):
    tmp = []
    for i in range(len(ls)):
        tmp.append(int(ls[i][j]))
    lsT.append(tmp)

res = 0 
for i in range(len(lsT)):
    op = ops[i]
    if op == "*":
        res += math.prod(lsT[i])
    else:
        res += sum(lsT[i])
    
print(res)

# Part 2
data = data.splitlines()[:-1]
ls = []
for l in data:
    ls.append([x for x in l])

tmp = ls[0][:]

for i in range(1,len(data)):
    r = data[i]
    for j in range(len(r)):
        tmp[j] += r[j]

tmp = [x.strip() for x in tmp]

ls = []
t = []
for x in tmp:
    if x == "":
        ls.append(t)
        t = []
    else:
        t.append(int(x))

ls.append(t)

res = 0 
for i in range(len(ls)):
    op = ops[i]
    if op == "*":
        res += math.prod(ls[i])
    else:
        res += sum(ls[i])
    
print(res)