from utilityfuncs import *
from attendance import AttendanceCheck
from complainthandler import MakeComp
from prettytable import from_db_cursor
import sqlite3

def CheckEquipmentDetails():
    '''
    Check Equipment Details Function.\

    Loads all values from Equipment Table and prints it using prettytable's table printing api.
    '''
    conn = sqlite3.connect("Data/maindatabase.db")
    command = "SELECT * FROM Equipment"
    c = conn.cursor()
    c.execute(command)
    x = from_db_cursor(c)
    print("Current Equipment Details are:")
    print(x)
    callpause()

def Gym_Staff_Menu(uid):
    '''
    Wrapper Function for Gym Staff Menu.
    '''
    while(True):

        try:
            callclearscreen()
            MenuHeaderPrinter("Gym Staff Menu")
            print("1. Salary Details")
            print("2. Attendance Check")
            print("3. Equipment Details")
            print("4. Make a Complaint/Suggestion")
            print("5. Log Out")

            choice = int(input("Choose an option:"))

            if(choice == 1):
                print("Please Talk to the accountant regarding this.")
                callpause()

            elif(choice == 2):
                AttendanceCheck(uid)

            elif(choice == 3):
                CheckEquipmentDetails()

            elif(choice == 4):
                MakeComp()

            elif(choice == 5):
                raise BreakMenu

            else:
                raise WrongChoiceError
                callpause()
        
        except ValueError:
            print("Invalid Character has been entered!")
            callpause()
        
        except BreakMenu:
            break
        
        except WrongChoiceError:
            print("Wrong Choice, Please choose a correct option!")
            callpause()
    return