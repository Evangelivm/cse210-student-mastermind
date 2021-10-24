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
        self.player = []
        self.number_1 = []
        self.number_2 = []
        self.answer_1 = ["-","-","-","-"]
        self.answer_2 = ["-","-","-","-"]
    def players(self,names):
        self.player.append(names)
    def apply(self):
        pass
    def is_empty(self):
        if self.answer_1 == self.number_1:
            return False
        elif self.answer_2 == self.number_2:
            return False
        elif self.answer_1 != self.number_1:
            for n in range (4):
                if self.answer_1[n] in self.number_1:
                    if self.answer_1[n] == self.number_1:
                        self.question_1[n] = "o"
                    else:
                        self.question_1[n] = 'x'
                else:
                    self.question_1[n] = "*"
            n = n + 1
        elif self.answer_2 != self.number_2:
            for n in range (4):
                if self.answer_2[n] in self.number_2:
                    if self.answer_2[n] == self.number_2:
                        self.question_2[n] = "o"
                    else:
                        self.question_2[n] = 'x'
                else:
                    self.question_2[n] = "*"
            n = n + 1
    def to_string(self):
        self.question_1 = ["*","*","*",'*']
        self.question_2 = ["*","*","*",'*']
        board = f"\n--------------------\
\nPlayer {self.player [0]}: ----, {self.question_1[0]}{self.question_1[1]}{self.question_1[2]}{self.question_1[3]}\
\nPlayer {self.player [1]}: ----, {self.question_2[0]}{self.question_2[1]}{self.question_2[2]}{self.question_2[3]}\
\n--------------------"
        return board
    def random(self):
        self.number_one = str(random. randint(1000,9999))
        self.number_1.append(self.number_one)
        self.number_two = str(random. randint(1000,9999))
        self.number_2.append(self.number_two)
