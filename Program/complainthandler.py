from utilityfuncs import *
import sqlite3
from prettytable import from_db_cursor

def MakeComp():
    '''
    Function to enter a complaint into a database.
    '''
    cs = str(input("Please enter your complaint or suggestion:"))
    conn = sqlite3.connect("Data/maindatabase.db")
    c = conn.cursor()
    c.execute("INSERT INTO CS VALUES(NULL,\"" + cs + "\")")
    print("The complaint / suggestion has been registered!")
    conn.commit()
    conn.close()
    callpause()

def ViewAllComp():
    '''
    Funtion to View all complaints.

    Complaints are read from the table called "CS".

    '''
    statement = "SELECT * FROM CS"
    conn = sqlite3.connect("Data/maindatabase.db")
    c = conn.cursor()
    c.execute(statement)
    x = from_db_cursor(c)
    print("Current Complaints / Suggestions are:")
    print(x)
    conn.commit()
    conn.close()
    callpause()

def DeleteAComp():
    '''
    Function to delete a complaint.

    ID in CS table is an auto-incrementing integer, one of SQL's features.
    Hence, no random ID is generated.
    '''
    ViewAllComp()
    conn = sqlite3.connect("Data/maindatabase.db")
    c = conn.cursor()
    cnum = int(input("Select ID number of complaint to be removed:"))
    gotconfirm = 1
    confirm = "n"
    while(gotconfirm):
        confirm = str(input("Are you sure?(Y/n):"))
        if(confirm == "Y" or confirm == "n" or confirm == "N"):
            gotconfirm = 0
        else:
            print("Invalid choice!")
    if(confirm == "Y"):
        print("Deleting entry with ID number: ", cnum)
        statement = "DELETE FROM CS WHERE ID = " + str(cnum)
        c.execute(statement)
        print("Done")
        conn.commit()
    else:
        print("Aborting Delete operation !")
    conn.close()
    callpause()


def ComplaintHandler():
    '''
    Wrapper fuction to manage complaints.
    '''
    while(True):
        try:
            callclearscreen()
            MenuHeaderPrinter("Complaints/Suggestion Menu")
            print("1. Add a complaint or suggestion")
            print("2. View all complaints and suggestions")
            print("3. Delete a suggestion or complaint")
            print("4. Go Back")
            choice = int(input("Choose an option:"))

            if(choice == 1):
                MakeComp()

            elif(choice == 2):
                ViewAllComp()

            elif(choice == 3):
                DeleteAComp()

            elif(choice == 4):
                raise BreakMenu

            else:
                raise WrongChoiceError

        except ValueError:
            print("Invalid Character has been entered!")
            callpause()
        
        except BreakMenu:
            break
        
        except WrongChoiceError:
            print("Wrong Choice, Please choose a correct option!")
            callpause()
            
    return