import sys
input_num = sys.stdin.readline()
num = int(input_num)
str_list = list(input_num)
if "7" not in str_list:
    if num%7 != 0:
        print(0)
    else:
        print(1)
else:
    if num%7 != 0:
        print(2)
    else:
        print(3)