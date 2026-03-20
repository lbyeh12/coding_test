import sys
num = int(sys.stdin.readline())
n = 1
pre = 1
while num > pre:
    pre += 6*n
    n += 1
print(n)