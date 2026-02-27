import sys
tmp = []
while True:
    n = float(sys.stdin.readline())
    if n == 0:
        break
    tmp.append(f"{(1+n+n**2+n**3+n**4):.2f}")
for num in tmp:
    print(num)