

def main():
    print ("Welcome to the Game of Sticks!")
    sticks = get_number_of_sticks()

    cur_player = 1

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

if __name__ == '__main__':
    main()
