import sys
msg = []
while True:
    nums = str(sys.stdin.readline().strip())
    if nums == "0":
        break
    if nums == nums[::-1]:
        msg.append("yes")
    else:
        msg.append("no")

for m in msg:
    print(m)
    
