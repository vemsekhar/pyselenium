mylist = [2,3,1,22,1,1]

result = [i for i, x in enumerate(mylist)
                 if x == 1]
print(result)

a = { i:i**2 for i in mylist}

print(a)