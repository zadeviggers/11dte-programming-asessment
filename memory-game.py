# =================================
# 11DTE Programming asessment: memory game by Zade Viggers is licensed under Attribution-ShareAlike 4.0 International.
# To view a copy of this license, visit http://creativecommons.org/licenses/by-sa/4.0/
# Check the LICENSE.md file for more details.
# =================================

# Memory game!

# Board
#     1   2   3   4
#   ╔═══╦═══╦═══╦═══╗
# 1 ║ # ║ # ║ # ║ # ║
#   ╠═══╬═══╬═══╬═══╣
# 2 ║ # ║ A ║ # ║ # ║
#   ╠═══╬═══╬═══╬═══╣
# 3 ║ # ║ # ║ # ║ # ║
#   ╠═══╬═══╬═══╬═══╣
# 4 ║ # ║ # ║ # ║ A ║
#   ╚═══╩═══╩═══╩═══╝

import random
import time


# Constants
#EMOJIS = ["😳","😂","😎","😍","😛","😭","🥵","🥶","🤡","🥳","🤢","👺","👻","☠","👽","👾","🤖","💩","🙉","🙀","🦄","🐲","🐳","🦆","👀","👌","👏","👋","🎃","🎉","💎","🔊","🔒","⌛","🍫","🍕","🍖","🚗","🚂"]
CHARACTERS = ["A","B","C","D","E","F","G","H","I","J", "K","L","M","N","O","P","P","Q","R", "S", "T","U","V","W", "X", "Y","Z"]
DEFAULT_BOARD_SIZE = 4
MINIMUM_BOARD_SIZE = 2 # I'm using 2 to make testing easier
MAXIMUM_BOARD_SIZE = 20 # For when you're really, REALLY bored
EXIT_COMMANDS = ["e", "exit"]
SECONDS_TO_SHOW_BOARD_FOR_AT_START = 3

# Variables
board = [] # Made up of rows represented by lists that hold cells represented by lists that look like: ["A", True] or ["C", False]
board_size = DEFAULT_BOARD_SIZE
currently_revealed_cards = [] # Made of of pair of coodrinated of cards that are currently being shown
score = 0

# Functions

def print_error(what_to_print, exclamation_mark=True):
    """Prints a error message.

    Args:
        what_to_print (str): Error message to print.
        exclamation_mark (bool, optional): Weather or not to add an exclamation_mark at the end. Defaults to True.
    """
    
    if exclamation_mark:
        print("❌  {}!".format(what_to_print))
    else:
        print("❌  {}".format(what_to_print))

def print_warning(what_to_print, exclamation_mark=True):
    """Prints a warning message.

    Args:
        what_to_print (str): Warning message to print.
        exclamation_mark (bool, optional): Weather or not to add an exclamation_mark at the end. Defaults to True.
    """
    if exclamation_mark:
        print("⚠  {}!".format(what_to_print))
    else:
        print("⚠  {}".format(what_to_print))

def print_success(what_to_print, exclamation_mark=True):
    """Prints a success message.

    Args:
        what_to_print (str): Success message to print.
        exclamation_mark (bool, optional): Weather or not to add an exclamation_mark at the end. Defaults to True.
    """
    if exclamation_mark:
        print("✔  {}!".format(what_to_print))
    else:
        print("✔  {}".format(what_to_print))

# Exit the program
def exit_program(exit_command=None):
    """Exit the program.

    Args:
        exit_command (str, optional): The command that triggered the exit. Defaults to None.
    """

    if exit_command is not None:
        print_success("Exit command detected: {}".format(exit_command), False)

    print_success("Exiting program")
    exit()

def clear_console():
    """'clear' the console by dumping a bunch of newlines into it
    """
    AMOUNT_TO_DUMP = 420
    str = "Shoo! Scroll back down!"
    # Loop a bunch of times and add newlines to a tring
    for i in range(AMOUNT_TO_DUMP):
        str+="\n"
    # Print all the newlines with a single print statement because calling print a bunch of times is slow
    print(str)

# Get a valid integer input from the user
def get_integer_input(prompt, minimum=1, maximum=10, default=None):
    """Gets a valid integer from the user, allowing for maximum and minimum values.

    Args:
        prompt (str): The message to show to the user when asking for input
        minimum (int, optional): The minimum value to be accepted. Defaults to 1.
        maximum (int, optional): The maximum value to be accepted. Defaults to 10.
        default (str, optional): The value to return if the user inputs nothing. Defaults to None.

    Returns:
        int: The value provided by the user, or the default value if it was provided and the user inputted nothing
    """
    value = 0

    valid_input = False
    # Loop until a valid input is provided or the user chooses to exit the program
    while not valid_input:
        print("{} (between {} & {})?".format(prompt, minimum, maximum))
        inputted_value = input("$ ").strip().lower() # Get input from user

        # If a default was set and the user inputted nothing, use the default
        if len(inputted_value) == 0:
            if default is not None:
                value = default
                valid_input = True
                print_warning("No option selected. Defaulting to {}".format(default))
            else:
                print_error("Please enter a number!")
        else:

            # If the user provided a valid exit command, exit the program
            if inputted_value in EXIT_COMMANDS:
                exit_program(inputted_value)

            # Try and cast the input to an integer
            try:
                inputted_value = int(inputted_value)
                # Maximum
                if inputted_value > maximum:
                    print_error("Please enter a integer less than {}".format(maximum+1))
                # Minimum
                elif inputted_value < minimum:
                    print_error("Please enter a integer greater than {}".format(minimum-1))
                else:
                    value = inputted_value
                    valid_input = True
            except ValueError:
                print_error("Please enter a valid integer")

    return value

def print_board(show_all=False):
    """Print the board

    Args:
        show_all (bool, optional): Wether or not to show all the caracters. Defaults to False.
    """

    # Print the column numbers (the numbers along the top)
    column_numbers = "   "
    # Add a number for each row in the board
    for i in range(len(board)):
        column_numbers += " {}".format(i+1)
        if len(str(i+1)) < 2:
            column_numbers += " " # Extra space so that the sigle digit column numbers line up

    print(column_numbers + "\n")

    # Loop through each row, using enumerate to get both the actual list element and the index
    for i, row in enumerate(board):

        row_text = "{} ".format(i+1)
        if len(str(i+1)) < 2:
            row_text += " " # Extra space so that the sigle digit row numbers line up

        for col in row:
                if col[1] or show_all:
                    row_text += " {} ".format(col[0])
                else:
                    row_text += " # "
        print(row_text + "\n")


# Main program
def main():
    """The main function for the game.
    """

    # Variables
    total_found_cards = 0

    #
    #   PROGRAM START
    #

    print("Welcome to Memories!")
    print("This is a memory game.")
    print("Type 'e' or 'exit' to exit the program at any time.")

    #
    #  BOARD GENAERATION
    #

    # Ask the user how large they would like the board to be
    board_size = get_integer_input("What size board would you like", minimum=MINIMUM_BOARD_SIZE, maximum=MAXIMUM_BOARD_SIZE, default=DEFAULT_BOARD_SIZE)

    # generate a set of random pairs
    chars_to_choose_from = []
    i = 1
    while i < (board_size*board_size)+1:
        # For  every second character, just add the previous character to the list. This ensures that there are pairs
        if i % 2 == 0:
            chars_to_choose_from.append(chars_to_choose_from[i-2])
        else:
            chars_to_choose_from.append(random.choice(CHARACTERS))
        i += 1

    # Genarate a board using the pairs
    for i in range(board_size):
        row = []
        for j in range(board_size):
            char = random.choice(chars_to_choose_from)
            chars_to_choose_from.pop(chars_to_choose_from.index(char))
            row.append([char, False])
        board.append(row)
    
    #
    #   GAME START
    #

    # Show the board for the size of the board minus 1 seconds
    print_board(True)
    time.sleep(board_size)
    clear_console()
    print_board()

    #
    #   GAME LOOP
    #

    playing = True
    while playing:

        # If there are two or more cards currently revealed (that haven't already been detected as matches), hide them

        # Ask the user what card they want to reveal
        col = get_integer_input("What Column (vertical) do you want to reveal a card from", minimum=1, maximum=board_size)-1
        row = get_integer_input("What Row (horizontal) do you want to reveal a card from", minimum=1, maximum=board_size)-1
        
        
        # Make sure that card isn't already locked
        if board[row][col][1]:
            print_error("That card has already been chosen!")
        else:

            # Show that card
            board[row][col][1] = True
            currently_revealed_cards.append([row, col])
            print_board()

            # If there are two cards currently revealed, check if they match
            if len(currently_revealed_cards) >= 2:

                # Do the symbols match?
                if board[currently_revealed_cards[0][0]][currently_revealed_cards[0][1]][0] == board[currently_revealed_cards[1][0]][currently_revealed_cards[1][1]][0]:
                    # They match!
                    # Empty the array of cards currently revealed
                    currently_revealed_cards[:] = [] # Can't use currently_revealed_cards=[] because that breaks things for some reason :/
                    
                    total_found_cards += 2 # Increment the count of how many pairs have been matched

                    print_success("Sucessfull match!")

                    # Are there as many matches as there are pairs? ()
                    if total_found_cards >= (board_size*board_size)-1:
                        # Re print the board, showing all cards incase it was an odd number of cards
                        clear_console()
                        print_board(True)
                        print_success("All matches found! Well done")
                        exit_program()
    
                else:
                    # They don't match, so let's hide them
                    for card in currently_revealed_cards:
                        board[card[0]][card[1]][1] = False # Board[X-coordinate][Y-coordinate][hidden] = False
                    
                    # Clear out the array of cards currently revealed since we're hiding them
                    currently_revealed_cards[:] = [] # Can't use currently_revealed_cards=[] because that breaks things for some reason :/

                    print_error("Cards don't match")

                    # And then print the board again (after a short wait)
                    time.sleep(2)
                    clear_console()

                    

                print_board() # Print the board again


# Only the the functions if this is being run as a standalone program
if __name__ == "__main__":
    # Exit gracefully on ctrl+C
    try:
        main()
    except KeyboardInterrupt:
        exit_program("ctrl+C")

