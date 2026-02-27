import sys
msg = []
while True:
    sweet, sour = map(int, sys.stdin.readline().split())
    if sweet == 0 and sour == 0:
        break
    if sweet + sour == 13:
        msg.append("Never speak again.")
        continue
    if sweet > sour:
        msg.append("To the convention.")
    elif sweet < sour:
        msg.append("Left beehind.")
    elif sweet == sour:
        msg.append("Undecided.")
for m in msg:
    print(m)