a = int(input("enter the number  "))

for i in range(2,a):
    if a % i == 0:
       print("given number is not prime")
       break
else:
    print("given number is prime number")
   



