from board import display_board
from interact import user_interact

def main():
    print("Hello World!")
    print("Welcome to the game of Tic-Tac-Toe!")
    pone_symbol = input("Player 1 to choose (X or O): ")
    print("Let us begin the game!!")
    display_board([[1,2,3], [4,5,6], [7,8,9]], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '])
    user_interact(pone_symbol)

main()


