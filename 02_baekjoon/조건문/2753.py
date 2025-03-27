year = int(input())
if year%4== 0:
    a=1
else: a=0

if year%100==0:
    a=0
if year%400==0:
    a=1
print(a)