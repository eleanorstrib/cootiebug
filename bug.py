
from random import randint
from threading import Timer

from bug_data import rules


user_is_player_1 = False

def say_hello():
    user_name = input("What's your name? > ")
    return user_name

def rules_or_play(name):
    user_input = input(
            "Hi %s! Type 'rules' for info or 'play' to get started > " % name
    )
    return user_input


# user types rules, print in console from bud_data

# user types play, generate a random number for them, then the computer
# compare the numbers
# create player/computer vars to hold scores
# instantiate the bug class for each
# roll the dice, get a number, check


def choose_player_one(user_name):
    print("OK, let's roll the dice to see who goes first...")
    print("Rolling the \U0001F3B2  for you, %s" % user_name)
    user_name_result = randint(1,6)
    print("You got %s" % user_name_result)
    print("Now, I'll roll the \U0001F3B2  for me...")
    computer_result = randint(1,6)
    print("I got %s" % computer_result)

    if user_name_result >= computer_result:
        print("Congratulations %s, you get to go first!" % user_name)
        return True
    else:
        print("Sorry %s, I won the toss, so I'll go first..." % user_name)
        return False

#
# def turn(roll_to_start, user_name):
#     if roll_to_start == True:
#         print(input("Ok %s, your turn! Type 'roll' to continue" % user_name))
#     else:
#         print("Rolling the dice for me...")




# class Bug(object):
#     def __init__(self):
#         self.body = False
#         self.head = False
#         self.hat = False
#         self.eye = False
#         self.mouth = False
#         self.leg = False
#
#     def add_part(self, value):
#         if value == 1:
#             self.body = True
#         if value == 2:
#             self.head = True
#         if value == 3:
#             self.hat = True
#         if value == 4:
#             self.eye = True
#         if value == 5:
#             self.mouth = True
#         if value == 6:
#             self.leg = True

if __name__ == "__main__":
    def main():
        print("\U0001F41B  " * 10, " * Welcome to CootieBug * ", "\U0001F41B  " * 10, )
        user_name = say_hello()
        start = rules_or_play(user_name)
        if start == 'play':
            player_one = choose_player_one(user_name)
            print(player_one)


    main()
