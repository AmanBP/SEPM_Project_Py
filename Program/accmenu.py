import os
from utilityfuncs import callclearscreen,callpause
def AccountantMenu(CurrentUserName):

    breakaccmenu = 1
    while(breakaccmenu):

        callclearscreen()
        print("Accountant Menu".center(80,'-'))
        print("1. Transaction Menu")
        print("2. View Rates")
        print("3. Make a Complaint/Suggestion")
        print("4. Log Out")
        choice = int(input("Choose an option:"))

        if(choice == 1):
            #TransactionHandler(CurrentUserName)
            pass

        elif(choice == 2):
            #Vrates()
            pass

        elif(choice == 3):
            #MakeComplaint()
            pass
        
        elif(choice == 4):
            breakaccmenu = 0
            
        else:
            print("Wrong Choice, Please choose a correct option:")
            callpause()
    
    return