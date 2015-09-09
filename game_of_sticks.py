# This is the Game of Sticks program for Execisize 06 - The Iron Yard
import re
import random

def art_intel_lookup(sticks):
    '''
    #TODO:  need a dictionary with a KEY associated with the number of sticks (1 to 10)
            The associated values are initially populated with [1,2,3].
            At each turn, a random number from 1-3 is selected.
            The number of sticks will be noted at each selection:
            If AI wins, the selection number will be added to the list (value)
            associated with the number of sticks at the time (key)
    of
    '''
    initial_ai_dict =       {
                            1:[1, 2, 3], 2:[1, 2, 3], 3:[1, 2, 3], 4:[1, 2, 3],
                            5:[1, 2, 3], 6:[1, 2, 3], 7:[1, 2, 3], 8:[1, 2, 3],
                            9:[1, 2, 3], 10:[1, 2, 3]
                            }

    tracking_ai_dict =      {
                            1:['e'], 2:['e'], 3:['e'], 4:['e'], 5:['e'], 6:['e'],
                            7:['e'], 8:['e'], 9:['e'], 10:['e']
                            }

    '''
    #TODO:  Fucntion takes the stick number when random selection from list associated
            with the stick number (initially 1-3 random selection).
            The selection is appended to the tracking_ai_dict using the key number.
            - random number using numbers in list associated with key (stick number)
            - tracking_ai_dict[stick number].append(selection):
                will append the selection number into appropriate stick bucket.
            - if AI wins, the tracking_ai_dict values will be appended to the
                initial_ai_dict value list.  [removed if AI loses]
            - the random number will be based on the growing or shrinking selection lists.

    '''

def confirm_input(take, min, max):          # confirms stick removal per turn is within range
    if min <= take <= max:
        return True
    print("Can only take between {} and {}. ". format(min, max))
    return False

def starting_stick_parameters(start_stick, low, high):  #keeps starting stick pile within range
    if start_stick > low and start_stick < high:
        return True
    else:
        print("Please select a number of sticks between {} and {}. ". format(low, high))
        return False

def better_starting_stick_parameters(start_stick, low, high):  # forces stick pile within range
    while start_stick < low or start_stick > high:
        print("Please select a number of sticks between {} and {}. ". format(low, high))
        start_stick = int(input("How many sticks do you want? "))
    return start_stick

def main():
    print("\n-- Welcome to the Game of Sticks --\n")
# Current parameters are:
    min = 1
    max = 3
    start_stick = 4     # initial start_stick for function.
    low = 10
    high = 100
    start_stick = better_starting_stick_parameters(start_stick, low, high)

    play1 = 'Player 1'
    play2 = 'Player 2'
    play_list = ('Player 1', play2)
    ATM = 0 # This is the ON switch for the AI player as player 2.
# Core game_play:
    while start_stick > 0:
        for p in range(len(play_list)):
            print("     There are {} sticks on the board.\n". format(start_stick))
            print("     Take away between {} to {} sticks\n". format(min, max))
            print("{}:". format(play_list[p]))
#            if ATM = 1:
#                ### function
#            else:
#                continue
            take = int(input("  Selection:  "))
            while confirm_input(take, min, max) == False:
                take = int(input("  Try another Selection:  "))
            start_stick = start_stick - take
            if start_stick == 0:
                break
    print("{} loses! - Play again". format(play_list[p]))


if __name__ == '__main__':
    main()
