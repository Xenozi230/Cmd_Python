# CMD Python

## Table of Content : 

1. Commands
2. Create .exe 

## 1. Commands

- `help`: to see the avaible commands
- `color` : to change the cmd color 
- `crypto`: to see the price of crypto-monaie in live
- `time`: to see the date en time 
- `password`: to generate password 
- `encoding`: to encode word or phrase
- `decoding`: to decode your word or phrase encode 
- `matrix`: to see the matrix effect and crtl+c for stop this effect
- `history`: "to see the order history"
- `exit`: to quit cmd app   


## 2. Create .exe

For create .exe file use :

- Cx_freeze : 

    For install cx_Freeze
    `pip install cx_Freeze`
    To create an .exe with cx_freeze, use the setup file and run with this command

    `python setup.py build`

- Pyinstaller :

    For install pyinstaller
    `pip install pyinstaller`
    to create an .exe with  pyinstaller, use this command 

    `pyinstaller --onefile cmd_app.py`