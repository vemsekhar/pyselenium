
'''dic = {'name':'ashok','date': 1984,'place':'chennai'}

for i,J in dic.items():
    if J == 1984:
         continue
    print(i)'''


dic = {'name':'ashok','date': 1984,'place':'chennai'}
print(dic.popitem())
print(dic)