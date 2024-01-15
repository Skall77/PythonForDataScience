class calculator:
    """
calculator class

Methods:
    __add__: Add  the rhs to every element of the lhs
    __sub__: Subtract the rhs to every element of the lhs
    __mul__: Multiply the rhs to every element of the lhs
    __truediv__: Divide the lhs by the rhs
    """

    def __init__(self, vector: list):
        """Constructor for Calculator class"""
        if not isinstance(vector, list):
            raise TypeError("vector must be a list")
        if not all(isinstance(x, (int, float)) for x in vector):
            raise TypeError("vector must contain only integers or floats")
        self.vector = vector

    def __add__(self, object) -> None:
        """Add the rhs to every element of the lhs"""
        if not isinstance(object, (int, float)):
            raise TypeError("object must be an integer or a float")
        self.vector = [x + object for x in self.vector]
        print(self.vector)

    def __sub__(self, object) -> None:
        """Subtract the rhs to every element of the lhs"""
        if not isinstance(object, (int, float)):
            raise TypeError("object must be an integer or a float")
        self.vector = [x - object for x in self.vector]
        print(self.vector)

    def __mul__(self, object) -> None:
        """Multiply the rhs to every element of the lhs"""
        if not isinstance(object, (int, float)):
            raise TypeError("object must be an integer or a float")
        self.vector = [x * object for x in self.vector]
        print(self.vector)

    def __truediv__(self, object) -> None:
        """Divide the lhs by the rhs"""
        if not isinstance(object, (int, float)):
            raise TypeError("object must be an integer or a float")
        if object == 0:
            raise ZeroDivisionError("division by zero is undefined")
        self.vector = [x / object for x in self.vector]
        print(self.vector)
