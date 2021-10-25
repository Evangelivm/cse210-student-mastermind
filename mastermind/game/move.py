class Move:
    """A maneuver in the game. The responsibility of Move is to keep track of the numbers.
    
    Stereotype: 
        Information Holder

    Attributes:
        _number (integer): The number to remove from.
    """
    def __init__(self, number):
        """The class constructor.
        
        Args:
            self (Board): an instance of Board.
        """
        self._number = number

    def get_number(self):
        """Returns the number to remove from.

        Args:
            self (Move): an instance of Move.
        """
        return str(self._number)

