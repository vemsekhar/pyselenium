dic = {'a':1,'b':2,'c':3}
for i in dic.values():
    if i == 2:
        continue
    print(i,end='  ')

for i in dic.items():
    print(i,end=" ")