
from random import randint
from threading import Timer

from bug_data import rules



def say_hello():
    user_name = input("What's your name? > ")
    return user_name

def start_selection():
    user_input = input("Type 'rules' for info or 'play' to get started > ")
    return user_input

def manager(start_selection):
    user_name = say_hello()
    user_input = start_selection()
    if user_input.lower() == 'rules':
        print(rules)
        start_selection()
    elif user_input.lower() == 'play':
        roll_to_start(user_name)
        start_selection()
    else:
        print("Did not understand your command.")
        start_selection()

# user types rules, print in console from bud_data

# user types play, generate a random number for them, then the computer
# compare the numbers
# create player/computer vars to hold scores
# instantiate the bug class for each
# roll the dice, get a number, check


def roll_to_start(user_name):
    print("Rolling the \U0001F3B2  for you, %s" % user_name)
    user_name_result = randint(1,6)
    print("You got %s" % user_name_result)
    print("Now, I'll roll the \U0001F3B2  for me...")
    computer_result = randint(1,6)
    print("I got %s" % computer_result)
    user_is_player_1 = True
    if user_name_result >= computer_result:
        print("Congratulations %s, you're player 1!" % user_name)
        turn(roll_to_start(user_name), user_name)
    else:
        user_is_player_1 = False
    return user_is_player_1

def turn(roll_to_start, user_name):
    if roll_to_start == True:
        print(input("Ok %s, your turn! Type 'roll' to continue" % user_name))



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

if __name__ == "__main__":
    def main():
        print("\U0001F41B  " * 10, " * Welcome to CootieBug * ", "\U0001F41B  " * 10, )
        manager(start_selection)

    main()
