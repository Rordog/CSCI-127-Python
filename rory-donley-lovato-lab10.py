import numpy as np
import random

# -------------------------------------------------
# CSCI 127, Lab 10
# Month __, 20__
# Your Name
# -------------------------------------------------

class Die:

    def __init__(self, sides):
        """A constructor method to create a die"""
        self.sides = sides

    def roll(self):
        """A general method to roll the die"""
        return random.randint(1, self.sides)

# -------------------------------------------------

class Yahtzee:

    def __init__(self, sides):
        """A constructor method that can record 5 dice rolls"""
        self.rolls = np.zeros(5, dtype=np.int16)
        self.sides = sides

    def roll_dice(self):
        """A general method that rolls 5 dice"""
        for i in range(len(self.rolls)):
            self.rolls[i] = Die(self.sides).roll()

    def count_outcomes(self):
        """A helper method that determines how many 1s, 2s, etc. were rolled"""
        counts = np.zeros(self.sides + 1, dtype=np.int16)
        for roll in self.rolls:
            counts[roll] += 1
        return counts

    def is_it_low_roll(self):
        for i in range(3, 9):
            if i in self.rolls:
                return False
        return True
        
    
    def is_it_three_of_a_kind(self):
        outcomes = self.count_outcomes()
        rolls = self.rolls
        for i in range(9):
            if outcomes[i] == 3:
                return True
        return False
    
    def is_it_large_straight(self):
        rolls = self.rolls
        rolls.sort()
        if (rolls[4] - rolls[3] == 1) and (rolls[3] - rolls[2] == 1) and (rolls[2] - rolls[1] == 1) and (rolls[1] - rolls[0] == 1):
            return True
        return False

# -------------------------------------------------
        
def main(how_many):

    low_rolls = 0
    three_of_a_kinds = 0
    large_straights = 0
    game = Yahtzee(8)

    for i in range(how_many):
        game.roll_dice()
        if game.is_it_low_roll():
            low_rolls += 1
        elif game.is_it_three_of_a_kind():
            three_of_a_kinds += 1
        elif game.is_it_large_straight():
            large_straights += 1

    print("Number of Rolls:", how_many)
    print("---------------------")
    
    print("Number of Low Rolls:", low_rolls)
    print("Percent:", "{:.2f}%\n".format(low_rolls * 100 / how_many))
    print("Number of Three of a Kinds:", three_of_a_kinds)
    print("Percent:", "{:.2f}%\n".format(three_of_a_kinds * 100 / how_many))
    print("Number of Large Straights:", large_straights)
    print("Percent:", "{:.2f}%".format(large_straights * 100 / how_many))

# -------------------------------------------------

main(20000)
    
        
