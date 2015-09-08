# This is the Game of Sticks program for Execisize 06 - The Iron Yard
import re
import random

# def stick_status(sticks, Player1, Player2):
#
# """
#     keeps track of how many sticks are in play.
#     inputs are player identifiers (AI, poeple) and pile start
#     - starting amount
#     - play1 pick
#     - play2 pick
#     -
#
# """
#     # TODO
#     pass
#
# def game_display(arg):
#
#     # TODO
#     pass
#

def confirm_input(take, min, max):
    if min <= take <= max:
        return True
    print("Can only take between {} and {}. ". format(min, max))
    return False

def starting_stick_parameters(start_stick, low, high):
    if low <= start_stick <= high:
        return True
    print("Please select a number of sticks between {} and {}. ". format(low, high))
    return False


def main():
    print("-- Welcome to the Game of Sticks --\n")
# Current parameters are:
    min = 1
    max = 3
    start_stick = 10
    # print("Select the number of sticks between How many sticks? ")
    play1 = 'Player 1'
    play2 = 'Player 2'
    play_list = ('Player 1', 'Player 2')  
# Core game_play:
    while start_stick > 0:
        for p in range(len(play_list)):
            print("     There are {} sticks on the board.\n". format(start_stick))
            print("     Take away between {} and {} sticks\n". format(min, max))
            print("{}:". format(play_list[p]))
            take = int(input("  Selection:  "))
            while start_stick - take < 0:
                take = int(input("  Try another Selection:  "))
            # possible insertion of confirm_input
            start_stick = start_stick - take

    print("{} loses! - Play again". format(play_list[p]))














if __name__ == '__main__':
    main()
