import sqlite3
from stock_quotes_current import *

def open_con():
    global con
    con = sqlite3.connect("portfolio.db")
    global cur
    cur = con.cursor()

def close_con():
    con.commit()
    cur.close()
    con.close()

def create_table():
    open_con()
    cur.execute("CREATE TABLE IF NOT EXISTS portfolio1 (ticket TEXT, quantity INTEGER)")
    close_con()

def show_stock():
    open_con()
    cur.execute("SELECT * FROM portfolio1")
    result = cur.fetchall()
    print(result)
    close_con()

def buy_stock():
    valid_in = False
    while not valid_in:
        try:
            addition = int(input("How many shares would you like to buy? "))
            valid_in = True
        except:
            print("Error, input must be a positive integer")
    ticket1 = input("Enter the ticket of the stock you would like to buy ")
    open_con()
    cur.execute("SELECT ticket FROM portfolio1")
    ticket_list = cur.fetchall()
    if (ticket1,) in ticket_list:
        current_quant = cur.execute("SELECT quantity FROM portfolio1 WHERE ticket=?", (ticket1,))
        current_quant_data = (cur.fetchall())[0][0]
        new_quant = current_quant_data + addition
        cur.execute("UPDATE portfolio1 SET quantity=? WHERE ticket=?", ((new_quant),(ticket1)))
    else:
        cur.execute("INSERT INTO portfolio1 VALUES(?,?)", (ticket1, addition))
    quote1 = get_quote(ticket1)
    cur.execute("SELECT balance FROM account1")
    balance_1 = float((cur.fetchall())[0][0])
    differential = float(float(quote1) * float(addition))
    new_balance = balance_1 - differential
    cur.execute("UPDATE account1 SET balance=?", (new_balance,))
    print("Transaction complete")
    close_con()

def sell_stock():
    valid_in = False
    while not valid_in:
        try:
            addition = int(input("How many shares would you like to sell? "))
            valid_in = True
        except:
            print("Error, input must be a positive integer")
    ticket1 = input("Enter the ticket of the stock you would like to sell ")
    open_con()
    cur.execute("SELECT ticket FROM portfolio1")
    ticket_list = cur.fetchall()
    if (ticket1,) in ticket_list:
        current_quant = cur.execute("SELECT quantity FROM portfolio1 WHERE ticket=?", (ticket1,))
        current_quant_data = (cur.fetchall())[0][0]
        new_quant = current_quant_data - addition
        cur.execute("UPDATE portfolio1 SET quantity=? WHERE ticket=?", ((new_quant),(ticket1)))
    else:
        print("Error, this stock is not in your portfolio")
    quote1 = get_quote(ticket1)
    cur.execute("SELECT balance FROM account1")
    balance_1 = float((cur.fetchall())[0][0])
    differential = float(float(quote1) * float(addition))
    new_balance = balance_1 + differential
    cur.execute("UPDATE account1 SET balance=?", (new_balance,))
    print("Transaction complete")
    cur.execute("DELETE FROM portfolio1 WHERE quantity=0")
    close_con()


    
    
def create_account():
    open_con()
    cur.execute("CREATE TABLE IF NOT EXISTS account1 (balance REAL)")
    cur.execute("INSERT INTO account1 VALUES(10000)")
    close_con()

def show_account():
    open_con()
    cur.execute("SELECT balance FROM account1")
    balance_1 = cur.fetchall()
    print(balance_1)
    close_con()
