import random
'''
We need a dictionary of Lists
'''


def main():
    hats = {key: [1, 2, 3] for key in range(1, 101)}
    # hats[1].remove(2)  vs hats[1].append(2)
    # does not have to be set-up dynamically with num of sticks
    # because it is a sliding scale against a max of 100 + 1.

    print ("Welcome to the Game of Sticks!")
    while True:
        # outer loop to play again.
        ai_game = is_ai_game()
        sticks = get_number_of_sticks()

        cur_player = 1

        if not ai_game:   # Human vs Human
            while True:
                print("There are {} sticks on the board.".format(sticks))
                sticks -= sticks_out(cur_player)
                if is_game_over(sticks) == True:
                    break
                if cur_player == 1:
                    cur_player = 2
                else:
                    cur_player = 1
            # cur_player = 1 if cur_player == 2 else 2  # list comprehension
            print("Player {}, you lose.".format(cur_player))

        else:           # Human vs AI
            beside = {}

            while True:
                print("There are {} sticks on the board.".format(sticks))
                sticks -= sticks_out(cur_player)
                if is_game_over(sticks) == True:
                    print("Player 1, you lose.")
                    learn_from_win(hats, beside)
                    break

                ai_sticks = pick_ai_sticks(hats, beside, sticks)
                print("AI selects {}.".format(ai_sticks))

                sticks -= ai_sticks

                if is_game_over(sticks):
                    print("AI loses.")
                    learn_from_loss(hats, beside)
                    break

            for i in range(1, 11):
                print(hats[i])

        if check_play_again() == True:
            continue
        else:
            # print("Thanks for playing. \n   Bye!")
            break


def check_play_again():
    choice = input('Play again? (Y/n)')
    if choice != 'n':
        return True
    else:
        return False


def is_ai_game():
    choice = int(input("""
Options:
 Play against a friend(1)
 Play agianst the computer(2)
Which option do you take (1-2)? """))
    # TODO; input validation
    if choice == 2:
        return True
    else:
        return False


def learn_from_win(hats, beside):
    for key in beside:
        hats[key].append(beside[key])


def learn_from_loss(hats, beside):
    for key in beside:
        if hats[key].count(beside[key]) > 1:  # if more than 1, remove 1
            hats[key].remove(beside[key])


def pick_ai_sticks(hats, beside, num_sticks):
    sticks = random.choice(hats[num_sticks])  # random selection at num_sticks

    beside[num_sticks] = sticks  # adds key (num_sticks) + sticks to beside{}.
    return sticks


def is_game_over(num_sticks):
    if num_sticks <= 0:
        return True
    else:
        return False


def get_number_of_sticks():
    # TODO; validate number entered
    sticks = int(input("How many sticks (10-100?)? "))
    return sticks


def sticks_out(cur_player):
    # TODO; validate number entered
    return int(input("Player {}: How many sticks to take (1-3)? ".format(cur_player)))


def make_dict(sticks):   # 2 variables
    ai_dict = {}
    for i in range(sticks):
        ai_dict = ai_dict[i], [1, 2, 3]
'''
for each stick, create an entry of dict{ i: [1, 2, 3], i: [1, 2, 3]}
'''

if __name__ == '__main__':
    main()
