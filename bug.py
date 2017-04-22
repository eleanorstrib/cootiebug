
import random

from bug_data import rules


def start_selection():
    user_input = input("Type 'rules' for info or 'play' to get started > ")
    return user_input

def manager(start_selection):
    user_input = start_selection()
    if user_input.lower() == 'rules':
        for item in rules:
            print(item)
        start_selection()
    elif user_input.lower() == 'play':
        start_selection()
    else:
        print("Did not understand your command.")
        start_selection()

# user types rules, print in console from bud_data

# user types play, generate a random number for them, then the computer
# compare the numbers
# instantiate the bug class for each

# determine



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

if __name__== '__main__':
    print("\U0001F41B  " * 10, " * Welcome to CootieBug * ", "\U0001F41B  " * 10, )
    manager(start_selection)

main()
