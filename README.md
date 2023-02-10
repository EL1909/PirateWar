# PIRATE WAR (Battleship)

Pirate War (Battleship) is a Python terminal game. The game runs using the Code
Institute mock terminal on Heroku.

This game is inspired on the classic BattleShip game; more information on the game can be better explain and found on it's [wikipedia site](https://en.wikipedia.org/wiki/Battleship_(game))

For this version i built a 8 x 8 board, and the player must find and destroy the 5 Pirate ships randomly hidden. The game have not dificult levels because the setup of the ships is random.

## How to Play
1. The purpose of the game is to destroy 5 ships hidden on the 8 x 8 Board.
2. Then, must select two values from a Column of with numbers (1-8) and a row with letter (A-H).
3. The user have 10 trys (Cannon Balls) to start.
4. If the user Destroy the ship, 3 Cannon Balls will be added to the stock.
5. In order to WIN the player must find all 5 ships before he ran out of Cannon Balls.

## Features

- Pirate ships are randomly placed on the board.
- Theres a Header and column to easily identify where to shoot.
- The player can't see where the ships are unless they're destroyed.
- The user have a counter to be aware of how many turns left remain.

- Accepts user inputs
- The input data is validated and check for errors
    - First input only accepts numbers from 1 to 8.
    - Second input only accepts letters from A to H and Uppercase them to match the code validation.
    - If there's an error the input will be required again.
    - The same guess can not be entered twice.


### Future Features

- Add difficulty levels by increasing the ships or shoot number.
- Add diferent types of ships, with more than one space.
- Improvements in design and sounds. 

## Data Model

I wrote the code using two classes. The first one for the board and its frame.

The second class for the ship's behavior, 3 methods to randomly set up the position on the board, determine and verifies the users input and identifies if the selected space was already chosen.

The runGame function starts the game, stablishing the lenght of the board.
Then sets 10 turns to begin, will increment x3 when a ship is hitted.

## Testing

I have manually ...
- Passed the code through a PEP8 linter and confirmed there are no errors.
- Gave invalid and repeated inputs.
- Tested in my local terminal, and the code Institute heroku terminal too.

## Bugs

- When i wrote the code, i was getting errors in the PEP8 linter, some for missing sapcing and also too long strings; therefore i used short variables to replace long name.
- There are no remainig bugs im aware of.


