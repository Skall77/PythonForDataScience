import numpy as np


def give_bmi(height: list[int | float], weight: list[int | float])\
        -> list[int | float]:
    """
Create a list of BMI from a list of height and weight.

Param:
    height (list[int | float]): List of height.
    weight (list[int | float]): List of weight.

Return:
    list[int | float]: List of BMI.
    """
    try:
        if len(height) != len(weight):
            raise ValueError("The height and weight lists must be the\
                            same size.")
        if any(h == 0 for h in height):
            raise ZeroDivisionError("Error: Some height values are zero.")
        return list(np.array(weight) / np.array(height) ** 2)
    except TypeError:
        print("The height and weight must be int or float.")
        exit(1)
    except ZeroDivisionError as zde:
        print(f"ZeroDivisionError: {zde}")
        exit(1)
    except ValueError as ve:
        print(f"ValueError: {ve}")
        exit(1)


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """
Check if the BMI is above a limit.

Param:
    bmi (list[int | float]): List of BMI.
    limit (int): Limit to check.

Return:
    list[bool]: List of boolean.
    """
    try:
        return list(np.array(bmi) > limit)
    except TypeError:
        print("The BMI must be a list of int or float, and the limit must be\
            an int.")
        exit(1)


def main():
    """
The main function of the program.
Test give_bmi and apply_limit functions.
    """
    height = [1.60, 1.60]
    weight = [60, 80]
    bmi = give_bmi(height, weight)
    print(bmi, type(bmi))
    print(apply_limit(bmi, 26))


if __name__ == "__main__":
    main()
