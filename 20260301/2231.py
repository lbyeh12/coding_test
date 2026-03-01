import sys

n = int(sys.stdin.readline())
gen = []
for i in range(n-1,1,-1):
    nums = list(map(int,str(i)))
    if i+sum(nums) == n:
        gen.append(i)
if gen:
    print(sorted(gen)[0])
else:
    print(0)