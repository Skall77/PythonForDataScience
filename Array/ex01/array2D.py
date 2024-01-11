def slice_me(family: list, start: int, end: int) -> list:
    """
Slice a list between two indexes.

Param:
    family (list): List to slice.
    start (int): Start index.
    end (int): End index.

Return:
    list: Sliced list.
    """
    try:
        if not all(isinstance(sub_list, list) for sub_list in family):
            raise TypeError("Not all elements in the list are lists.")
        family_size = len(family[0])
        if not all(len(sub_list) == family_size for sub_list in family):
            raise ValueError("Not all lists have the same size.")
        print("My shape is : (" + str(len(family)) + ", " + str(family_size)
              + ")")
        print("My new shape is : (" + str(len(family[start:end])) + ", " +
              str(len(family[start:end][0])) + ")")
        return family[start:end]
    except TypeError as te:
        print(f"TypeError: {te}")
        exit(1)
    except IndexError:
        print("The start index must be in the range of the family and the" +
              "range must be positive.")
        exit(1)
    except ValueError as ve:
        print(f"ValueError: {ve}")
        exit(1)


def main():
    """
The main function of the program.
Test slice_me function.
    """
    family = [["toto", "titi"],
              ["tata", "tutu"],
              ["thth", "tyty"],
              ["trtr", "tsts"]]
    print(slice_me(family, 0, 5))
    print(slice_me(family, 1, -1))


if __name__ == "__main__":
    main()
