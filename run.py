# import module random to place order of ships on the table
import random

"""
simple board with columns and rows, computer has placed 
5 hidden shios and we have 10 turns to guess
it will show a - when missed or X when hit a ship
"""


class GameBoard:
    def __init__(self, board):
        self.board = board
#  translates the Input from user into default list numbers. 
    def get_letters_to_numbers():
        letters_to_numbers = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6, "H": 7}
        return letters_to_numbers

# Print the board we will use for the game, starting row one and loop
    def print_board(self):
        print(" A B C D E F G H ")
        print(" +-+-+-+-+-+-+-+ ")
        row_number = 1
        for row in self.board:
            print("%d|%s|" % (row_number, " ".join(row)))
            row_number += 1
            
# Creates 5 ships to be hidden in the board
class Battleship:
    def __init__(self, board):
        self.board = board

    def create_ship(self):
        for i in range(5):
            self.x_row, self.y_column = random.randint(0, 7), random.randint(0, 7)
            while self.board[self.x_row][self.y_column] == "X":
                self.x_row, self.y_column = random.randint(0,7), random.randint(0, 7)
            self.board[self.x_row][self.y_column] = "X"
        return self.board

 # ask for inpur and verifis the data type, will run until true
    def get_user_input(self):
        try:
            x_row = input("Enter the row of the ship: ")
            while x_row not in '12345678':
                print('Not an appropiate choice, please select a valid row')
                x_row = input("Enter the row of the ship: ")

            y_column = input("Enter the column letter of the ship: ").upper()
            while y_column not in "ABCDEFGH":
                print('Not an appropiate choice, please select a valid column')
                y_column = input("Enter the column letter of the ship: ").upper()
            return int(x_row) - 1, GameBoard.get_letters_to_numbers()[y_column]
        except ValueError and KeyError:
            print("Not a valid input")
            return self.get_user_input()


GameBoard()
print(GameBoard)