num=list(range(0,10001))
num2=list()
i=0
for i in num:
    for n in str(i):
        i+=int(n)
    if i<=10000:
        num2.append(i)
for num2 in set(num2):
    num.remove(num2)
for i in num:
    print(i)