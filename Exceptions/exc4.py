while True:
    try:
        x = int(input("Enter value of X: "))
        break
    except ValueError:
        print('X is not a value')

print(f'you have entered {x}')