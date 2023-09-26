from __future__ import annotations
import math as m
from types import NoneType

def input_integer(prompt: str="", lower_lim: int=-m.inf, upper_lim: int=m.inf) -> int:
    while True:
        try:
            int_input = int(input(prompt))
            if lower_lim <= int_input <= upper_lim:
                return int_input
            else:
                print(f"Please enter an int between {lower_lim} and {upper_lim}.")
        except ValueError:
            print(f"Please enter an int.")
        except KeyboardInterrupt:
            print("\nExiting program...")
            exit()

def display_menu() -> None:
    menu = "\nYou are in a concrete room barely taller than you. "
    menu += "There is an air duct, a grate in the floor, and a very small nightstand. "
    menu += "On the nightstand is a lamp, a shoestring, and a paperclip. What do you want to do? "
    menu += "\n Type 'exit' to give up."
    print(menu)
    print_options("Inspect the stuff on the nightstand", "Find a way out", "Stare blankly at the wall", "Stumble a bit")

# Satisfies 7
def print_options(*options: str) -> None:
    for i, option in enumerate(options):
        print(f"{i+1}. {option}")
    
# Satifies 6, 12
def inspect_nightstand(inventory: list, objs: list=None) -> list:
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
    else:
        print("\nThe item you would like is no longer on the nightstand.")

    return inventory, objs

# Satisfies 11
def update_inventory(inventory: list, objs: list, add_objs: NoneType=None) -> list:
    if add_objs is not None:
        inventory.append(add_objs)
        objs.remove(add_objs)
    else:
        inventory.extend(objs)
    return inventory, objs

def leave_room(inventory: list) -> None:
    print("\nYou have only two choices here.")
    print_options("Try to crawl through the air duct", "Try to unscrew the grate")
    choice = input_integer("\t-> ", 1, 2)
    
    if len(inventory) == 1:
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
    elif len(inventory) > 1 and choice == 1:
        print("\nYou are too heavy, so the moment your finger touches the grate, you implode and form a supermassive black hole.")
    elif len(inventory) > 1 and choice == 2:
        print("\nYou are too heavy, so you fall straight through the thin aluminum of the air duct onto the hard floor.")

def stare() -> None:
    print("\nYou stare blankly at the wall. What did you expect?")

# Satisfies 8, 13, 14
def attempt_enter_restricted_area(area_name, one_loc=None, two_loc=None) -> None:
  if one_loc is not None or two_loc is not None:
    raise ValueError(f"\nCannot enter {area_name} using given arguments.")

# Satisfies 9, 10
def print_restricted_area(area_name: str) -> None:
  if area_name == "corner":
    print("You are now in the corner. There is nothing interesting here.")
  elif area_name == "mirror":
    print("You are now in front of the mirror. Wow, they look familiar!.")
  else:
    raise ValueError(f"\nUnknown restricted area: {area_name}")

# Satisfies 5
def enter_restricted_area(area_name, loc_indic=None) -> None:
  try:
    attempt_enter_restricted_area(area_name, loc_indic)
    print_restricted_area(area_name)
  except ValueError as error:
    print(error)

def main():
    inventory = []
    objs = ["lamp", "shoestring", "paperclip"]
    display_menu()
    # Satisfies 2, 4
    choice = input_integer("What do you want to do? ", 1, 4)

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
                enter_restricted_area("Knowhere", loc_indic="Knowhere")

        display_menu()
        choice = input_integer("What do you want to do? ", 1, 4)

    print("Thanks for playing.")

if __name__ == "__main__":
    main()
