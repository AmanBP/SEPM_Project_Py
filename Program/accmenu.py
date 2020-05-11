from utilityfuncs import *
from ratehandler import VRates
from complainthandler import MakeComp
from transhandler import TransHandler

def AccountantMenu(CurrentUserName):
    '''
    Wrapper Function for Accountant Menu.
    '''
    while(True):
        try:
            callclearscreen()
            print("Accountant Menu".center(80,'-'))
            print("1. Transaction Menu")
            print("2. View Rates")
            print("3. Make a Complaint/Suggestion")
            print("4. Log Out")
            choice = int(input("Choose an option:"))

            if(choice == 1):
                TransHandler(CurrenUserName)

            elif(choice == 2):
                VRates()
                callpause()

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