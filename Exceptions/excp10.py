# creating custom exceptions
# - clean code
# - Documentation
# - Uniqueness

class AgeErrorException(Exception):  # inheritance
    def _init_(self, value, message="Age out of Range"):
        self.value = value
        self.message = message
        super()._init_(self.message)


age = int(input("Enter age: "))

if not 0 < age < 80:
    raise AgeErrorException(age)
