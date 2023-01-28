import sys

if len(sys.argv) < 3:
    sys.exit("Few arguments, add more")
elif len(sys.argv) > 3:
    print("Enough args")
else:
    print("Hello there, I am", sys.argv[1])
