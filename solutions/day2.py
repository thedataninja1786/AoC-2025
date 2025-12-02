data = """11-22,95-115,998-1012,1188511880-1188511890,222220-222224,
1698522-1698528,446443-446449,38593856-38593862,565653-565659,
824824821-824824827,2121212118-2121212124"""

with open("data/day2.txt","r") as f:
    data = f.read()

# Part 1
def good(x):
    sx = str(x)
    l = len(sx) // 2
    return not sx[:l] == sx[l:]

res = 0 
for l in data.split(","):
    x,xx = l.split("-")
    x = int(x)
    xx = int(xx)
    for y in range(x,xx+1):
        if not good(y):
            res += y
print(res)

# Part 2 
def good(x):
    sx = str(x)
    for i in range(len(sx)):
        for j in range(i,len(sx)+1):
            ss = sx[i:j]
            cnt = sx.count(ss)
            if cnt > 1 and cnt * len(ss) == len(sx):
                return False
    return True

res = 0 
for l in data.split(","):
    x,xx = l.split("-")
    x = int(x)
    xx = int(xx)
    invalid = []
    for y in range(x,xx+1):
        if not good(y):
            invalid.append(y)
            res += y
print(res)