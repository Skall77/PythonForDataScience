from S1E9 import Character


class Baratheon(Character):
    """
Baratheon class

Attributes:
    first_name (str): Baratheon first_name
    is_alive (bool): Baratheon is alive (default True)
    family_name (str): Baratheon family name (always Baratheon)
    eyes (str): Baratheon eyes color (always brown)
    hairs (str): Baratheon hair color (always dark)

Methods:
    die(): Set is_alive attribute from True to False
    create_baratheon(): Create a Baratheon object
    def __str__(self): Return a string with the Baratheon representation
    def __repr__(self): Return a string with the Baratheon representation
    """
    def __init__(self, first_name: str, is_alive: bool = True):
        """Constructor for Baratheon class"""
        super().__init__(first_name, is_alive)
        self.family_name = "Baratheon"
        self.eyes = "brown"
        self.hairs = "dark"

    def die(self):
        """Set is_alive attribute from True to False"""
        super().die()

    @staticmethod
    def create_baratheon(first_name: str, is_alive: bool = True):
        """Create a Baratheon object"""
        return Baratheon(first_name, is_alive)

    def __str__(self):
        """Return a string with the Baratheon representation"""
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def __repr__(self):
        """Return a string with the Baratheon representation"""
        return self.__str__()


class Lannister(Character):
    """
Lannister class

Attributes:
    first_name (str): Lannister first_name
    is_alive (bool): Lannister is alive (default True)
    family_name (str): Lannister family name (always Lannister)
    eyes (str): Lannister eyes color (always blue)
    hairs (str): Lannister hair color (always light)

Methods
    die(): Set is_alive attribute from True to False
    create_lannister(): Create a Lannister object
    def __str__(self): Return a string with the Lannister representation
    def __repr__(self): Return a string with the Lannister representation
    """
    def __init__(self, first_name: str, is_alive: bool = True):
        """Constructor for Lannister class"""
        super().__init__(first_name, is_alive)
        self.family_name = "Lannister"
        self.eyes = "blue"
        self.hairs = "light"

    def die(self):
        """Set is_alive attribute from True to False"""
        super().die()

    @staticmethod
    def create_lannister(first_name: str, is_alive: bool = True):
        """Create a Lannister object"""
        return Lannister(first_name, is_alive)

    def __str__(self):
        """Return a string with the Baratheon representation"""
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def __repr__(self):
        """Return a string with the Baratheon representation"""
        return self.__str__()
