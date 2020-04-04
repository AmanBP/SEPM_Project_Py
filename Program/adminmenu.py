import os
from backuputility import Backup
from utilityfuncs import callclearscreen,callpause,MenuHeaderPrinter
from userhandler import UserHandler
from complainthandler import ComplaintHandler
from attendance import AttendanceHandler
from ratehandler import RateHandler
from transhandler import TransLogs

def AdminMenu(CurrentUserName):
    
    breakadminmenu = 1
    while(breakadminmenu):

        callclearscreen()
        MenuHeaderPrinter("Admin & Owner Menu")
        print("1. Attendance Menu")
        print("2. Rates Menu")
        print("3. Users Menu")
        print("4. Access Transaction Logs")
        print("5. Create Backups")
        print("6. Complaints/Suggestions Menu")
        print("7. Log Out")
        choice = int(input("Choose an option:"))
        
        if(choice == 1):
            AttendanceHandler()

        elif(choice == 2):
            RateHandler()
        
        elif(choice == 3):
            UserHandler()

        elif(choice == 4):
            TransLogs()

        elif(choice == 5):
            Backup()

        elif(choice == 6):
            ComplaintHandler()

        elif(choice == 7):
            print("Logging Out.")
            breakadminmenu = 0
    
        else:
            print("\nWrong Choice! Please choose a correct option:")
            callpause()

    return
