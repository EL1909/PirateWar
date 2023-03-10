# import module random to place the ships on the table
import random

"""
I create the board using a class
Computer will place 5 ships randomly and we'll have 10 turns to find them
Everytime you hit a ship you'll have 3 extra shots
The board will show a - when missed or X when you hit a ship
"""


class GameBoard:
    def __init__(self, board):
        self.board = board

# Translates the Input from user into default list numbers.
    def get_lett_to_num():
        ltnm = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6, "H": 7}
        return ltnm

# Print the board we will use for the game, starting with one row one and loop
    def print_board(self):
        print("  A B C D E F G H ")
        print("  +-+-+-+-+-+-+-+ ")
        row_number = 1
        for row in self.board:
            print("%d|%s|" % (row_number, ":".join(row)))
            row_number += 1


# Creates 5 ships to be hidden in the board
class Battleship:
    def __init__(self, board):
        self.board = board

# Place the ships randomly inide our board
    def create_ships(self):
        for i in range(5):
            self.x_row, self.y_column = random.randint(0, 7), random.randint(0, 7)
            while self.board[self.x_row][self.y_column] == "X":
                self.x_row, self.y_column = random.randint(0, 7), random.randint(0, 7)
            self.board[self.x_row][self.y_column] = "X"
        return self.board

# Ask for input and verifies if valid, will run until a valid input
    def get_user_input(self):
        try:
            x_row = input("Choose a row number: \n")
            while x_row not in '12345678':
                print('Not an number, please select 1 to 8\n')
                x_row = input("Enter the row number:\n")

            y_column = input("Choose a letter, try to find my ship:\n").upper()
            while y_column not in "ABCDEFGH":
                print('Sharpen your aim, please select a column LETTER\n')
                y_column = input("Enter the column letter: \n").upper()
            return int(x_row) - 1, GameBoard.get_lett_to_num()[y_column]
        except ValueError and KeyError:
            print("Not a valid input\n")
            return self.get_user_input()

# Runs loop thru the table and when finds an "X" fills the hit_ship variable
    def count_hit_ships(self):
        hit_ships = 0
        for row in self.board:
            for column in row:
                if column == "X":
                    hit_ships += 1
        return hit_ships


# Stablish lenght of the board
def RunGame():
    computer_board = GameBoard([[" "] * 8 for i in range(8)])
    user_guess_board = GameBoard([[" "] * 8 for i in range(8)])
    Battleship.create_ships(computer_board)
    # Start 10 turns, will increment x3 when a ship is hitted
    turns = 10
    while turns > 0:
        GameBoard.print_board(user_guess_board)
        # Get user input
        user_x_row, user_y_column = Battleship.get_user_input(object)
        # Check if space is already hitted
        guess = user_guess_board.board[user_x_row][user_y_column]
        while guess == "-" or guess == "X":
            print("You shooted that one already\n")
            user_x_row, user_y_column = Battleship.get_user_input(object)
        # Check for hit or miss
        if computer_board.board[user_x_row][user_y_column] == "X":
            print("You sunk one of the Pirates!\n")
            turns += 3
            user_guess_board.board[user_x_row][user_y_column] = "X"
        else:
            print("The Pirates just ran away!\n")
            user_guess_board.board[user_x_row][user_y_column] = "-"
        # Check for win or lose
        if Battleship.count_hit_ships(user_guess_board) == 5:
            print("You hit them all!! Pirates menace is gone!\n\n    WINNER\n")
            break
        else:
            turns -= 1
            print(f"You have {turns} Cannon balls remaining\n")
            if turns == 0:
                print("Sorry you ran out of balls\n\n    GAME OVER\n")
                GameBoard.print_board(user_guess_board)
                break


__name__ == '__main__'
RunGame()
