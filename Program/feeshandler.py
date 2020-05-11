from utilityfuncs import *
from ratehandler import VRates
from transhandler import EnterFunds

def FeesHandler(uid):

    while(True):
        try:
            callclearscreen()
            MenuHeaderPrinter("Fees Menu")
            print("1. View Current Rates")
            print("2. Recieve Fees")
            print("3. Go Back")
            choice = int(input("Choose an option:"))

            if(choice == 1):
                VRates()

            elif(choice == 2):
                EnterFunds(uid)

            elif(choice == 3):
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