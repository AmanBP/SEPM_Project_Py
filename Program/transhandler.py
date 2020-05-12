from utilityfuncs import *
from datetime import datetime
import sqlite3
import prettytable as pt

def GetCurrentTime():
    '''
    Function for getting current system time.

    Function returns a string formatted in the format "HH:MM:SS , DD/MM/YYYY"
    '''
    now = datetime.now()
    return now.strftime("%H:%M:%S , %d/%m/%Y")

def EnterintoLogs(values):
    '''
    Function that creates entries for a transaction loc.
    values is a tuple containing 5 data members:
        (username,transaction type,value/amount,transaction time,comment)
    '''
    conn = sqlite3.connect("Data/maindatabase.db")
    c = conn.cursor()
    c.execute('''INSERT INTO Transaction_Log VALUES(?,?,?,?,?)''',values)
    conn.commit()
    conn.close()

def EnterFunds(uid):
    '''
    Function to "Deposit Funds"
    uid is a string containing the de-encrypted username string.

    Simply asks and adds the amount to the table.
    Creates a log once done.
    '''
    print("Current User:",uid)
    value = int(input("Enter the amount you want to add: "))
    print("Entering amount:",value,"to the database.")
    transactiontype = "deposit"
    transtime = GetCurrentTime()
    comment = str(input("Please enter a comment for this transaction: "))
    packet = (uid,transactiontype,value,transtime,comment)
    EnterintoLogs(packet)
    print("Done!")
    callpause()

def TakeFunds(uid):
    '''
    Function to "Withdraw Funds"
    uid is a string holding a de-encrypted username string.

    Uses ViewFunds in mode = 2 to get the current balance.
    Asks for a valeu to deduct if balance is not 0.
    If Balance is 0, it returns after giving a suitable statement.
    Else, it will keep asking a value to deduct, untill a proper value is given.
    (Note: Doesn't allow cancellation of this loop(for now).)
    Creates a log once done.
    '''
    print("Current User:",uid)
    gotpropervalue = 0
    balance = ViewFunds(2)
    print("Current Balance is: ",balance)
    if(balance == 0):
        print("0 Balance detected, Aborting!")
        callpause()
        return
    while(not gotpropervalue):
        value = int(input("Enter the amount you want to deduct: "))    
        if(value > balance):
            print("Value entered is greater than current balance of",balance)
            print("Please Enter a proper amount!")
        else:
            print("Accepted, Continuing...")
            gotpropervalue = 1
    print("Deducting amount:",value,"from the database.")
    transactiontype = "withdraw"
    transtime = GetCurrentTime()
    comment = str(input("Please enter a comment for this transaction: "))
    packet = (uid,transactiontype,value,transtime,comment)
    EnterintoLogs(packet)
    print("Done!")
    callpause()

def TransLogs():
    '''
    Function that prints all the Transaction logs found in the table Transaction_Log.

    Creates a table using pretty table and prints that table.
    '''
    print("Current Transaction Logs are:")
    conn = sqlite3.connect("Data/maindatabase.db")
    c = conn.cursor()
    c.execute("SELECT * FROM Transaction_Log")
    x = pt.from_db_cursor(c)
    print(x)
    callpause()

def ViewFunds(mode):
    '''
    Function to see current balance
    Mode is an integer

    Builds the final balance value, using transaction types.
    Starts counting balance from 0.
    Queries the maindatabase.db file and extracts all transaction value and their type.
    For a withdrwal, balance is deducted by the value.
    For a deposit, balance is incremented by that value.
    
    If mode = 1:
        It functions as a current balance printer.
    else:
        It returns the value of balance.
    '''
    conn = sqlite3.connect("Data/maindatabase.db")
    c = conn.cursor()
    balance = 0
    for row in c.execute("SELECT operation,amount FROM Transaction_Log"):
        if(row[0] == "deposit"):
            balance += row[1]
        elif(row[0] == "withdraw"):
            balance -= row[1]
    conn.close()
    if(mode == 1):
        print("Current Balance is:",balance)
        callpause()
        return
    else:
        return balance

def TransHandler(uid):
    '''
    Transaction Wrapper Function

    uid is a string having a decrypted username, it is passed onto the transact functions as per needed.
    Value of uid is used to log usernames in a transaction.
    '''
    while(True):
        try:
            callclearscreen()
            MenuHeaderPrinter("Transaction Menu")
            print("1. Enter Funds")
            print("2. Take Funds")
            print("3. Check Transaction Logs")
            print("4. View Current Balance")
            print("5. Go Back")
            choice = int(input("Choose an option:"))

            if(choice == 1):
                EnterFunds(uid)

            elif(choice == 2):
                TakeFunds(uid)

            elif(choice == 3):
                TransLogs()

            elif(choice == 4):
                ViewFunds(1)

            elif(choice == 5):
                raise BreakMenu

            else:
                raise WrongChoiceError

        except BreakMenu:
            break
        
        except WrongChoiceError:
            print("Wrong Choice, Please choose a correct option!")
            callpause()

        except ValueError:
            print("Invalid Character has been entered!")
            callpause()
    return