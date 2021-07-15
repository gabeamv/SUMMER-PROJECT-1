# Project 2, Tic Tac Toe

# import modules
import random

# List to represent tic tac toe board.
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]


# Function to display board.
def display_board():
    # Display board.
    print(" | " + board[0] + " | " + board[1] + " | " + board[2] + " | ")
    print(" | " + board[3] + " | " + board[4] + " | " + board[5] + " | ")
    print(" | " + board[6] + " | " + board[7] + " | " + board[8] + " | ")


# Function to play game. (calls other functions to operate the game properly).
def play_game():
    # Display the board.
    display_board()
    print()

    # Variables to represent the computer and the user (holds X or O).
    userPlayer = ""
    compPlayer = ""

    # Variables to represent the turns of user and computer.
    userTurn = True
    compTurn = True

    # Call first to determine who goes first, user or computer. Player is either X or O.
    player = determine_letter()

    # Determine player O (who goes second).
    # If player is X.
    if player == "X":
        # Assign letters to the players
        compPlayer = "O"
        userPlayer = "X"

    # If player is O.
    if player == "O":
        # Assign letter to the players.
        compPlayer = "X"
        userPlayer = "O"

    # Variables to represent the turn of user and computer. (True if it is their turn, False if it is not their turn.
    # If compPlayer is O and userPlayer is X.
    if (compPlayer == "O") and (userPlayer == "X"):
        # userTurn is True and compPlayer is False (user goes first).
        userTurn = True
        compTurn = False

    # If compPlayer is X and userPlayer is O.
    if (compPlayer == "X") and (userPlayer == "O"):
        # userTurn is False and compPlayer is True (computer goes first).
        userTurn = False
        compTurn = True

    # Variable gameOver that calls check_win to hold for a false value until the game has a winner.
    gameOver = check_win(board, userPlayer, compPlayer)
    tie = False

    # Loop to run until there is a winner or a tie.
    while not gameOver:

        # Variable that calls get_position to get position on the board.
        position = get_position(userTurn, compTurn)

        # Mark the board by calling the function mark_board
        # which takes in the boolean values of userTurn and compTurn,
        # str values of X and O for userPlayer and compPlayer, and
        # the int value which represents the position of the board.
        mark_board(userTurn, compTurn, userPlayer, compPlayer, position)

        # Display the board.
        display_board()
        print()

        # Check for win (return True or False).
        gameOver = check_win(board, userPlayer, compPlayer)

        # Check for a tie.
        tie = check_tie(board)

        # If tie is True print there is a tie a break from loop.
        if tie:
            # Set game over to true and break.
            gameOver = True
            break

        # When there is no winner, call the flip_turn function to switch the userTurn and compTurn values.
        userTurn = flip_turn(userTurn)
        compTurn = flip_turn(compTurn)

    print("Thank you for playing!")
    print()


# unction to generate a random number to determine who gets  "X" or "O", (return X or O)
def determine_letter():
    # Tell user it the game is determining who goes first.
    print("Determining who goes first...")
    print()

    # Generate a random number from 1-100.
    turn = random.randint(1, 100)

    # Determine if even or odd.

    # If even, return "X" and display the type of player (X or O).
    if turn % 2 == 0:
        print("User is X. Computer is O. User goes first.")
        print()
        return "X"

    # If odd return "O".
    else:
        print("Computer is X. User is O. Computer goes first.")
        print()
        return "O"


# Function to switch the turn of computer and user (if true return false, if false return true).
def flip_turn(player):
    # If user/comp is True (X), return False (O turn).
    if player:
        return False

    # If user/comp False (O) return True (X turn)
    else:
        return True


# Function for user to input a position, also calls validate_position \
# to validate the input/position (returns the position of computer or user)
def get_position(userTurn, computerTurn):
    # Variable position to represent user input.
    position = ""

    # If userTurn is true, let user input position.
    if userTurn:

        # Variable for user to input enter to continue the process.
        prompt = input("It is your turn. Please press enter to continue.")
        print()

        # Variable valid to initialize loop. Loop ends when true (when valid input is inputed).
        valid = False

        # Loop to run while valid is false to check the validity of user input.
        while not valid:

            # Prompt user to input a position.
            position = input("Please enter a valid position from 1-9: ")
            print()

            # While number not in range from 1-9, user input new number 1-9.
            while not ("1" <= position <= "9"):
                position = input("Please enter a valid position from 1-9: ")
                print()

            # Convert position to integer.
            position = int(position)

            # Check validity on the board, call validate_position.
            valid = validate_position(position)

            # Print what user chose.
            print("You have chosen position", position, end=".\n")
            print()

        # Return position
        return position

    # If computerTurn is true, let computer get a random position from 1-9.
    elif computerTurn:

        # Variable for user to input enter to continue the process.
        prompt = input("It is the computer's turn. Please press enter to continue.")
        print()
        prompt = input("Generating the computer's choice...")
        print()

        # Variable valid to initialize loop. Loop ends when computer picks a valid position on the board.
        valid = False

        # While number is not a valid number.
        while not valid:
            # Computer generates a random number/position.
            position = random.randint(1, 9)

            # Check validity, call validate_position.
            valid = validate_position(position)

        # Print what the computer chooses.
        print("The computer chooses position", position, end=".\n")
        print()

        # Return position.
        return position


# Function to check if anybody won. (horizontal, vertical, diagonal).
def check_win(currentBoard, userPlayerSign, compPlayerSign):
    # Variable to become true when there is a win.
    win = False

    # Check user wins.
    # Check top horizontal.
    if (((currentBoard[0] == userPlayerSign) and (currentBoard[1] == userPlayerSign) and
         (currentBoard[2] == userPlayerSign)) or
            # Check middle horizontal.
            ((currentBoard[3] == userPlayerSign) and (currentBoard[4] == userPlayerSign) and
             (currentBoard[5] == userPlayerSign)) or
            # Check bottom horizontal.
            ((currentBoard[6] == userPlayerSign) and (currentBoard[7] == userPlayerSign) and
             (currentBoard[8] == userPlayerSign)) or
            # Check left vertical.
            ((currentBoard[0] == userPlayerSign) and (currentBoard[3] == userPlayerSign)
             and (currentBoard[6] == userPlayerSign)) or
            # Check middle vertical.
            ((currentBoard[1] == userPlayerSign) and (currentBoard[4] == userPlayerSign)
             and (currentBoard[7] == userPlayerSign)) or
            # Check right vertical.
            ((currentBoard[2] == userPlayerSign) and (currentBoard[5] == userPlayerSign)
             and (currentBoard[8] == userPlayerSign)) or
            # Check left diagonal.
            ((currentBoard[0] == userPlayerSign) and (currentBoard[4] == userPlayerSign)
             and (currentBoard[8] == userPlayerSign)) or
            # Check right diagonal.
            ((currentBoard[2] == userPlayerSign) and (currentBoard[4] == userPlayerSign)
             and (currentBoard[6] == userPlayerSign))):
        # Print congratulations and set win to true and return win.
        print(userPlayerSign, "has won.")
        print("Congratulations! You have won Tic-Tac-Toe!")
        print()

        win = True
        return win

    # Check computer wins.
    # Check top horizontal.
    if (((currentBoard[0] == compPlayerSign) and (currentBoard[1] == compPlayerSign) and
         (currentBoard[2] == compPlayerSign)) or
            # Check middle horizontal.
            ((currentBoard[3] == compPlayerSign) and (currentBoard[4] == compPlayerSign) and
             (currentBoard[5] == compPlayerSign)) or
            # Check bottom horizontal.
            ((currentBoard[6] == compPlayerSign) and (currentBoard[7] == compPlayerSign) and
             (currentBoard[8] == compPlayerSign)) or
            # Check left vertical.
            ((currentBoard[0] == compPlayerSign) and (currentBoard[3] == compPlayerSign)
             and (currentBoard[6] == compPlayerSign)) or
            # Check middle vertical.
            ((currentBoard[1] == compPlayerSign) and (currentBoard[4] == compPlayerSign)
             and (currentBoard[7] == compPlayerSign)) or
            # Check right vertical.
            ((currentBoard[2] == compPlayerSign) and (currentBoard[5] == compPlayerSign)
             and (currentBoard[8] == compPlayerSign)) or
            # Check left diagonal.
            ((currentBoard[0] == compPlayerSign) and (currentBoard[4] == compPlayerSign)
             and (currentBoard[8] == compPlayerSign)) or
            # Check right diagonal.
            ((currentBoard[2] == compPlayerSign) and (currentBoard[4] == compPlayerSign)
             and (currentBoard[6] == compPlayerSign))):
        # Print the computer has won and set win to true and return win.
        print(compPlayerSign, "has won.")
        print("The computer has won Tic-Tac-Toe. Try again next time.")
        print()

        win = True
        return win


# Function to validate if the user or computer can secure a position on the board \
# (checks if a space is already taken or not, returns True or False).
def validate_position(position):
    # Subtract one from the position to represent the index of the list called board.
    position -= 1

    # Determine if the position is free on the board.
    if board[position] == "-":

        # Return True
        return True

    # If anything besides "-" in board[position].
    else:

        # Return False
        return False


# Function to mark the board.
# Determines whether to mark X or O on the board and has a parameter
# that takes in the position, and parameters that take in the the sign of the player.
def mark_board(userTurn, compTurn, userPlayerSign, compPlayerSign, position):
    # Subtract position by one to represent the index in the list called board.
    position -= 1

    # If it is the users turn.
    if userTurn:
        # Update the board.
        board[position] = userPlayerSign

    # If it is the computer's turn.
    if compTurn:
        # Update the board.
        board[position] = compPlayerSign


# Function to check if there is a tie. Parameter to hold for the current state of the board (takes in the list).
# Returns True or False
def check_tie(currentBoard):
    # Variable "tie" to hold for boolean value of False. Becomes True when there is a tie on the board.
    tie = False

    # Loop to check if there is yet to be a position taken yet from the board.
    for position in currentBoard:

        # If a position has not been taken yet.
        if position == "-":
            # There is no tie yet, so return tie as False.
            return tie

    # When currentBoard passes the loop to check if there is no more spaces to hold a position,
    # set tie as True and return it, print there is a tie.
    tie = True
    print("There is a tie.")
    print()
    return tie


# Main function
def main():
    # Print welcome.
    print("Welcome to Tic-Tac-Toe!")
    print()

    # Variable playAgain to hold for "y" to initialize the while loop.
    playAgain = "y"

    # While playAgain is True.
    while playAgain == "y" or playAgain == "Y":
        # Call play_game.
        play_game()

        # Reset the board.
        global board
        board = ["-", "-", "-",
                 "-", "-", "-",
                 "-", "-", "-"]

        # Ask user if the would want to play again
        playAgain = input("Would you like to play again? (Enter y or Y to play again, anything else will exit)")
        print()

    # Print goodbye.
    print("Goodbye! Hope you play again!")


# Call main to run.
main()
