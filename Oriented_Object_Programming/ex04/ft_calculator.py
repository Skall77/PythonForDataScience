class calculator:
    """
calculator class

Methods:
    dotproduct: display the dot product of two vectors
    add_vec: Add two vectors and display the result
    sous_vec: Subtract two vectors and display the result
    """
    @staticmethod
    def dotproduct(lhs: list[float], rhs: list[float]) -> None:
        """Return the dot product of two vectors"""
        if not isinstance(lhs, list) or not isinstance(rhs, list):
            raise TypeError("lhs and rhs must be lists")
        if len(lhs) != len(rhs):
            raise ValueError("lhs and rhs must be the same size")
        print("Dot product is:", sum([x * y for x, y in zip(lhs, rhs)]))

    @staticmethod
    def add_vec(lhs: list[float], rhs: list[float]) -> None:
        """Return the sum of two vectors"""
        if not isinstance(lhs, list) or not isinstance(rhs, list):
            raise TypeError("lhs and rhs must be lists")
        if len(lhs) != len(rhs):
            raise ValueError("lhs and rhs must be the same size")
        print("Add Vector is:", [float(x + y) for x, y in zip(lhs, rhs)])

    @staticmethod
    def sous_vec(lhs: list[float], rhs: list[float]) -> None:
        """Return the difference of two vectors"""
        if not isinstance(lhs, list) or not isinstance(rhs, list):
            raise TypeError("lhs and rhs must be lists")
        if len(lhs) != len(rhs):
            raise ValueError("lhs and rhs must be the same size")
        print("Sous Vector is:", [float(x - y) for x, y in zip(lhs, rhs)])
