from utilityfuncs import *
from complainthandler import MakeComp

def gym_user_menu():
    '''
    Gym User Wrapper Function.
    '''
    while(True):
        try:
            callclearscreen()
            MenuHeaderPrinter("Gym User's Menu")
            print("1. Pay Fees")
            print("2. Make a Complaint/Suggestion")
            print("3. Change Plans")
            print("4. Logout")
            choice = int(input("Choose an option:"))

            if(choice == 1):
                print("Please Visit the receptionist for this option!")
                callpause()

            elif(choice == 2):
                MakeComp()

            elif(choice == 3):
                print("Please Visit the receptionist for this option!")
                callpause()

            elif(choice == 4):
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