import sys
import tkinter as tk
import tkinter.ttk as ttk
from database import Database

class DATA_VIEW:

    def show_data(self):
        conn = Database()
        data = conn.view()
        name = []
        email = []
        password = []
        for record in data:
            name.append(record[0])
            email.append(record[1])
            password.append(record[2])
        
        for i in range(len(name)):
            self.Text1.insert(tk.END,str("\nname = "+str(name[i])+"\nemail = "+str(email[i])+"\npassword = "+str(password[i])+"\n"))            

    def __init__(self):
        
        self.top = tk.Tk()
        '''This class configures and populates the self.toplevel window.
           self.top is the self.toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        font9 = "-family {Segoe UI Emoji} -size 10"
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.configure('.',font="TkDefaultFont")
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])

        self.top.geometry("600x450+650+150")
        self.top.minsize(152, 1)
        self.top.maxsize(1924, 1055)
        self.top.resizable(0, 0)
        self.top.title("DATA VIEW")
        self.top.configure(background="#d9d9d9")

        self.Label1 = tk.Label(self.top)
        self.Label1.place(relx=0.083, rely=0.044, height=47, width=523)
        self.Label1.configure(activebackground="#c0c0c0")
        self.Label1.configure(activeforeground="#000000")
        self.Label1.configure(background="#c0c0c0")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(text='''VIEW''')

        self.TButton1 = ttk.Button(self.top)
        self.TButton1.place(relx=0.117, rely=0.2, height=51, width=479)
        self.TButton1.configure(takefocus="")
        self.TButton1.configure(text='''SHOW''')
        self.TButton1.configure(command = self.show_data)

        self.Text1 = tk.Text(self.top)
        self.Text1.place(relx=0.1, rely=0.378, relheight=0.596, relwidth=0.857)
        self.Text1.configure(background="white")
        self.Text1.configure(font=font9)
        self.Text1.configure(foreground="black")
        self.Text1.configure(highlightbackground="#d9d9d9")
        self.Text1.configure(highlightcolor="black")
        self.Text1.configure(insertbackground="black")
        self.Text1.configure(selectbackground="#c4c4c4")
        self.Text1.configure(selectforeground="black")
        self.Text1.configure(wrap="word")

        self.top.mainloop()

    @staticmethod
    def popup1(event, *args, **kwargs):
        Popupmenu1 = tk.Menu(root, tearoff=0)
        Popupmenu1.configure(activebackground="#f9f9f9")
        Popupmenu1.configure(activeborderwidth="1")
        Popupmenu1.configure(activeforeground="black")
        Popupmenu1.configure(background="#d9d9d9")
        Popupmenu1.configure(borderwidth="1")
        Popupmenu1.configure(disabledforeground="#a3a3a3")
        Popupmenu1.configure(font="-family {Segoe UI} -size 10")
        Popupmenu1.configure(foreground="black")
        Popupmenu1.post(event.x_root, event.y_root)





