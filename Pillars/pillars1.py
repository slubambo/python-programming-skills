def mydeco(func):
    def wrapper():
        print("Hello decorator")
        func()
        print("Done")

def hellowdeco():
    print("Yes there!")

hello = mydeco(hellowdeco)

hello()

