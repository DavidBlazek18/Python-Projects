 # Python:   Ver. 3.8

    # Author:   David Blazek

    # Program:  File Transfer Assignment, Part 3 (Python Course Assignment Page 269, The Tech Academy)

import shutil                       # This module's functions are provided which support file copying and removal.
import os                           # os and sys modules provide numerous tools to deal with filenames, paths, directories.
import datetime                     # The datetime module supplies classes for manipulating dates and times.
import os.path, time                # This module implements some useful functions on pathnames.
import webbrowser                   # Imports the module which allows the display of Web-based documents to users.
import tkinter as tk                # Imports the toolkit which enables the building of a GUI.
from tkinter import *               # Allows all modules to be used from the toolkit. 
from tkinter.filedialog import askdirectory


def daily_scan():                                                           # Defining a function called daily_scan.
    source = listBox1.get(0, END)[0]# List the source of the folder where file names will be examined.
    widgetVar = v1.get()
    destination = listBox2.get(0, END)[0]    # List the destination folder where files less than 1-day old will be sent.

    newVar = os.listdir(source)                     # Made new variable so we can have a list of .txt files. If this is not done and the
                                                    # for statement below says "for filename in source" it will move the whole folder. 


    for filename in newVar:                             # Iterating through a list of file names in our source folder.
        if filename.endswith(".txt"):                   # Want list of .txt files only.
            abPath = os.path.join(source, filename)     # Finding the absolute path by joining the source w/file name.
            print (abPath)                              # Verifying the absolute path by printing it to console.
            currentTimeInSeconds = time.time()                      # Get the time right now.
            oldFilesAgeInSeconds = os.path.getmtime(abPath)         # Sets the variable for finding age of Modified files.
                                                                   
            x = (currentTimeInSeconds)-(oldFilesAgeInSeconds)       # Gets the difference in seconds between. 
                                                                    # current time vs. time when a file was modified (will want to move any
                                                                    # file Modified within 24 hours (86400 seconds).
            print(x)                                                # Prints age of file to console.
            
            if x <= (86400):                        # Determining if the age of the modified file is less than 24 hours.
                print(x)                            # Prints age of file to console.
                print(filename)                     # Prints the filename of modified files less than 24 hours old.
            
                shutil.move(abPath, destination)    # Move the files less than 24 hours old to their new folder destination.


win = Tk()                  # Allows tkinter to install a window widget and assigns the variable "f" as the window frame
f = Frame(win)              
v1 = StringVar()             # Creates the variable-1 for the new abPath where we will SET our listbox.        



def getSource():                ###connect to button1  see link in comment at line 70
    a = askdirectory()
    listBox1.insert(0, a)

def getDestination():           ###connect to button2
    b = askdirectory()
    listBox2.insert(0, b)



button1 = Button(win, width= 25, text="Browse Daily Folder...", command=lambda: getSource())    # Creates the button variable and button name "Daily Folder". This link makes it so function doesn't 
button1.grid(row=0, column=0, padx=10, pady=10, ipadx=10, sticky="W")                           # run automatically https://pythonprogramming.net/passing-functions-parameters-tkinter-using-lambda/

listBox1 = Listbox(win, height=1, width=100)                                           # Creates the listbox for the files in the Daily Folder.  
listBox1.grid(row=0, column=3, columnspan=2, padx=10, pady=10)                      ### <--- From the placement of this listbox in your gui, it would make more sense that this would hold your source path, which would only require an Entry box

button2 = Button(win, width= 25, text="Browse Destination Folder...", command=lambda: getDestination())                 # Creates the button variable and button name "Destination Folder".
button2.grid(row=1, column=0, padx=10, pady=10, ipadx=10, sticky="W")

listBox2 = Listbox(win, height=1, width=100)                                           # Creates the listbox for the files in the Daily Folder.
listBox2.grid(row=1, column=3, columnspan=2, padx=10, pady=10)

button3 = Button(win, width= 25, text="Click here for immediate copying \nof Daily Files to Destination Folder", command=lambda: daily_scan())
button3.grid(row=2, column=0, columnspan=1, rowspan=2, padx=10, pady=10, ipadx=10, sticky="W")

button4 = Button(win, text="Close", command=lambda: quit())                         #### The "quit" function is defined in Line_19. 
button4.grid(row=2, column=4, padx=10, pady=10, ipadx=10, sticky="E")

