class Move:
    """A maneuver in the game. The responsibility of Move is to keep track of the stones to remove and which pile to remove them from.
    
    Stereotype: 
        Information Holder

    Attributes:
        _pile (integer): The pile to remove from.
    """
    def __init__(self, pile):
        """The class constructor.
        
        Args:
            self (Board): an instance of Board.
        """
        self._pile = pile

    def get_pile(self):
        """Returns the pile to remove from.

        Args:
            self (Move): an instance of Move.
        """
        return str(self._pile)

