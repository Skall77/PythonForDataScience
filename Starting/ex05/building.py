import sys


def display_sums_characters(text):
    """
    Display the number of characters in the text, and the number of
    characters for each category (upper letters, lower letters, punctuation
    marks, spaces, digits).

    Param:
    text (str): The text to count.

    Return:
        None
    """

    char_count = 0
    upper_count = 0
    lower_count = 0
    digit_count = 0
    space_count = 0
    punctuation_count = 0

    for character in text:
        char_count += 1
        if character.isupper():
            upper_count += 1
        elif character.islower():
            lower_count += 1
        elif character.isdigit():
            digit_count += 1
        elif character.isspace():
            space_count += 1
        elif character in ",.!?;:\'\"-[{}]()":
            punctuation_count += 1
    print("The text contains", char_count, "characters:")
    print(upper_count, "upper letters")
    print(lower_count, "lower letters")
    print(punctuation_count, "punctuation marks")
    print(space_count, "spaces")
    print(digit_count, "digits")


def main():
    """
    The main function of the program.
    Check if the user provided an argument, if not, ask for a text.

    Param:
        None
    Return:
        None
    """

    try:
        if len(sys.argv) > 2:
            raise AssertionError("more than one argument is provided")

        if len(sys.argv) == 2 and sys.argv[1] != "None":
            display_sums_characters(sys.argv[1])
        else:
            print("What is the text to count?")
            while True:
                try:
                    text = input()
                    break
                except EOFError:
                    break
            display_sums_characters(text)
    except AssertionError as err:
        print(AssertionError.__name__ + ":", err)


if __name__ == '__main__':
    main()
