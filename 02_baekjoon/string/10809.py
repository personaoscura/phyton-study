li=list(chr(i) for i in range(ord('a'), ord('z')+1))
li2=list()
s = input()
for i in li:
    li2.append(s.find(i))
for i in li2:
    print(i, end=' ')