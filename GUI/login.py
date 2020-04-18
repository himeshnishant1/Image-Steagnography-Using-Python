from tkinter import *
import tkinter.messagebox 
from tkinter import ttk
import random
import time
import datetime 

def main():
    root = Tk()
    app = Window1(root)

class Window1:
    def __init__(self,master):
        self.master = master
        self.master.title("Stegno Login System")
        self.master.geometry("1200x700+110+55")
        self.master.config(bg='powder blue') #color
        self.frame = Frame(self.master,bg='powder blue') #color
        self.frame.pack()

        self.Username = StringVar
        self.Password = StringVar

        self.tit= Label(self.frame,text="Stegno Login System",font=('arial',50,'bold'),bg='powder blue',fg='black')
        self.tit.grid(row = 0,columnspan =2,pady=40)
        #*******************************************************************************************************************
        self.loginFrame = Frame(self.frame, width=1350, height=600, font=(
            'arial', 50, 'bold'), bg='powder blue', fg='black')
        self.btnlogin =Button(self.frame,text='Login',width = 17 ,command = self.new_window)
        self.btnlogin.grid(row = 3,column=0)
        self.btnlogin = Button(self.frame, text='Reset',width=17)
        self.btnlogin.grid(row=3, column=1)
        self.btnlogin = Button(self.frame, text='Exit', width=17, command=self.exit())
        self.btnlogin.grid(row=3, column=3)

        def new_window(self):
            self.new_window = Toplevel(self.master)
            self.app =Window2(self.newWindow)


class Window2:
    def __init__(self, master):
        self.master = master
        self.master.title("Stegnography System")
        self.master.geometry("1200x700+110+55")
        self.master.config(bg='blue')  # color
        self.frame = Frame(self.master, bg='powder blue')  # color
        self.frame.pack()



if __name__ == "main__":
    main()
    
