import os
from utilityfuncs import callpause,callclearscreen

def ReceptionistMenu(CurrentUserName):

    breakrecepmenu = 1
    while(breakrecepmenu):

        callclearscreen()
        print("Receptionist Menu".center(80,'-'))
        print("1. Register")
        print("2. Receive Fees")
        print("3. Make a Complaint/Suggestion")
        print("4. Log Out")
        choice = int(input("Choose an option:"))

        if(choice == 1):
            #Register(2)
            pass

        elif(choice == 2):
            #Fees(CurrentUserName)
            pass

        elif(choice == 3):
            #MakeComp()
            pass
        
        elif(choice == 4):
            breakrecepmenu = 0

        else:
            print("Wrong Choice, Please choose a correct option:")
            callpause()

    return