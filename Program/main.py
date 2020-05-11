from utilityfuncs import *
from prettytable import PrettyTable
from adminmenu import AdminMenu
from accmenu import AccountantMenu
from recepmenu import ReceptionistMenu
from gymstaffhandler import Gym_Staff_Menu
from gymuserhandler import gym_user_menu
from userhandler import newAdminReg
import pathlib as pl
import sqlite3
import os
import getpass
import time

def main():

    while(True):
        try:
            callclearscreen()
            print("PROGRAM MAIN MENU".center(80,'-'))
            print("1.Login")
            print("2.Exit")
            choice = int(input("Choose an option:"))
            if(choice==1):
                breakusernameinput = 1

                sqlite3conn = sqlite3.connect('Data/maindatabase.db')
                sqlite3cursor = sqlite3conn.cursor()
                sqlite3cursor.execute("SELECT count(*) FROM User_List")
                value = sqlite3cursor.fetchall()
                checkforadminid = False
                gotproperchoice = False
                if(value[0][0] == 0):
                    while(not gotproperchoice):
                        yn = input("Looks like this is the first time this program is run,\nWould you like to create a new administrator cridential?(y/n):")
                        if(yn == "y" or yn == "Y"):
                            gotproperchoice = True
                            newAdminReg()
                            checkforadminid = True
                        elif(yn == "N" or yn == "n"):
                            sqlite3conn.close()
                            gotproperchoice = True
                            print("This Program cannot continue without atleast one Admin Cridential.\nExiting!")
                            callpause()
                            breakmainwhile = 0
                        else:
                            print("Wrong option Selected!")
                            callpause()
                else:
                    checkforadminid = True

                while(breakusernameinput and checkforadminid):
                    if(gotproperchoice == True):
                        print("Entering back into Login",end = ',')
                        callpause()

                    callclearscreen()
                    Uname = str(input("Enter a Username:\n"))
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

                                        sqlite3conn.close()
                                        Gym_Staff_Menu(Uname)
                                        breakpassloop = 0
                                        breakusernameinput = 0

                                    elif (row[2] == 5):

                                        sqlite3conn.close()
                                        gym_user_menu()
                                        breakpassloop = 0
                                        breakusernameinput = 0

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

if __name__ == "__main__":
    main()
