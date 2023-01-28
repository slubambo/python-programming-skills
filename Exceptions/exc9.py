#creating custom exceptions 
# - clean code
# - Documentation 
# - Uniqueness 

class AgeErrorException(Exception): #inheritance 
    def _init_(self, value):
        self.value = value

try:
    age = int(input("Enter age: "))

    if age <= 0 or age > 120:
        raise AgeErrorException("Out of range age")
    print(f"Age entered is: {age} ")
except ValueError:
    print("Only integers")
except AgeErrorException as ageErr:
    print(ageErr)