import requests
from prettytable import PrettyTable
import colorama
from colorama import Fore, Style
import os 

def get_crypto_prices(crypto_ids):
    url = 'https://api.coingecko.com/api/v3/simple/price'
    params = {
        'ids': ','.join(crypto_ids),
        'vs_currencies': 'usd'
    }
    response = requests.get(url, params=params)
    data = response.json()
    return data

def display_prices(prices):
    table = PrettyTable()
    table.field_names = ["Crypto-monnaie", "Prix (USD)"]
    for crypto, price_info in prices.items():
        table.add_row([crypto.capitalize(), price_info['usd']])
    print(table )

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
            print(actual_color +"- crypto (to see the price of crypto-monaie in live)"+ Style.RESET_ALL)
            print(actual_color +"- exit (to quit the cmd app)"+ Style.RESET_ALL)

        elif commands.startswith("color"):
            try: 
                _, couleur = commands.split() 
                actual_color = color_changer(couleur)
                print(color_changer(couleur), end="")  
            except ValueError: 
                print("Usage: color <couleur>")

        elif commands == "crypto":
            crypto_ids = ['bitcoin', 'ethereum', 'ripple', 'litecoin', 'cardano']
            prices = get_crypto_prices(crypto_ids)
            display_prices(prices)

        else:
            print("Unrecognized command type 'help' to see the avaible commands")



if __name__ == "__main__":
    main()