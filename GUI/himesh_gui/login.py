import sys
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox
from database import Database
from Home import Toplevel1 as home

class Toplevel1:

    def jump_home(self):
        self.top.destroy()
        home()

    def Cancel_login(self):
        msg = messagebox.askyesno('Login page','Are you sure, you want to cancel login?')
        if (msg):
            exit()
    
    def login_usr(self):
        conn = Database()
        name = self.Entry_userid.get()
        password = self.Entry_passwd.get()
        query = '''select * from detail where name = "'''+name+'''" and pwd = "'''+password+'''";'''
        data = conn.run(query)
        nm = ''
        pw = ''
        for i in data:
            nm = i[0]
            pw = i[2]

        if (nm == name) and (pw == password):
            self.jump_home()
        else:
            self.Label_warning['text'] = "invalid username or password!"

    def __init__(self):

        self.top = tk.Tk()
        '''This class configures and populates the toplevel window.
           self.top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        font10 = "-family {Berlin Sans FB Demi} -size 12 -weight bold"
        font9 = "-family {ROG Fonts} -size 20"

        self.top.geometry("600x450+650+150")
        self.top.minsize(148, 1)
        self.top.maxsize(1924, 1055)
        self.top.resizable(0, 0)
        self.top.title("Login")
        self.top.configure(background="#0080ff")

        self.Button_login = tk.Button(self.top)
        self.Button_login.place(relx=0.367, rely=0.667, height=43, width=89)
        self.Button_login.configure(activebackground="#004b97")
        self.Button_login.configure(activeforeground="white")
        self.Button_login.configure(activeforeground="#f9f9f9")
        self.Button_login.configure(background="#399cff")
        self.Button_login.configure(disabledforeground="#a3a3a3")
        self.Button_login.configure(font=font10)
        self.Button_login.configure(foreground="#000000")
        self.Button_login.configure(highlightbackground="#d9d9d9")
        self.Button_login.configure(highlightcolor="black")
        self.Button_login.configure(pady="0")
        self.Button_login.configure(text='''Login''')
        self.Button_login.configure(command = self.login_usr)

        self.Button_cancel = tk.Button(self.top)
        self.Button_cancel.place(relx=0.55, rely=0.667, height=43, width=86)
        self.Button_cancel.configure(activebackground="#004b97")
        self.Button_cancel.configure(activeforeground="white")
        self.Button_cancel.configure(activeforeground="#fcfcfc")
        self.Button_cancel.configure(background="#399cff")
        self.Button_cancel.configure(disabledforeground="#a3a3a3")
        self.Button_cancel.configure(font=font10)
        self.Button_cancel.configure(foreground="#000000")
        self.Button_cancel.configure(highlightbackground="#d9d9d9")
        self.Button_cancel.configure(highlightcolor="black")
        self.Button_cancel.configure(pady="0")
        self.Button_cancel.configure(text='''Cancel''')
        self.Button_cancel.configure(command=self.Cancel_login)

        self.Entry_userid = tk.Entry(self.top)
        self.Entry_userid.place(relx=0.333, rely=0.378, height=34, relwidth=0.44)
        self.Entry_userid.configure(background="#399cff")
        self.Entry_userid.configure(disabledforeground="#a3a3a3")
        self.Entry_userid.configure(font="TkFixedFont")
        self.Entry_userid.configure(foreground="#000000")
        self.Entry_userid.configure(insertbackground="black")

        
        self.Label_userid = tk.Label(self.top)
        self.Label_userid.place(relx=0.117, rely=0.378, height=36, width=80)
        self.Label_userid.configure(background="#0080ff")
        self.Label_userid.configure(disabledforeground="#a3a3a3")
        self.Label_userid.configure(font=font10)
        self.Label_userid.configure(foreground="#000000")
        self.Label_userid.configure(text='''User Id''')

        self.Label_password = tk.Label(self.top)
        self.Label_password.place(relx=0.117, rely=0.489, height=36, width=88)
        self.Label_password.configure(background="#0080ff")
        self.Label_password.configure(disabledforeground="#a3a3a3")
        self.Label_password.configure(font=font10)
        self.Label_password.configure(foreground="#000000")
        self.Label_password.configure(text='''Password''')

        self.Entry_passwd = tk.Entry(self.top)
        self.Entry_passwd.place(relx=0.333, rely=0.489, height=34, relwidth=0.44)
        self.Entry_passwd.configure(background="#399cff")
        self.Entry_passwd.configure(disabledforeground="#a3a3a3")
        self.Entry_passwd.configure(font="TkFixedFont")
        self.Entry_passwd.configure(foreground="#000000")
        self.Entry_passwd.configure(insertbackground="black")

        self.Labelframe_login = tk.LabelFrame(self.top)
        self.Labelframe_login.place(relx=0.367, rely=0.044, relheight=0.167, relwidth=0.25)
        self.Labelframe_login.configure(relief='groove')
        self.Labelframe_login.configure(foreground="black")
        self.Labelframe_login.configure(background="#0080ff")

        self.Label_lg = tk.Label(self.Labelframe_login)
        self.Label_lg.place(relx=0.067, rely=0.133, height=56, width=127, bordermode='ignore')
        self.Label_lg.configure(background="#0080ff")
        self.Label_lg.configure(disabledforeground="#a3a3a3")
        self.Label_lg.configure(font=font9)
        self.Label_lg.configure(foreground="#000000")
        self.Label_lg.configure(text='''LOGIN''')

        text = tk.StringVar()
        text = ''
        self.Label_warning = tk.Label(self.top, text = text)
        self.Label_warning.place(relx=0.233, rely=0.244, height=36, width=252)
        self.Label_warning.configure(background="#0080ff")
        self.Label_warning.configure(disabledforeground="#a3a3a3")
        self.Label_warning.configure(foreground="#000000")
        self.Label_warning.configure(font=font10)

        self.top.mainloop()

if __name__ == "__main__":
    Toplevel1()