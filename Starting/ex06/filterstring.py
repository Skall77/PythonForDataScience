import sys
from ft_filter import ft_filter


def main():
    """
The main function of the program.
Check arguments and then output a list of word from arg[1] that
are longer than arg[2].
    """
    try:
        if len(sys.argv) != 3:
            raise AssertionError("the arguments are bad")
        if not sys.argv[2].isdigit() or int(sys.argv[2]) < 0:
            raise AssertionError("the arguments are bad")
        string_list = list(ft_filter(lambda x: len(x) > int(sys.argv[2]),
                                     sys.argv[1].split()))
        print(string_list)
    except AssertionError as err:
        print(AssertionError.__name__ + ":", err)


if __name__ == "__main__":
    main()
