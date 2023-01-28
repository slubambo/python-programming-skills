try:
    x = int(input("Enter X: "))
    print(f'You have entered {x}')
except ValueError:
    print('Wrong Value')