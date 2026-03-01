import sys

n,m = map(int,sys.stdin.readline().split())
nums = list(map(int,sys.stdin.readline().split()))

def black_jack(n,m,nums):
    maxi = []
    for i in range(n):
        for j in range(i+1,n):
            for k in range(j+1,n):
                sum_n = nums[i]+nums[j]+nums[k]
                if sum_n == m:
                    return m
                else:
                    if sum_n < m:
                        maxi.append(sum_n)
    return (sorted(maxi,reverse=True)[0])

print(black_jack(n,m,nums))