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

def main():
    print(input_integer("Enter an int between 1 and 3: ", 1, 3))

main()
