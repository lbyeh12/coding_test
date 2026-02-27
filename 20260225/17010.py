import sys

n = int(sys.stdin.readline())
for _ in range(n):
    num, a  =  map(str, sys.stdin.readline().split())
    num = int(num)
    print(a*num)

