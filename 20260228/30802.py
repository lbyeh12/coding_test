import sys
import math
n = int(sys.stdin.readline())
size = map(int,sys.stdin.readline().split())
t, p = map(int,sys.stdin.readline().split())
t_count = 0
for s in size:
    if s == 0:
        continue
    if t < s:
        t_count += math.ceil(s/t)
    else:
        t_count += 1
print(t_count)
print(n//p,n%p)