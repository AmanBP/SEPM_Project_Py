import shutil
import os
from utilityfuncs import MenuHeaderPrinter,callpause,callclearscreen

def Backup():
    callclearscreen()
    MenuHeaderPrinter("Backup")
    loc = input("Enter a folder to backup the Data folder:")
    if(os.path.exists(loc)):
        shutil.copy2("./Data/maindatabase.db",loc)
        print("Backup has been made!")
        print("To see backed-up files, open this folder in file explorer: {}".format(loc))
    else:
        print("Folder does not exist,Creating a folder....")
        os.mkdir(loc)
        shutil.copy2("./Data/maindatabase.db",loc)
        print("Backup has been made!")
        print("To see backed-up files, open this folder in file explorer: {}".format(loc))
    callpause()
    return