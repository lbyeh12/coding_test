import sys

n = int(sys.stdin.readline())
sum = 0
time = 1
count = 0
while n > sum:
    if sum+time > n:
        time = 1
    else:
        sum += time
        time += 1
        count += 1
print(count)