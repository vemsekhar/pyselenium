from operator import index

a= int(input("enter the number "))
try:
    sum = 1
    num = a/0
    for i in range(1,a+1):
        sum=sum*i
    print(sum)
except Exception as error:
    print(f"error : {error.__class__.__name__}")

else:
    #a= int(input("enter the marks  "))
    if a >100:
        print("Enter value should be below 100")
    elif a >=90 and a<=100:
        print(f"student secured {a} marks and he is Grade A+")
    elif a < 90 and a >= 75:
        print(f"student secured {a} marks and he is Grade A")
    elif a < 75 and a >= 60:
        print(f"student secured {a} marks and he is Grade B")
    elif a < 60 and a >= 40:
        print(f"student secured{a} marks and he is Grade C")
    else:
        print(f"Student secured {a} marks and he is failed")
finally:
   # a=int(input("enter number:  "))

    if a % 2 == 0 :
        print(f"{a} is an even number")

    else:
        print(f"{a} is odd number")







