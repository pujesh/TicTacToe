from check import check_position, check_result
from board import update_board, display_board

def user_interact(pone):
    turn = 0
    game = False
    pos_board = [[1,2,3], [4,5,6], [7,8,9]]
    game_board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    if pone == 'X':
        ptwo = 'O'
    else:
        ptwo = 'X'

    while turn < 9 and game == False:
        player = (1 if ((turn+1) % 2 != 0) else 2)
        while True:
            pos = input("Player {} to pick a position: ".format(player))
            if pos.isnumeric() and pos != '\n':
                pos = int(pos)
                if pos in range(1, 10):
                    pos_check = check_position(pos_board, pos)
                    if not pos_check:
                        break
                    else:
                        print("Oops! the chosen position is already filled. Please choose another position!")
                else:
                    print("Please enter a number seen in the board! ")
            else:
                print("Please enter a number seen in the board! ")

        turn += 1
        mark = (pone if player == 1 else ptwo)
        pos_board, game_board = update_board(pos_board, game_board, pos, mark)
        display_board(pos_board, game_board)
        if turn >= 4:
            game, game_board = check_result(game_board)
            if game:
                print('#####################################')
                display_board(pos_board, game_board)
                print("We have a winner and the winner is: Player {}".format(player))
                print('#####################################')

    if not game:
        print("Looks like we ended a game in a draw!")