
'''
program for student grades using if ,elif 
'''
a= int(input("enter the marks  "))
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