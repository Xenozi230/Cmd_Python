# CMD Python

## Table of Content : 

1. Commands
2. Create .exe 

## 1. Commands

- `help`: to see the avaible commands
- `color` : to change the cmd color 
- `crypto`: to see the price of crypto-monaie in live
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