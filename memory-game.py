# =================================
# 11DTE Programming asessment: memory game by Zade Viggers is licensed under Attribution-ShareAlike 4.0 International.
# To view a copy of this license, visit http://creativecommons.org/licenses/by-sa/4.0/
# Check the LICENSE.md file for more details.
# =================================

# Memory game!

# Board
#     1   2   3   4
#   ╔═══╦═══╦═══╦═══╗
# 1 ║ @ ║ @ ║ @ ║ @ ║
#   ╠═══╬═══╬═══╬═══╣
# 2 ║ @ ║ @ ║ @ ║ @ ║
#   ╠═══╬═══╬═══╬═══╣
# 3 ║ @ ║ @ ║ @ ║ @ ║
#   ╠═══╬═══╬═══╬═══╣
# 4 ║ @ ║ @ ║ @ ║ @ ║
#   ╚═══╩═══╩═══╩═══╝
# 



# Constants
EMOJIS = ["😳","😂","😎","😍","😛","😭","🥵","🥶","🤡","🥳","🤢","👺","👻","☠","👽","👾","🤖","💩","🙉","🙀","🦄","🐲","🐳","🦆","👀","👌","👏","👋","🎃","🎉","💎","🔊","🔒","⌛","🍫","🍕","🍖","🚗","🚂"]
DEFAULT_BOARD_SIZE = 4
EXIT_COMMANDS = ["exit", "e"]

# Variables
board = [[]]
board_size = 4

# Functions

# Print an error message
def print_error(what_to_print: str) -> None:
    print(f"❌ {what_to_print}!")

# Print a warning message
def print_warning(what_to_print: str) -> None:
    print(f"⚠ {what_to_print}.")

# Print a success message
def print_success(what_towhat_to_print: str) -> None:
    print(f"✔ {what_to_print}!")


def get_integer_input(prompt: str, min=None: int, max=None: int, default=None: int) -> int:
    value = 0

    valid_input = False
    # Loop until a valid input is provided or the user chooses to exit the program
    while not valid_input:
        print(f"{prompt}, or type {EXIT_COMMANDS[0]} to exit the program.")
        inputted_value = input(": ").strip().lower() # Get input from user

        # If a default was set and the user inputted nothing, use the default
        if default is not None and len(inputted_value) == 0:
            inputted_value = default

        # If the user provided a valid exit command, exit the program
        if inputted_value in EXIT_COMMANDS:
            print_warning("Exiting program...")
            exit()

        # Try and cast the input to an integer
        try:
            value = int(inputted_value)
            valid_input = True
        except ValueError:
            print_error("Please enter a valid integer")
    
    return value

# Main program

# Ask the user how large they would like the board to be
board_size = get_integer_input("", min=2, max=len(EMOJIS), default=DEFAULT_BOARD_SIZE)

