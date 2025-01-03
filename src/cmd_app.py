import requests
from prettytable import PrettyTable
import colorama
from colorama import Fore, Style

def color_changer(colors):
    color = {
        "red": Fore.RED,
        "green": Fore.GREEN,
        "blue": Fore.BLUE,
        "magenta": Fore.MAGENTA,
        "cyan": Fore.CYAN,
        "reset": Fore.RESET,
    }
    return color.get(colors.lower(), Fore.RESET)
    
def main():
    print("Welcome to the Cmd app !")
    print("Type 'help' to see the avaible commands")

    actual_color = Fore.RESET

    while True:
        commands = input(f"{actual_color}Cmd > ").strip()

        if commands == "exit":
            print(Style.RESET_ALL)
            break

        elif commands == "help":
            print(actual_color +"Avaible commands :" + Style.RESET_ALL)
            print(actual_color +"- color (to change the cmd color)"+ Style.RESET_ALL)
            print(actual_color +"- exit (to quit the cmd app)"+ Style.RESET_ALL)

        elif commands.startswith("color"):
            try: 
                _, couleur = commands.split() 
                actual_color = color_changer(couleur)
                print(color_changer(couleur), end="")  
            except ValueError: 
                print("Usage: color <couleur>")

        else:
            print("Unrecognized command type 'help' to see the avaible commands")



if __name__ == "__main__":
    main()