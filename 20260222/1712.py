import sys
a,b,c = map(int,(sys.stdin.readline().split()))
n = c-b
if n<=0:
    print(-1)
else:
    print((a//n)+1)