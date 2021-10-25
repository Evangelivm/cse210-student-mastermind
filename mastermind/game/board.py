import random

class Board:
    """A code template for the Board. The responsibility is to create and update the table, in addition to verifying the results.
    
    Stereotype:
        Information Holder

    Attributes:
        player (List): The list of players.
        number_1 (String): A randomly chosen number for player 1.
        number_2 (String): A randomly chosen number for player 2.
        answer_1 (List): The number chosen by the player 1.
        answer_2 (List): The number chosen by the player 2.
        question_1 (List): Player 1's signs to check his answer.
        question_2 (List): Player 2's signs to check his answer
    """
    def __init__(self):
        """The class constructor.
        
        Args:
            self (Player): an instance of Player.
        """
        self.player = []
        self.number_1 = []
        self.number_2 = []
        self.answer_1 = ["-","-","-","-"]
        self.answer_2 = ["-","-","-","-"]
        self.question_1 = ["*","*","*",'*']
        self.question_2 = ["*","*","*",'*']
    def players(self,names):
        """Add the names of the players.
        
        Args:
            self (Director): an instance of Director.
            names (String): the name of the player.
        """
        self.player.append(names)
    def apply(self, move, player):
        """Add the names of the players.
        
        Args:
            self (Director): an instance of Director.
            move (String): the number of the player.
            player (String): the name of the player.
        """
        if player == self.player[0]:
            list_player = list(str(move))
            self.answer_1 = list_player 
        else:
            list_player = list(str(move))
            self.answer_2 = list_player 
    def is_empty(self):
        """Verify the answer of each player.
        
        Args:
            self (Director): an instance of Director.
        """
        if self.answer_1 == self.number_1:
            return False
        elif self.answer_2 == self.number_2:
            return False
        if self.answer_1 != self.number_1:
            for n in range (4):
                if self.answer_1[n] in self.number_1:
                    if self.answer_1[n] == self.number_1[n]:
                        self.question_1[n] = "o"
                    else:
                        self.question_1[n] = 'x'
                else:
                    self.question_1[n] = "*"
            n = n + 1
        if self.answer_2 != self.number_2:
            for n in range (4):
                if self.answer_2[n] in self.number_2:
                    if self.answer_2[n] == self.number_2[n]:
                        self.question_2[n] = "o"
                    else:
                        self.question_2[n] = 'x'
                else:
                    self.question_2[n] = "*"
            n = n + 1
    def to_string(self):
        """Create the board.
        
        Args:
            self (Director): an instance of Director.
        """
        board = f"\n--------------------\
\nPlayer {self.player [0]}: {self.answer_1[0]}{self.answer_1[1]}{self.answer_1[2]}{self.answer_1[3]}, {self.question_1[0]}{self.question_1[1]}{self.question_1[2]}{self.question_1[3]}\
\nPlayer {self.player [1]}: {self.answer_2[0]}{self.answer_2[1]}{self.answer_2[2]}{self.answer_2[3]}, {self.question_2[0]}{self.question_2[1]}{self.question_2[2]}{self.question_2[3]}\
\n--------------------"
        return board
    def random(self):
        """Decide the correct answer of each player.
        
        Args:
            self (Director): an instance of Director.
        """
        self.number_one = list(str(random. randint(1000,9999)))
        self.number_1 = self.number_one 
        self.number_two = list(str(random. randint(1000,9999)))
        self.number_2 = self.number_two
