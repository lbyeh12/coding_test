import sys 

_ = int(sys.stdin.readline())
submit = []
nums = list(map(int,sys.stdin.readline().split()))
max_num = max(nums)
for num in nums:
    submit.append((num/max_num)*100)

print(sum(submit)/len(submit))