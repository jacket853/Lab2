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

def display_menu():
    print("\nYou are in a concrete room barely taller than you. There is an air duct, a grate, and a very small nightstand.")
    print("On the nightstand is a lamp, a shoestring, and a paper clip. What do you want to do?")
    print("1  Inspect the stuff on the nightstand")
    print("2  Find a way out")
    print("3  Stare blankly at the wall\n")

def opt_1():
    pass

def opt_2():
    pass

def opt_3():
    print("\nYou stare blankly at the wall. What did you expect?")

def main():
    display_menu()
    choice = input_integer("What do you want to do? ", 1, 3)
    if choice == 1:
        opt_1()
    elif choice == 2:
        opt_2()
    elif choice == 3:
        opt_3()

main()
