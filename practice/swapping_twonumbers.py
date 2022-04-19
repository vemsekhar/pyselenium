
a = 10
b = 20
print("Before swapping value of a is", a , "and b is", b)

#code to swap a & b
a = a ^ b
b = b ^ a
a = b ^ a
print("After swapping value of a is", a , "and b is", b)


'''
method-2
'''
a = 100
b = 202
print("Before swapping value of a is", a , "and b is", b)

#code to swap a & b
a = a + b #30
b = a - b #10
a = a - b #20
print("After swapping value of a is", a , "and b is", b)
