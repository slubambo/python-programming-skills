class HallAllocationError(Exception):
    pass

def checkAge(age):
    ageLimit = 30
    if age > ageLimit:
        raise HallAllocationError("Too old")
    else:
        print("Qualified")
    

try:
    age = int(input("What is your age: "))

    checkAge(age)

except HallAllocationError as ageErr:
    print(ageErr)
