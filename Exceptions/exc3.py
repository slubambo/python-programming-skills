while True:
    try:
        x = int(input("Enter value of X: "))
    except ValueError:
        print('X is not a value')
    else: # the else runs with the try
        break

print(f'you have entered {x}')