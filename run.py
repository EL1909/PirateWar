""" Import module to order ships on board """
import random


class GameBoard:
    """
    Class to create Board instances
    """
    def __init__(self, board):
        self.board = board

    def print_board(self):
        """
        Print board we will use for the game,
        starting with one row one and loop
        """
        print("  " + " ".join(chr(65 + i) for i in range(len(self.board))))
        print("  " + "- " * len(self.board))
        row_number = 1
        for row in self.board:
            print(f"{row_number}|{':'.join(row)}|")
            row_number += 1
        print("\n")


class BattleShip:
    """ Creates 5 ships to be hidden in the board """
    def __init__(self, board):
        self.board = board

    def create_ships(self):
        """
        Place the ships randomly inside the board
        """
        board_size = len(self.board)
        for _ in range(5):
            while True:
                x_row = random.randint(0, board_size - 1)
                y_column = random.randint(0, board_size - 1)
                if self.board[x_row][y_column] != "X":
                    break
        return self.board

    def get_letter_to_num(self):
        """
        Translates the Input from user into default list numbers.
        """
        ltnm = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6, "H": 7}
        return ltnm

    def get_user_input(self):
        """
        Ask for input and verifies if valid,
        will run until a valid input.
        """
        try:
            while True:
                x_row = input("Choose a row number: \n")
                if x_row.isdigit() and 1 <= int(x_row) <= len(self.board):
                    break
                print('Sharpen your aim!\n\nPlease type a number from 1 to', len(self.board))
            while True:
                y_column = input("Choose a letter, try to find my ship:\n").upper()
                if y_column.isalpha() and 'A' <= y_column <= chr(65 + len(self.board[0]) - 1):
                    break
                print('Sharpen your aim!\n\nType a letter from A to', chr(65 + len(self.board[0]) - 1))
            return int(x_row) - 1, self.get_letter_to_num()[y_column]
        except (ValueError, KeyError):
            print("Not a valid input\n")
            return self.get_user_input()

    def count_hit_ships(self):
        """
        Loop thru the table, if finds an "X" fills the hit_ship variable
        """
        hit_ships = 0
        for row in self.board:
            for column in row:
                if column == "X":
                    hit_ships += 1
        return hit_ships


# Select game difficulty
def choose_difficulty():
    """
    Select game type
    """
    while True:
        difficulty = input('Would you like to play Easy (1) or Hard (2) mode?\n').lower()
        if difficulty == "1":
            return 5
        elif difficulty == "2":
            return 8
        else:
            print('Type 1 or 2 to start the game \n')


# Stablish lenght of the board
def run_game():
    """
    Run Battleship game
    """
    difficulty = choose_difficulty()
    computer_board = GameBoard([[" "] * difficulty for i in range(difficulty)])
    user_guess_board = GameBoard([[" "] * difficulty for i in range(difficulty)])
    battleship = BattleShip(computer_board.board)
    battleship.create_ships()
    turns = 10
    # Start 10 turns, will increment x3 when a ship is hitted
    while turns > 0:
        user_guess_board.print_board()
        user_x_row, user_y_column = battleship.get_user_input()
        guess = user_guess_board.board[user_x_row][user_y_column]
        # Check if space is already hitted
        while guess == "-" or guess == "X":
            print("You shooted that one already\n")
            user_x_row, user_y_column = battleship.get_user_input()
            guess = user_guess_board.board[user_x_row][user_y_column]
        # Check for hit or miss
        if computer_board.board[user_x_row][user_y_column] == "X":
            print("You sunk one of the Pirates!\n")
            turns += 3
            user_guess_board.board[user_x_row][user_y_column] = "X"
        else:
            print("The Pirates just ran away!\n")
            user_guess_board.board[user_x_row][user_y_column] = "-"
        # Check for win or lose
        if BattleShip.count_hit_ships(user_guess_board) == 5:
            print("You hit them all!! Pirates menace is gone!\n\n    WINNER\n")
            break
        else:
            turns -= 1
            print(f"You have {turns} Cannon balls remaining\n")
            if turns == 0:
                print("Sorry you ran out of balls\n\n    GAME OVER\n")
                GameBoard.print_board(user_guess_board)
                break


run_game()
