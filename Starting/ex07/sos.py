import sys


def main():
    """
The main function of the program.
Check if there is only one alphanumeric argument and then
encode it in Morse code.
    """
    try:
        if len(sys.argv) != 2:
            raise AssertionError("the arguments are bad")
        for c in sys.argv[1]:
            if c.isalnum() is False and c.isspace() is False:
                raise AssertionError("the arguments are bad")
        NESTED_MORSE = {
                'A': '.- ',
                'B': '-... ',
                'C': '-.-. ',
                'D': '-.. ',
                'E': '. ',
                'F': '..-. ',
                'G': '--. ',
                'H': '.... ',
                'I': '.. ',
                'J': '.--- ',
                'K': '-.- ',
                'L': '.-.. ',
                'M': '-- ',
                'N': '-. ',
                'O': '--- ',
                'P': '.--. ',
                'Q': '--.- ',
                'R': '.-. ',
                'S': '... ',
                'T': '- ',
                'U': '..- ',
                'V': '...- ',
                'W': '.-- ',
                'X': '-..- ',
                'Y': '-.-- ',
                'Z': '--.. ',
                '0': '----- ',
                '1': '.---- ',
                '2': '..--- ',
                '3': '...-- ',
                '4': '....- ',
                '5': '..... ',
                '6': '-.... ',
                '7': '--... ',
                '8': '---.. ',
                '9': '----. ',
                ' ': '/ ',
        }
        print(''.join(NESTED_MORSE[c] for c in sys.argv[1].upper()))
    except AssertionError as err:
        print(AssertionError.__name__ + ":", err)


if __name__ == "__main__":
    main()
