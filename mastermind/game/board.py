import random

class Board:
    """A code template for a person who directs the game. The responsibility of 
    this class of objects is to control the sequence of play.
    
    Stereotype:
        Controller

    Attributes:
        board (Hunter): An instance of the class of objects known as Board.
        console (Console): An instance of the class of objects known as Console.
        keep_playing (boolean): Whether or not the game can continue.
        move (Rabbit): An instance of the class of objects known as Move.
        roster (Roster): An instance of the class of objects known as Roster.
    """
    def __init__(self):
        self.called_piles = []
    def apply(self):
        pass
    def is_empty(self):
        if sum(self.stones) == 0:
            return True
        else:
            return False
    def to_string(self):
        self.piles = 0
        self.stones = []
    def _prepare(self):
        piles = random. randint(2,5)
        self.called_piles.append(piles)
        for x in range(piles):
            print(f"{x}: ",end =" ")
            x = x + 1
            for x in range(random. randint(1,9)):
                print(f"O ",end =" ")
            print("",end = None)