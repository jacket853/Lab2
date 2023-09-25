from __future__ import annotations
import math as m

def input_integer(prompt: str, lower_lim: int=-m.inf, upper_lim: int=m.inf) -> int:
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

def display_menu():
    menu = "\nYou are in a concrete room barely taller than you. "
    menu += "There is an air duct, a grate in the floor, and a very small nightstand. "
    menu += "On the nightstand is a lamp, a shoestring, and a paperclip. What do you want to do? "
    menu += "\n1  Inspect the stuff on the nightstand"
    menu += "\n2  Find a way out"
    menu += "\n3  Stare blankly at the wall"
    menu += "\n Type 'exit' to give up."
    print(menu)

def inspect_nightstand(inventory: list, objs: list=None) -> list:
    if objs is None:
        print("You did not enter the objects to be used.")
        exit()

    options = "\nOn the nightstand is a lamp, a shoestring, and a paperclip. What do you want to do? "
    options += "\n1 Take the lamp"
    options += "\n2 Take the shoestring"
    options += "\n3 Take the paperclip"
    options += "\n4 Take all three\n"
    options += "\n What do you want to do? "
    choice = input_integer(options, 1, 4)

    if choice == 1:
       inventory, objs = update_inventory(inventory, objs, "lamp")
    elif choice == 2:
        inventory, objs = update_inventory(inventory, objs, "shoestring")
    elif choice == 3:
        inventory, objs = update_inventory(inventory, objs, "paperclip")
    elif choice == 4:
        inventory, objs = update_inventory(inventory, objs, None)

    print(inventory)
    print(objs)
    return inventory

def leave_room(inventory: list):
    options = "\nYou have only two choices here."
    options += "\n1 Try to crawl through the air duct"
    options += "\n2 Try to unscrew the grate"

    choice = input_integer(options, 1, 2)
    if choice == 1 and "lamp" in inventory:
        pass
    elif choice == 1 and "shoestring" in inventory:
        pass
    elif choice == 1 and "paperclip" in inventory:
        pass
    elif choice == 2:
        pass

def update_inventory(inventory: list, objs: list, add_objs: str) -> list:
    if add_objs is not None:
        inventory.append(add_objs)
        objs.remove(add_objs)
    else:
        inventory.append(objs)
        objs.clear()
    return inventory, objs

def stare():
    print("\nYou stare blankly at the wall. What did you expect?")

def main():
    inventory = []
    objs = ["lamp", "shoestring", "paperclip"]
    display_menu()
    choice = input_integer("What do you want to do? ", 1, 3)

    while choice != "exit":
        if choice == 1:
            inventory = inspect_nightstand(inventory, objs)
        elif choice == 2:
            inventory, objs = leave_room(inventory)
            break
        elif choice == 3:
            stare()

        display_menu()
        choice = input_integer("What do you want to do? ", 1, 3)

    print("Thanks for playing.")

if __name__ == "__main__":
    main()
