class HallAllocationError(Exception):
    pass


class HomeDistanceError(Exception):
    pass


def checkHomeDist(distance):
    maxDistance = 80

    if(distance < maxDistance):
        raise HomeDistanceError("You can commute from Home")
    else:
        print("You maybe allocated a Hall of Residence")


def checkAge(age):
    ageLimit = 30
    if age > ageLimit:
        raise HallAllocationError("Too old")
    else:
        dist = int(input("Enter Distance: "))
        checkHomeDist(dist)
        print("Qualified")


try:
    age = int(input("What is your age: "))

    checkAge(age)


except HallAllocationError as ageErr:
    print(ageErr)
except HomeDistanceError as homeErr:
    print(homeErr)
