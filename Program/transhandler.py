from utilityfuncs import callclearscreen,callpause,MenuHeaderPrinter
from datetime import datetime
import sqlite3
import prettytable as pt

def GetCurrentTime():
    now = datetime.now()
    return now.strftime("%H:%M:%S , %d/%m/%Y")

def EnterintoLogs(values):
    conn = sqlite3.connect("./Data/maindatabase.db")
    c = conn.cursor()
    c.execute('''INSERT INTO Transaction_Log VALUES(?,?,?,?,?)''',values)
    conn.commit()
    conn.close()

def EnterFunds(uid):
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
    print("Current Transaction Logs are:")
    conn = sqlite3.connect("./Data/maindatabase.db")
    c = conn.cursor()
    c.execute("SELECT * FROM Transaction_Log")
    x = pt.from_db_cursor(c)
    print(x)
    callpause()

def ViewFunds(mode):
    conn = sqlite3.connect("./Data/maindatabase.db")
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

    breaktransmenu = 0
    while(not breaktransmenu):

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
            breaktransmenu = 1

        else:
            print("\nWrong Choice! Please choose a correct option:")
            callpause()
    return