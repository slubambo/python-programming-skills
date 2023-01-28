def main():
    z = get_int()
    print(f'you have entered {z}')

def get_int():
    while True:
        try:
            return int(input("Enter value of X: "))
        except ValueError:
            print('X is not a value')

main()