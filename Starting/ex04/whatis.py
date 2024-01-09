import sys

try:
    if len(sys.argv) > 2:
        raise AssertionError("more than one argument is provided")

    if len(sys.argv) == 2:
        try:
            number = int(sys.argv[1])
        except ValueError:
            raise AssertionError("Argument is not an integer")
        if number % 2 == 0:
            print("I'm Even.")
        else:
            print("I'm Odd.")
except AssertionError as err:
    print(AssertionError.__name__ + ":", err)
