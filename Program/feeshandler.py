from utilityfuncs import callpause,callclearscreen,MenuHeaderPrinter
from ratehandler import VRates
from transhandler import EnterFunds

def FeesHandler(uid):

    breakfeesmenu = 0
    while(not breakfeesmenu):

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
            breakfeesmenu = 1
    
        else:
            print("\nWrong Choice! Please choose a correct option:")
            callpause()
    return