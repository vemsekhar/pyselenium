

#In Python 2
map(lambda x : x*2, [1, 2, 3, 4]) #Output [2, 4, 6, 8]
# Python 3
a = map(lambda x : x*2, [1, 2, 3, 4]) # returns a map object
# use a magic method __next__ to get values from the object.
a.__next__() # 2
a.__next__() # 4
print(list(a)) # [4, 8] it will create a list and append remaining values from the