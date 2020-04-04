from utilityfuncs import encryptDecrypt,callclearscreen,callpause
from prettytable import PrettyTable
from adminmenu import AdminMenu
from accmenu import AccountantMenu
from recepmenu import ReceptionistMenu
import sqlite3
import os
import getpass
import time

def main():
    breakmainwhile = 1
    while(breakmainwhile):

        callclearscreen()
        print("PROGRAM MAIN MENU".center(80,'-'))
        print("1.Login")
        print("2.Exit")
        choice = int(input("Choose an option:"))

        if(choice==1):

            breakusernameinput = 1

            while(breakusernameinput):

                callclearscreen()
                Uname = str(input("Enter a Username:\n"))
                sqlite3conn = sqlite3.connect('../Data/maindatabase.db')
                sqlite3cursor = sqlite3conn.cursor()
                found = 0
                for row in sqlite3cursor.execute("SELECT * FROM User_List"):
                    
                    if(encryptDecrypt(row[0]) == Uname):

                        callclearscreen()
                        print("Username Found!\n\nWelcome " + Uname )
                        found = 1
                        password = " "
                        breakpassloop = 1
                        passfailcount = 0
                        
                        while(breakpassloop):

                            print("Enter your password:")
                            password = getpass.getpass()

                            if ( encryptDecrypt(row[1]) == password ):
                                
                                callclearscreen()
                                print("Please Wait...")
                                time.sleep(0.7)
                                callclearscreen()
                                print("Logged In Succesfully!")
                                callpause()
                                if (row[2] == 1):

                                    sqlite3conn.close()
                                    AdminMenu(Uname)
                                    breakpassloop = 0
                                    breakusernameinput = 0

                                elif (row[2] == 2):

                                    sqlite3conn.close()
                                    AccountantMenu(Uname)
                                    breakpassloop = 0
                                    breakusernameinput = 0

                                elif (row[2] == 3):

                                    sqlite3conn.close()
                                    ReceptionistMenu(Uname)
                                    breakpassloop = 0
                                    breakusernameinput = 0

                                elif (row[2] == 4):

                                    #AdminMenu(Uname)
                                    sqlite3conn.close()
                                    print("In Gym Staff Menu")
                                    callpause()
                                    breakpassloop = 0
                                    breakusernameinput = 0

                                elif (row[2] == 5):

                                    #AdminMenu(Uname)
                                    sqlite3conn.close()
                                    print("In Gym User Menu")
                                    callpause()
                                    breakpassloop = 0
                                    breakusernameinput = 0


                                #Need to check database locks once menus are implemented.

                            else:

                                print("Incorrect Password!")
                                passfailcount +=1
                                if(passfailcount == 3 ):

                                    print("You have entered the wrong password 3 times.\nExiting to program menu!")
                                    callpause()
                                    breakpassloop = 0
                                    breakusernameinput = 0
                        
                        sqlite3conn.close()
                        break
                if(found==0):
                    
                    print("Username Not found, Please register or try again!!")
                    callpause()
                    breakusernameinput = 0
                    sqlite3conn.close()
                    break
                
                else:
                    sqlite3conn.close()
                    break
                            
        elif (choice==2):

            print("\n" + " Exiting ".center(40,"!"))
            callpause()
            breakmainwhile = 0

        else:

            print("\n" + " Wrong option selected ".center(40,"!"))
            callpause()
            breakmainwhile = 0
    return

if __name__ == "__main__":
    main()
