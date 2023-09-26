"""
Name: Jack Harvey
Date: 9/25/23
Description: This program is a simple text-based choose-your-own adventure that implements certain features of Python."
"""

from __future__ import annotations
import math as m
from types import NoneType

def input_integer(prompt: str="", lower_lim: int=-m.inf, upper_lim: int=m.inf) -> int:
    """Get user input within a range
    Args: The string to prompt the user, the lower/upper limits (set to infinity by default)
    Returns: The valid integer that the user chose
    Raises: ValueError if the user's input cannot be casted to an int, KeyboardInterrupt should CTRL+C happen
    """
    # Very standard, 
    while True:
        try:
            int_input = int(input(prompt))
            if lower_lim <= int_input <= upper_lim:
                return int_input
            else: # These bounds are infinite by default (virtually not set)
                print(f"Please enter an int between {lower_lim} and {upper_lim}.")
        except ValueError:
            print(f"Please enter an int.")
        except KeyboardInterrupt:
            print("\nExiting program...")
            exit()

def display_menu() -> None:
    """Print the menu at the beginning of every while loop in main()
    Args: None
    Returns: None
    Raises: None
    """
    menu = "\nYou are in a concrete room barely taller than you. "
    menu += "There is an air duct, a grate in the floor, and a very small nightstand. "
    menu += "On the nightstand is a lamp, a shoestring, and a paperclip. What do you want to do? "
    menu += "\n Type 'exit' to give up."
    print(menu)
    print_options("Inspect the stuff on the nightstand", "Find a way out", "Stare blankly at the wall", "Stumble a bit")

# Satisfies 7
def print_options(*options: str) -> None:
    """Prints the choices that the user has to pick from when providing input
    Args: An unlimited number of positional arguments, usually sentences
    Returns: None
    Raises: None
    """
    for i, option in enumerate(options):
        print(f"{i+1}. {option}")
    
# Satifies 6, 12
def inspect_nightstand(inventory: list, objs: list=None) -> list:
    """Gives the user the option of picking several different objects from the nightstand and placing them into their inventory
    Args: The inventory (blank at the start), remaining objects on the nightstand
    Returns: The updated inventory and things on the nightstand
    Raises: None
    """
    # This will not happen. List will be empty should the user choose 3 happen.
    if objs is None:
        print("Objs to be entered cannot be default.")
        exit()

    print("\nOn the nightstand is a lamp, a shoestring, and a paperclip. What do you want to do?")
    print_options("Take the lamp", "Take the shoestring", "Take the paperclip", "Take all three")
    choice = input_integer("\t->", 1, 4)

    if choice == 1 and "lamp" not in inventory:
       inventory, objs = update_inventory(inventory, objs, "lamp")
    elif choice == 2 and "shoestring" not in inventory:
        inventory, objs = update_inventory(inventory, objs, "shoestring")
    elif choice == 3 and "paperclip" not in inventory:
        inventory, objs = update_inventory(inventory, objs, "paperclip")
    elif choice == 4 and objs is not []:
        inventory, objs = update_inventory(inventory, objs)
    else: # Make sure that the user cannot add an item that doesn't exist
        print("\nThe item you would like is no longer on the nightstand.")

    return inventory, objs

# Satisfies 11
def update_inventory(inventory: list, objs: list, add_objs: NoneType=None) -> list:
    """Adds strings to inventory list and removes the appropriate object from the nightstand list
    Args: The user's inventory, objects on the nightstand, objects to be added (which is None if we are taking all things)
    Returns: The updated inventory and objects lists
    Raises: None
    """
    if add_objs is not None:
        inventory.append(add_objs)
        objs.remove(add_objs)
    else:
        inventory.extend(objs) # The equivalent of adding lists
    return inventory, objs

def leave_room(inventory: list) -> None:
    """Large print function that branches based on the user's choice and certain items in their inventory
    Args: The user's inventory
    Returns: None
    Raises: None
    """
    print("\nYou have only two choices here.")
    print_options("Try to crawl through the air duct", "Try to unscrew the grate")
    choice = input_integer("\t-> ", 1, 2)
    
    if len(inventory) == 1: # If the user has only iterated once
        # Inventory also factors into branching
        if choice == 1 and "lamp" in inventory:
            lamp_choice = "\nYou easily enter the duct, but it is pitch black. "
            lamp_choice += "When you finally find an outlet to plug in the lamp, the bulb glows brightly. "
            lamp_choice += "Unfortunately, it is so bright that Siren Head finds you and gobbles you up."
            print(lamp_choice)
        elif choice == 1 and "shoestring" in inventory:
            lamp_choice = "\nYou have three shoelaces (2 xshoes, 1x), an odd number... "
            lamp_choice += "Naturally, you are teleported to the third dimension and become the z-coordinate on a 3D math problem."
            print(lamp_choice)
        elif choice == 1 and "paperclip" in inventory:
            clip_choice = "\nWhew! That was a close one! You scramble through the duct. "
            clip_choice += "The paperclip didn't really do anything, but it was the only safe choice. "
            clip_choice += "So, good job!"
            print(clip_choice)
        elif choice == 2:
            print("\nThe grate is hard to unscrew, so you pound your foot on it. You fall through and die.")
    elif len(inventory) == 0:
        print("\nYou are so light that you float out of the room and asphyxiate due to high-altitude oxygen loss.")
    # If the user has already chosen something for his bag
    elif len(inventory) > 1 and choice == 1:
        print("\nYou are too heavy, so the moment your finger touches the grate, you implode and form a supermassive black hole.")
    elif len(inventory) > 1 and choice == 2:
        print("\nYou are too heavy, so you fall straight through the thin aluminum of the air duct onto the hard floor.")

def stare() -> None:
    """Prints the outcome of choosing option 3 initially
    Args: None
    Returns: None
    Raises: None
    """
    print("\nYou stare blankly at the wall. What did you expect?")

# Satisfies 5
def enter_restricted_area(area_name:str, pos_indic:NoneType=None) -> None:
    """This function is kinda dumb - it really just satisfies several of the requirements.
    If the user selected option 4 (to wander), then they can either go to the corner/mirror or simply wander again.
    This function uses try and except statments to see if their choices result in valid function calls.
    Args: The name of the area the user chose (or omitted), indicator of choosing 4 
    Returns: None
    Raises: ValueError if the below function's conditional triggers
    """
    # If it exists, pos_indic also simply demonstrates if the call provided a kwarg to default
    try:
        attempt_enter_restricted_area(area_name, pos_indic)
        print_restricted_area(area_name)
    except ValueError as error:
        print(error)

# Satisfies 8, 13, 14
def attempt_enter_restricted_area(area_name:str, first_pos:NoneType=None, second_pos:NoneType=None) -> None:
    """If the user chose option 3 (blindly walk), they will trigger the if statment and following error message
    Args: The name of the area, the first_pos (filled by pos_indic if the user chose 4), the second_pos (basically irrelevant in this case)
    Returns: None
    Raises: ValueError as described above
    """
    # Option 3 triggers b/c no kwarg was filled, so default val for pos_indic is None
    if first_pos is not None or second_pos is not None:
        raise ValueError(f"\nCannot enter {area_name} using given arguments.")

# Satisfies 9, 10
def print_restricted_area(area_name: str) -> None:
    """Uses an if statement to sort through specific locations, then using the unkown presuming the user chose 3
    Args:The name of the area the user chose
    Returns: None
    Raises: ValueError if the loc is not the corner or the mirror
    """
    if area_name == "corner":
        print("\nYou are now in the corner. There is nothing interesting here.")
    elif area_name == "mirror":
        print("\nYou are now in front of the mirror. Wow, they look familiar!.")
    else:
        raise ValueError(f"\nUnknown restricted area: {area_name}")

def main():
    inventory = []
    objs = ["lamp", "shoestring", "paperclip"]
    display_menu()
    # Satisfies 2, 4
    choice = input_integer("What do you want to do? ", 1, 4)

    # Program runs until the user types exit or presses ctrl+c (KeyboardInterrrupt)
    while choice != "exit":
        if choice == 1:
            inventory, objs = inspect_nightstand(inventory, objs)
        elif choice == 2:
            leave_room(inventory)
            break
        elif choice == 3:
            stare()
        elif choice == 4:
            area_choice_text = "\n1 to navigate to corner, 2 for the mirror, 3 to walk blindly, "
            area_choice_text += "4 to walk in the dark but with your eyes open... -> "
            area_choice = input_integer(area_choice_text, 1, 4)
            if area_choice == 1:
                enter_restricted_area("corner")
            elif area_choice == 2:
                enter_restricted_area("mirror")
            elif area_choice == 3:
                enter_restricted_area("Area 51 or something")
            # Satisfies 1
            elif area_choice == 4:
                enter_restricted_area("Knowhere", pos_indic="Knowhere")

        display_menu()
        choice = input_integer("What do you want to do? ", 1, 4)

    print("Thanks for playing.")

if __name__ == "__main__":
    main()
