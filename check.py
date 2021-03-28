from board import cross_board

def check_position(board, n):
    for i in board:
        for j in i:
            if j == n:
                return False
    return True


def check_result(game_board):
    moves = (
        (0,1,2), (3,4,5), (6,7,8),
        (0,3,6), (1,4,7), (2,5,8),
        (0,4,8), (2,4,6)
    )

    for i in moves:
        if game_board[i[0]] != ' ' and game_board[i[1]] != ' ' and game_board[i[2]] != ' ':
            if game_board[i[0]] == game_board[i[1]] == game_board[i[2]]:
                # game_board = cross_board(game_board, i, dims)
                game_board = cross_board(game_board, i)
                return True, game_board
        else:
            continue

    return False, game_board