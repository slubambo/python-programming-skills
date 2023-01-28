num1 = int(input("Num1: "))
num2 = int(input("Num2: "))

if num2 == 0:
    raise ZeroDivisionError("Not possible")
else:
    print("Quotient = ", num1/num2)