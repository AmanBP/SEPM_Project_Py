import sqlite3
import os
from utilityfuncs import *
import getpass
from prettytable import PrettyTable

def newAdminReg():
    '''
    Function only meant to register an admin user for the initial running of the program

    Only executes when main function detects 0 users in the User_List database.
    '''
    print("Registering Admin for the first run:")
    uname = input("Enter a username:")
    print("\nEnter a Password:")
    password = getpass.getpass()
    print("\n\nYou have entered the following data (password is encrypted):")
    DD(uname,encryptDecrypt(password),1)
    print("\nWriting data to database, Please Wait.....")
    conn = sqlite3.connect("Data/maindatabase.db")
    c = conn.cursor()
    values = (encryptDecrypt(uname),encryptDecrypt(password),1)
    c.execute("INSERT INTO User_List VALUES(?,?,?)",values)
    conn.commit()
    conn.close()
    print("\nDone sending values to database.")
    print("Heading back to previous menu")
    callpause()
    return

def Register(x:int):
    '''
    Register Function

    x:int corresponds to the "mode of registeration"
    if x = 1:
        The register code treats the registeration as an admin registering into the system.
    if x = 2:
        The register code treats the registeration as a receptionist registering a member into the system.
    '''
    print("REGISTER".center(80,'-'))
    print("Registeration has begun::")

    gotuname = 1
    while(gotuname):
        
        uname = input("Enter a username:")
        conn = sqlite3.connect("Data/maindatabase.db")
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
    conn = sqlite3.connect("Data/maindatabase.db")
    c = conn.cursor()
    values = (encryptDecrypt(uname),encryptDecrypt(password),typechoice)
    c.execute("INSERT INTO User_List VALUES(?,?,?)",values)
    conn.commit()
    conn.close()
    print("\nDone sending values to database.")
    print("Heading back to previous menu")
    callpause()
    return


def ListUsers():
    '''
    Function to list all users

    Creates an SQLite3 connection to maindatabase.db file.
    Queries for all users in the table User_List.
    Creates a table using a prettytable object and adds the data.
    Prints the created table.
    '''
    x = PrettyTable()
    x.field_names = ["Username","User Type"]
    usertypelist = ["Admin/Owner","Accountant","Receptionist","Gym Staff","Gym User"]
    conn = sqlite3.connect("Data/maindatabase.db")
    c = conn.cursor()
    print("Current Users found are: ")
    for row in c.execute("SELECT username,usertype FROM User_List"):
        data = [encryptDecrypt(row[0]),usertypelist[row[1]-1]]
        x.add_row(data)
    print(x)
    conn.close()
    callpause()
    return

def DelUser():
    '''
    Function to delete a user
    
    Creates an SQLite3 connection to maindatabase.db file.
    Asks for a username to delete.
    Queries for all usersnames in the table User_List.
    If input username matches any of the usernames from database, prompt to confirm deletion.
    '''
    uname = str(input("Enter a Username to delete:"))
    conn = sqlite3.connect("Data/maindatabase.db")
    c = conn.cursor()
    found = 0
    for row in c.execute("SELECT username FROM User_List;"):
        if(encryptDecrypt(row[0]) == uname):
            print("\nUsername " + uname + " was found!")
            print("\nAre you sure you want to delete " + uname + "'s data entry?")
            yn = input("(Y/n):")
            found = 1
            breakyn = 1
            while(breakyn):
                if(yn == 'Y'):
                    c.execute("DELETE FROM User_List WHERE username = \"" + encryptDecrypt(uname) + "\";")
                    conn.commit()
                    print("Data has been deleted!")
                    breakyn = 0

                elif(yn == 'n' or yn == 'N'):
                    print("Delete User has been cancelled.")
                    breakyn = 0
                else:
                    print("Wrong choice entered!")
                    break
    if(found == 0):
        print("\nUser was not found!")
    conn.commit()
    conn.close()
    callpause()
    return

def UserHandler():
    '''
    Function for User Menu
    '''
    while(True):
        try:
            callclearscreen()
            MenuHeaderPrinter("User's Menu")
            print("1. Add a User")
            print("2. List all Users")
            print("3. Delete a User")
            print("4. Back to previous menu")
            choice = int(input("Choose an option:"))

            if(choice == 1):
                Register(1)

            elif(choice == 2):
                ListUsers()

            elif(choice == 3):
                DelUser()

            elif(choice == 4):
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