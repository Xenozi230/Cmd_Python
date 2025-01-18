import requests
from prettytable import PrettyTable
from colorama import Fore, Style
import os 
from datetime import datetime
import secrets
import string 
import argparse
import base64
import time
import random

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
    print(table)

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

def get_time():
    now = datetime.now() 
    Time_date = now.strftime("%d-%m-%Y / %H:%M:%S") 
    return f"{Time_date}"

def password_generator(lenght = 15):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(caracteres) for i in range(lenght))
    return password

def encoding_message(message):
    encoded_message = base64.b64encode(message.encode()).decode()
    return encoded_message

def decoding_message(encoded_message):
    try:
        decoded_bytes = base64.b64decode(encoded_message.encode("utf-8"))
        return decoded_bytes.decode("utf-8")
    except Exception as e:
        return f"Erreur de décodage : {e}"
    
def get_terminal_width():
    return os.get_terminal_size().columns


def generate_random_line(width):
    characters = list("        1 0 ")
    return ''.join(random.choice(characters + [' ']) for _ in range(width))

def matrix_effect(speed=0.05):  
    try:
        while True:
            width = get_terminal_width()
            print(generate_random_line(width))
            time.sleep(speed)
    except KeyboardInterrupt:
        print("\nMatrix effect stopped")

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
            print(actual_color +"- time (to see the date and time)"+ Style.RESET_ALL)
            print(actual_color +"- password (to generate a password)"+ Style.RESET_ALL)
            print(actual_color +"- encoding (to encode a message or password)"+ Style.RESET_ALL)
            print(actual_color +"- decoding (to decode a message or password)"+ Style.RESET_ALL)
            print(actual_color +"- matrix (to see the matrix effect and crtl+c for stop this effect)"+ Style.RESET_ALL)
            print(actual_color +"- exit (to quit the cmd app)"+ Style.RESET_ALL)
            
        
        elif commands.startswith("color"):
            try: 
                _, couleur = commands.split() 
                actual_color = color_changer(couleur)
                print(color_changer(couleur), end="")  
            except: 
                print("Usage: color <couleur>")

        elif commands == "crypto":
            crypto_ids = ['bitcoin', 'ethereum', 'XRP' , 'BNB', 'solana', 'dogecoin', 'USDC', 'Cardano', 'Tron']
            prices = get_crypto_prices(crypto_ids)
            display_prices(prices)

        elif commands == "time":
            Time_date = get_time() 
            print(actual_color + Time_date + Style.RESET_ALL)
        
        elif commands == "password":
            password = password_generator()
            print(actual_color + password + Style.RESET_ALL)
            
        elif commands.startswith("encoding"):
            result = encoding_message(commands.split(" ", 1)[1])
            print(f"Encoded message : {result}")
        
        elif commands.startswith("decoding"):
            result = decoding_message(commands.split(" ", 1)[1])    
            print(f"Decoded message : {result}")
        
        elif commands == "matrix":
            matrix_effect()
            
        else:
            print("Unrecognized command type 'help' to see the avaible commands")
            
if __name__ == "__main__":
    main()