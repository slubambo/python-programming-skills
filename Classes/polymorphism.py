##Polymorphism
# def rolexPoly(rolex):
#     print(rolex)
#
# rolexPoly(rolex)
# rolexPoly(specialRolex)

#Encapsulation
class Rolexx:
    def __int__(self, toppings):
        self.toppings = toppings

    @property
    def __repr__(self):
        return f"Rolex x toppings are: {','.join(self.__toppings)}"

rolexx = Rolexx(["tomatoes", "onions"])

print(rolexx)