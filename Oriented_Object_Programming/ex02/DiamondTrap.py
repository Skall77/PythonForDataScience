from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """
King class

Attributes:
    first_name (str): King first_name
    is_alive (bool): King is alive (default True)
    family_name (str): King family name
    eyes (str): King eyes color
    hairs (str): King hair color

Methods:
    get_eyes: Return eyes attribute
    get_hairs: Return hairs attribute
    set_eyes: Set eyes attribute
    set_hairs: Set hairs attribute
    """

    def __init__(self, first_name, is_alive=True):
        """Constructor for King class"""
        super().__init__(first_name)

    def get_eyes(self):
        """Return eyes attribute"""
        return self.eyes

    def get_hairs(self):
        """Return hairs attribute"""
        return self.hairs

    def set_eyes(self, eyes):
        """Set eyes attribute"""
        self.eyes = eyes

    def set_hairs(self, hairs):
        """Set hairs attribute"""
        self.hairs = hairs
