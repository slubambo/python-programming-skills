class Rolex:

    # attributes
    chapati_size: str
    number_of_eggs: int()
    withSalt: bool
    toppings: bool

    def price(self, tax):
        total = 0.0

        if self.chapati_size == 'large':
            total += 3000
        elif self.chapati_size == 'medium':
            total += 2000
        else:
            total += 1000

        total = total + self.number_of_eggs * 500

        if self.toppings:
            total += 1000

        total += (tax * total)

        return total


a_rolex: Rolex = Rolex()

a_rolex.chapati_size = 'large'
a_rolex.number_of_eggs = 5
a_rolex.withSalt = False
a_rolex.toppings = False





#print(type(a_rolex))

#print(a_rolex)

print(a_rolex.price(0.4))
