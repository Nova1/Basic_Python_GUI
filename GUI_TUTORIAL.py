#!/user/python/lib 


#imports 
import tkinter as tk
from tkinter import *
from sys import *
import os
import time


#class
class App(Frame): #The 'F' in frame has to be a captial letter as when putting a lower case 'frame' is not defined in the TkInter library.

#initialisation
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.pack() 
        self.createWidgets() #This is for the creation of the buttons.
        

#creation of the buttons
    def createWidgets(self):

        self.tutorial = tk.Button(self)
        self.tutorial["text"] = ("Tutorial Button") #This is what text is going to be shown on the button.
        self.tutorial["command"] = self.tutorial_message #When this button is pressed what is going to be carried out? This is going to be defined later on.
        self.tutoria;.pack(side="bottom") # Where the button is going to be in the GUI

        self.QUIT = tk.Button(self, text="QUIT", fg="red", command=root.destroy) #'fg' is the colour, 'root.destroy' is basically the command in which to close the GUI.
        self.QUIT.pack(side="bottom") #Where the button is going to be in the GUI.

        
        

    
    def tutorial_message(self): #As mentioned above this is whats going to take place after the button is pressed.
        print("Hello World!")


#Loop, if this isn't here the GUI will NOT work.
root = tk.Tk()
app = App(master=root)
app.mainloop()

        






        
        
        
