#try ... except ... else ... finally

try:
    num = int(input('Enter Numerator: '))
    denom = int(input('Enter Denominator: '))
    quotient  = num / denom 

    print("Correct Division")
except ZeroDivisionError: 
    print("You can't divide by Zero")
except ValueError:
    print("Only integers needed")
else:
    print("Quotient = ", quotient)

finally:
    print('I\'m always here')