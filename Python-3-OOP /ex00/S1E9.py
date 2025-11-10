from abc import ABC, abstractmethod

class Character(ABC):
    """Abstract class representing a character."""
    @abstractmethod
    def __init__(self, first_name, is_alive = True):
        """Constructor for Character"""
        self.first_name = first_name
        self.is_alive = is_alive
        
    def die(self):
        """Method to change the health state of the character."""
        self.is_alive = False

class Stark(Character):
    """Class representing a Stark Character"""


    def __init__(self, first_name, is_alive=True):
        """Stark character has been constructed"""
        self.first_name = first_name
        self.is_alive = is_alive
