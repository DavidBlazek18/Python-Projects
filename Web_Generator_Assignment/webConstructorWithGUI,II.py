
    # Python:   Ver. 3.7

    # Author:   David Blazek

    # Program:  Web Page Generator (Python Course Assignment Page 250, The Tech Academy)

 
                    
import webbrowser                                                           # imports the module which allows the display of Web-based documents to users.

import tkinter as tk                                                        # Imports the toolkit which enables the building of a GUI.
from tkinter import *                                                       # Allows all modules to be used from the toolkit. 

class ParentWindow(Frame):                                                  # Class parent window and our Frame inherits the attributes
    def __init__ (self, master):                                            # Dunder initialize and pass in class self and named master(can be any name)
        Frame.__init__ (self)                                               # The frame is going to initialize itself and then run the code below.
        



    # put all the above into function


win = Tk()                                                                  # Allows tkinter to install a window widget and assigns the variable "f" as the window frame
f = Frame(win)


l = Label(win, text="Enter new message below then click the SUBMIT button.")# Creates the label variable and label instructions.

v = StringVar()                                                             # Creates the variable for the new message in Entry window which we can get (with Get func.).
e = Entry(win, width = 80, textvariable = v)
b1 = Button(f, text="SUBMIT")                                               # Creates the button variable and button name.
l.pack(pady = 10)                                                                     
e.pack(padx = 10)                                                           # Uses the "pack" method to vertically align the label, entry window and SUBMIT button in the frame.
b1.pack(pady = 10)
f.pack()

def but1():                                                                 # defining the function for our button.
    print("The SUBMIT button was pushed")                                   # This shows up in the console that the button was pushed.
    newVariable = e.get()
    fileToWrite = open("webConstructor.html", "w")                              # Defines the variable that opens an HTML document the user can write to.
    newTextToWrite = "Stay tuned for our amazing summer sale!"                  # Defines the variable for the text string a user can change in the script.
    newScript = ("<html><body><h1>" + newVariable + "</h1></body></html>")   # Defines the variable which concatenates the python script with new text from the user.
    fileToWrite.write(newScript)                                                # Overwrites the HTML file with a new script which includes the new text.
    fileToWrite.close()                                                         # Close file per Best Coding Practices.
    webbrowser.open_new_tab("webConstructor.html")                              # Runs the new HTML file in the browser.
        
b1.configure(command=but1)
v.get()
webbrowser.get()





if __name__ == "__main":                                                    # Controls program flow. All lines below are read and then the above code is run (if needed).
    root = Tk()                                                             # Instantiates the TKinter...
    App = ParentWindow(root)                                                # then passes it over to our class program ParentWindow...
    root.mainloop()                                                         # and create a main loop for the program to run so it constantly stays open.
    

#self.btnSubmit = Button(self.master, text='Submit', width=10, height=2, command=self.submit)   # (Code contained in TK GUI Video Part 5)
