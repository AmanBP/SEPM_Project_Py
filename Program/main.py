from encryptor import encryptDecrypt
from prettytable import PrettyTable
import sqlite3
import os
import getpass
import time

def main():
    breakmainwhile = 1
    somechar = ''

    while(breakmainwhile):

        os.system('cls' if os.name == 'nt' else 'clear')
        print("PROGRAM MAIN MENU".center(80,'-'))
        print("1.Login")
        print("2.Exit")
        choice = int(input("Choose an option:"))

        if(choice==1):

            breakusernameinput = 1

            while(breakusernameinput):

                os.system('cls' if os.name == 'nt' else 'clear')
                Uname = str(input("Enter a Username:\n"))
                sqlite3conn = sqlite3.connect('../Data/maindatabase.db')
                sqlite3cursor = sqlite3conn.cursor()
                found = 0
                for row in sqlite3cursor.execute("SELECT * FROM User_List"):
                    
                    if(encryptDecrypt(row[0]) == Uname):

                        os.system('cls' if os.name == 'nt' else 'clear')
                        print("Username Found!\n\nWelcome " + Uname )
                        found = 1
                        password = " "
                        breakpassloop = 1
                        passfailcount = 0

                        while(breakpassloop):

                            print("Enter your password:")
                            password = getpass.getpass()

                            if ( encryptDecrypt(row[1]) == password ):
                                
                                os.system('cls' if os.name == 'nt' else 'clear')
                                print("Please Wait...")
                                time.sleep(0.7)
                                os.system('cls' if os.name == 'nt' else 'clear')
                                print("Logged In Succesfully!")
                                somechar = input("Enter any key to continue...")

                                if (row[2] == 1):

                                    #AdminMenu(Uname)
                                    print("In Admin Menu")
                                    sqlite3conn.close()
                                    somechar = input("Enter any key to continue...")
                                    breakpassloop = 0
                                    breakusernameinput = 0

                                elif (row[2] == 2):

                                    #AdminMenu(Uname)
                                    sqlite3conn.close()
                                    print("In Accountant Menu")
                                    somechar = input("Enter any key to continue...")
                                    breakpassloop = 0
                                    breakusernameinput = 0

                                #ADD the rest DONT FORGET
                                #Need to check database locks once menus are implemented.

                            else:

                                print("Incorrect Password!")
                                passfailcount +=1
                                if(passfailcount == 3 ):

                                    print("You have entered the wrong password 3 times.\nExiting to program menu!")
                                    somechar = input("Enter any key to continue...")
                                    breakpassloop = 0
                                    breakusernameinput = 0
                        
                        sqlite3conn.close()
                        break
                if(found==0):
                    
                    print("Username Not found, Please register or try again!!")
                    somechar = input("Enter any key to continue...")
                    breakusernameinput = 0
                    sqlite3conn.close()
                    break
                
                else:
                    sqlite3conn.close()
                    break
                            
        elif (choice==2):

            print("\n" + " Exiting ".center(40,"!"))
            somechar = input("Enter any key to continue...")  
            breakmainwhile = 0

        else:

            print("\n" + " Wrong option selected ".center(40,"!"))
            somechar = input("Enter any key to continue...")
            breakmainwhile = 0
    return

if __name__ == "__main__":
    main()
