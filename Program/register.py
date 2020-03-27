import sqlite3
import os
from utilityfuncs import *
import getpass


def Register(x:int):

    print("REGISTER".center(80,'-'))
    print("Registeration has begun::")

    gotuname = 1
    while(gotuname):
        
        uname = input("Enter a username:")
        conn = sqlite3.connect("../Data/maindatabase.db")
        c = conn.cursor()
        found = 0
        for row in c.execute("SELECT username FROM User_List"):
            if(encryptDecrypt(row[0]) == uname):
                print("Username was found in the list!\nPlease create a new username!")
                found = 1
                break
        if(found == 1):
            conn.close()
        
        elif(found == 0):
            conn.close()
            gotuname = 0

    print("\nUsername is available!")
    print("\nEnter a Password:")
    password = getpass.getpass()
    print("\nChoose a User Type from below:")
    if(x == 1):    
        print("1. Admin/Owner")
        print("2. Accountant")
        print("3. Receptionist")
        print("4. Gym Staff")
        print("5. Gym User")
    else:
        print("1. Gym Staff")
        print("2. Gym User")
    gotpropertype = 1
    typechoice = 0
    while(gotpropertype):
        typechoice = int(input("Enter your user choice:"))
        if(typechoice>=1 and typechoice<=5 and x==1):
            gotpropertype = 0
        
        elif(typechoice>=1 and typechoice<=2 and x==2):
            typechoice+=3
            gotpropertype = 0

        else:
            print("\nPlease enter a valid type!")
    
    print("\n\nYou have entered the following data:")
    if(x==1):
        DD(uname,encryptDecrypt(password),typechoice)
    else:
        DD(uname,encryptDecrypt(password),(typechoice-3))
    print("\nWriting data to database, Please Wait.....")
    conn = sqlite3.connect("../Data/maindatabase.db")
    c = conn.cursor()
    values = (encryptDecrypt(uname),encryptDecrypt(password),typechoice)
    c.execute("INSERT INTO User_List VALUES(?,?,?)",values)
    conn.commit()
    conn.close()
    print("\nDone sending values to database.")
    print("Heading back to previous menu")
    callpause()
    return