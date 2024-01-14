from abc import ABC, abstractmethod


class Character(ABC):
    """
Character abstract class

Attributes:
    first_name (str): Character first_name
    is_alive (bool): Character is alive (default True)

Methods:
    die: Set is_alive attribute from True to False
    """

    def __init__(self, first_name: str, is_alive: bool = True):
        """Constructor for abstract class Character"""
        self.first_name = first_name
        self.is_alive = is_alive

    @abstractmethod
    def die(self):
        """Set is_alive attribute from True to False"""
        self.is_alive = False


class Stark(Character):
    """
Stark class

Attributes:
    first_name (str): Stark first_name
    is_alive (bool): Stark is alive (default True)

Methods:
    die: Set is_alive attribute from True to False
    """
    def __init__(self, first_name: str, is_alive: bool = True):
        """Constructor for Stark class"""
        super().__init__(first_name, is_alive)

    def die(self):
        """Set is_alive attribute from True to False"""
        super().die()
