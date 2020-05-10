from utilityfuncs import *
import sqlite3
from prettytable import from_db_cursor

def getproperdate(somedatestring):
    bad_chars = ['-','_','\\','/']
    newdate = ""
    for i in somedatestring:
        if(i not in bad_chars):
            newdate += i
    return newdate

def AttendanceCheck(uid):
    conn = sqlite3.connect("./Data/maindatabase.db")
    c = conn.cursor()
    datelist = []
    count = 0
    command = '''SELECT name FROM sqlite_master WHERE type='table' AND name LIKE 'date_%';'''
    for row in c.execute(command):
        datelist.append(str(row[0]))
        count += 1
    for i in range(count):
        print("Attendace of : {}".format(datelist[i][5:]))
        command = "SELECT * FROM " + datelist[i] + ''' WHERE ID="{}"'''.format(uid) + ";"
        c.execute(command)
        x = from_db_cursor(c)
        print(x)
    conn.close()
    callpause()
    
def createdatetable(date):
    properdate = getproperdate(date)
    command = "CREATE TABLE date_" + properdate + "(ID varchar(100),Attendance CHARACTER(1));"
    conn = sqlite3.connect("./Data/maindatabase.db")
    c = conn.cursor()
    c.execute(command)
    print("Entry Successfully Created.")
    conn.commit
    conn.close()

def insertintodatetable(date,id,pora):
    properdate = getproperdate(date)
    command = "INSERT INTO date_" + properdate + " VALUES(\"" + str(id) + "\",\"" + str(pora) + "\");"
    conn = sqlite3.connect("./Data/maindatabase.db")
    c = conn.cursor()
    c.execute(command)
    print("Succesfully Entered Attendance!")
    conn.commit()
    conn.close()

def checkifdatetableexists(date):
    properdate = getproperdate(date)
    command = "SELECT count(*) FROM sqlite_master WHERE type='table' AND name='date_" + properdate + "';"
    conn = sqlite3.connect("./Data/maindatabase.db")
    c = conn.cursor()
    c.execute(command)
    value = c.fetchone()
    conn.close()
    if(value[0] == 0):
        return 0 
    else:
        return 1

def getattendanceofdate(date):
    properdate = getproperdate(date)
    command = "SELECT * FROM date_" + properdate + ";"
    conn = sqlite3.connect("./Data/maindatabase.db")
    c = conn.cursor()
    c.execute(command)
    x = from_db_cursor(c)
    print("Attendance of {}:".format(date))
    print(x)
    conn.close()
    
def AttendanceHandler():
    breakattendancemenu = 1
    while(breakattendancemenu):
        callclearscreen()
        MenuHeaderPrinter("Attendance Menu")
        print("1. Create Entry of a date")
        print("2. Insert Attendance of a date")
        print("3. View Attendance of a date")
        print("4. Check if date entry exists")
        print("5. Go Back")
        choice = int(input("Enter a choice:"))
        if(choice == 1):
            date = input("Please enter a date in (DD MM YYYY format)(braces allowed: ('_','-','\\','/')):")
            print("Creating a date entry for", date)
            createdatetable(date)
            callpause()

        elif(choice == 2):
            date = input("Please enter a date in (DD MM YYYY format)(braces allowed: ('_','-','\\','/')):")
            exist = checkifdatetableexists(date)
            if(exist == 0):
                print("Date entry was not found.")
                breakcheckoption = 1
                choice = "0"
                while(breakcheckoption):
                    print("Would you like to create an entry for",date,"?(Y|n)")
                    choice = input()
                    if(choice == "Y" or choice == "n" or choice == "N" or choice == "y"):
                        breakcheckoption = 0
                if(choice == "Y" or choice == "y"):
                    print("Creating a date entry for",date)
                    createdatetable(date)
                else:
                    print("Alright then, returning to menu.")
            else:
                print("Date Entry was found!")    
                num_of_entries = int(input("Please enter the number of attendances you want to enter(0 to cancel):"))
                for i in range(num_of_entries):
                    tryagainuname = 1
                    while(tryagainuname):
                        uname = input("Please enter a username to enter attendance of:")
                        command = "SELECT username FROM User_List;"
                        conn = sqlite3.connect("./Data/maindatabase.db")
                        c = conn.cursor()
                        found = 0
                        for row in c.execute(command):
                            if(encryptDecrypt(uname) == str(row[0])):
                                found = 1
                                break
                        conn.close()
                        if(found == 1):
                            gotcorrectattendance = 1
                            while(gotcorrectattendance):
                                pora = input("Please enter a P for Present or A for Absent:")
                                if(pora == "P" or pora == "A"):
                                    gotcorrectattendance = 0
                            insertintodatetable(date,uname,pora)
                            print("Entering data into Date Entry!")
                            tryagainuname = 0
                        else:
                            print("Username was not found, Please enter a correct username!")
            callpause()
                    
        elif(choice == 3):
            date = input("Please enter a date in (DD MM YYYY format)(braces allowed: ('_','-','\\','/')):")
            exist = checkifdatetableexists(date)
            if(exist == 1):
                print("A Date entry was found! Printing attendance:")
                getattendanceofdate(date)
            else:
                print("Date entry was not found! Please try again with another date!")
            callpause()

        elif(choice == 4):
            date = input("Please enter a date in (DD MM YYYY format)(braces allowed: ('_','-','\\','/')):")
            exists = checkifdatetableexists(date)
            if(exists == 1):
                print("Date Entry was found!")
            else:
                print("Date entry was not found!")
            callpause()

        elif(choice == 5):
            breakattendancemenu = 0    
        
        else:
            print("Wrong Choice, Please choose a correct option:")
            callpause()

    return