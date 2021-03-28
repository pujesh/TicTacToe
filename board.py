def display_board(pos_board, game_board):
    border = "-------------"
    pos = 0
    print(border + '\t' + border)
    for i in pos_board:
        line_pos = ''
        line_game = ''
        for j in i:
            line_pos += ('| ' + str(j) + ' ')
            line_game += ('| ' + game_board[pos] + ' ')
            pos += 1
        print(line_pos + '|' + '\t' + line_game + '|')
        print(border + '\t' + border)


def update_board(pos_board, game_board, n, mark):
    for first_key, i in enumerate(pos_board):
        for second_key, j in enumerate(i):
            if j == n:
                pos_board[first_key][second_key] = ' '
    game_board[n-1] = mark
    return pos_board, game_board


def cross_board(game_board, move):
    if move in ((0,1,2), (3,4,5), (6,7,8)):
        game_board[move[0]] = game_board[move[1]] = game_board[move[2]] = '-'
    elif move in ((0,3,6), (1,4,7), (2,5,8)):
        game_board[move[0]] = game_board[move[1]] = game_board[move[2]] = '|'
    elif move == (0,4,8):
        game_board[move[0]] = game_board[move[1]] = game_board[move[2]] = '\\'
    else:
        game_board[move[0]] = game_board[move[1]] = game_board[move[2]]\
            = '/'
    return game_board