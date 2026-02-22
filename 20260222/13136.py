import sys
import math
x,y,n = map(int,(sys.stdin.readline().split()))
print(math.ceil(x/n)*math.ceil(y/n))