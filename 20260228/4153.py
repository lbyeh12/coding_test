import sys
tmp = []
while True:
    length = map(int,sys.stdin.readline().split())
    a,b,c = sorted(length)
    if a==0 and b==0 and c==0:
        break
    if c**2 == a**2+b**2:
        tmp.append("right")
    else:
        tmp.append("wrong")
for m in tmp:
    print(m)