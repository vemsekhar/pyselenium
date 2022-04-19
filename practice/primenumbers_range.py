'''
prime number program

'''
'''a = int(input("enter the number  "))

for i in range(2,a):
    if a % i == 0:
        print(f"the entered number {a} is not a prime number")
        break

else:
    print(f"enter number {a} is prime")'''


'''
find range of prime numbers
'''

a = int(input("enter the number  "))
l=[]
for i in range(2,a):

    for j in range(2,i):
        if i % j == 0:
            print(f"given number {i} is not a prime number")
            break

    else:
        l.append(i)
print(l)



