import sqlite3
from utilityfuncs import *
from prettytable import from_db_cursor

def VRates():
    print("Current Rates are:\n")
    sections = ["Membership_Fees","Gym_Trainer_Fees","Dietician_Fees"]
    columns = "Monthly,QuadAnnual,BiAnnual,Annual"
    command1 = "SELECT "
    command2 = " FROM "
    conn = sqlite3.connect("Data/maindatabase.db")
    c = conn.cursor()
    for i in range(0,3):
        command = command1 + columns + command2 + sections[i]
        c.execute(command)
        x = from_db_cursor(c)
        print((str(i+1)) + ". " + sections[i])
        print(x)
        print()
    conn.close()
    return

def CRates():
    VRates()
    gotcorrectnum = 0
    choice = 9000
    span = ["0","Monthly","QuadAnnual","BiAnnual","Annual"]
    types = ["0","Membership_Fees","Gym_Trainer_Fees","Dietician_Fees"]
    while(not gotcorrectnum):
        choice = int(input("Choose which Rate you would like to change:(-1 to cancel) "))
        if((choice >= 1 and choice <=3) or(choice == -1)):
            gotcorrectnum = 1
        else:
            print("You have Entered an invalid option. Please enter a correct option!")
    
    if(choice == -1):
        print("Returning to Rates Menu.")
        callpause()
        return

    else:
        print("You have chosen to edit {}.".format(types[choice]))
        gotcorrectnum = 0
        val = 9000
        while(not gotcorrectnum):
            val = int(input("Please enter column number of plan you want to change(-1 to cancel, allowed values 1-4):"))
            if((val>= 1 and val<=4) or (val == -1)):
                gotcorrectnum = 1
            else:
                print("You have Entered an invalid option. Please enter a correct option!")
        
        if(val == -1):
            print("Returning to Rates Menu.")
            return
        else:
            newvalue = int(input("Please enter a new rate for {} rate:".format(span[val])))
            conn = sqlite3.connect("Data/maindatabase.db")
            c = conn.cursor()
            statement = "UPDATE " + types[choice] + " SET " + span[val] + "=" + str(newvalue) + " WHERE ID=1;"
            c.execute(statement)
            conn.commit()
            print("Rate Has been updated in database!")
            conn.close()
    print("Returning to Rates Menu")
    return

def RateHandler():
    while(True):
        try:
            callclearscreen()
            MenuHeaderPrinter("Rates Menu")
            print("1. View Rates")
            print("2. Change Rates")
            print("3. Go Back")
            choice = int(input("Choose an option:"))

            if(choice == 1):
                VRates()
                callpause()

            elif(choice == 2):
                CRates()
                callpause()

            elif(choice == 3):
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