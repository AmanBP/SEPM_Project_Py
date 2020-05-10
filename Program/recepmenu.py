from utilityfuncs import *
from userhandler import Register
from complainthandler import MakeComp
from transhandler import EnterFunds

import os

def ReceptionistMenu(CurrentUserName):

    while(True):
        try:
            callclearscreen()
            print("Receptionist Menu".center(80,'-'))
            print("1. Register")
            print("2. Receive Fees")
            print("3. Make a Complaint/Suggestion")
            print("4. Log Out")
            choice = int(input("Choose an option:"))

            if(choice == 1):
                Register(2)

            elif(choice == 2):
                EnterFunds(CurrentUserName)

            elif(choice == 3):
                MakeComp()

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