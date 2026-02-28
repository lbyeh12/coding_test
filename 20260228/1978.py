import sys
_ = int(sys.stdin.readline())
cnt = 0
num = map(int,sys.stdin.readline().split())
for n in num:
    if n <= 1:
        continue
    is_prime = True
    for i in range(2,int(n**(1/2))+1):
        if n%i == 0:
            is_prime = False
            break
    if is_prime:
        cnt+=1
print(cnt)
