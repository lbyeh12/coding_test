import sys
n = int(sys.stdin.readline())
if n%2024 == 0 and n<=100000:
    print("Yes")
else:
    print("No")
