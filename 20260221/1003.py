import sys
from collections import defaultdict
n = int(sys.stdin.readline())
dp = defaultdict(list)
for _ in range (n):
    fibo = int(sys.stdin.readline())
    for i in range(fibo+1):
        if i == 0:
            dp[i] = [1,0]
        elif i == 1:
            dp[i] = [0,1]
        else:
            dp[i] = [dp[i-1][0] + dp[i-2][0],dp[i-1][1] + dp[i-2][1]]
    print(dp[fibo][0],dp[fibo][1])