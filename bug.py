# The object of this game is to draw a completed cootie bug before the other players. Provide each player with a piece of paper and a pencil. Players roll a die to complete their bug.
# Every time, the number of dots on the die represents a different body part:
# 1 = body
# 2 = head
# 3 = antennae, hat, or bow
# 4 = eye,
# 5 = tongue, teeth, or lips
# 6 = a leg
# Have each player roll the die and the player with the highest roll goes first.
# A player must start by throwing a one for the body and then a two for the head.
# If a player cannot roll the required numbers, they lose their turn and must try again on their next turn.
# After a player gets the body and head, cootie parts can be added in any order a player desires. However, if a player rolls a number of a cootie body part they already have, their turn is over.
# When a player successfully rolls a needed number, they get a free roll to attempt to get another body part. The winner of the game is the first to finish their cootie.

import random

print("\U0001F41B  " * 10, " * Welcome to CootieBug * ", "\U0001F41B  " * 10, )
print("Type 'rules' for info or 'play' to get started")

# computer vs user
# generate



class Bug(object):
    def __init__(self):
        self.body = False
        self.head = False
        self.hat = False
        self.eye = False
        self.mouth = False
        self.leg = False

    def add_part(self, value):
        if value == 1:
            self.body = True
        if value == 2:
            self.head = True
        if value == 3:
            self.hat = True
        if value == 4:
            self.eye = True
        if value == 5:
            self.mouth = True
        if value == 6:
            self.leg = True
