try:
    def fact(num):
        sum = 1
        for i in range(1,num+1):
            sum = sum * i
        print(sum)

    fact(5)
except Exception as error:
    print(f"error:{error.__Class__.__name__}")






