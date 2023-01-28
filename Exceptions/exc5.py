def main():
    z = get_int()
    print(f'you have entered {z}')

def get_int():
    while True:
        try:
            x = int(input("Enter value of X: "))
            break
        except ValueError:
            print('X is not a value')
    return x

main()

    