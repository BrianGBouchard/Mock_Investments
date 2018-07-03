from stock_quotes_current import *
from sqlite_operationsTEST import *

#use create_account() to initialize your 'account' the first time you use the program


def main():
    create_table()
    valid_in = False
    while not valid_in:
        user_choice = input("Please select an option.  Type 'B' to buy stock, 'S' to sell stock, 'V' to view portfolio, 'A' to view account, or 'X' to exit. ")
        if (user_choice.upper() == "B"):
            buy_stock()
            valid_in = True
        elif (user_choice.upper() == "S"):
            sell_stock()
            valid_in = True
        elif (user_choice.upper() == "V"):
            show_stock()
            valid_in = True
        elif (user_choice.upper() == "A"):
            show_account()
            valid_in = True
        elif (user_choice.upper() == "X"):
            return
        else:
            print("Error, invalid input.")
    valid_again = False
    while not valid_again:
        again = input("Would you like to perform another operation? Y or N ")
        if (again.upper() == "Y"):
            main()
            valid_again = True
        elif (again.upper() == "N"):
            valid_again = True
        else:
            print("Invalid input")
