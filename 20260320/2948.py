import sys
import datetime

d, m = map(int,sys.stdin.readline().split())
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
y = 2009

if m > 12:
    y += m//12
    m = m%12

date = datetime.date(y,m,d).weekday()
print(days[date])