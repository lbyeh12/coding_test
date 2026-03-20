import sys

a_a, a_d = map(int,sys.stdin.readline().split())
b_a, b_d = map(int,sys.stdin.readline().split())
a_alive = True
b_alive = True
while a_alive and b_alive:
    if a_a >= b_d:
        b_alive = False
    if b_a >= a_d:
        a_alive = False
    a_d -= b_a
    b_d -= a_a
    
if a_alive:
    print("PLAYER A")
elif b_alive:
    print("PLAYER B")
else:
    print("DRAW")