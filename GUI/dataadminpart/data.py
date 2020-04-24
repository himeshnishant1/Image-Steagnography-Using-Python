import sys
import tkinter as tk
import tkinter.ttk as ttk
from data_insert 

class toplevel1:
    def __init__(self):

        self.top = tk.Tk()
        '''This class configures and populates the self.toplevel window.
           self.top is the self.toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'

        self.top.geometry("739x616+650+150")
        self.top.minsize(152, 1)
        self.top.maxsize(1924, 1055)
        self.top.resizable(1, 1)
        self.top.title("New self.toplevel")
        self.top.configure(background="#d9d9d9")
        self.top.configure(highlightbackground="#d9d9d9")
        self.top.configure(highlightcolor="black")

        self.Canvas1 = tk.Canvas(self.top)
        self.Canvas1.place(relx=0.041, rely=0.049, relheight=0.898
                , relwidth=0.939)
        self.Canvas1.configure(background="#d9d9d9")
        self.Canvas1.configure(borderwidth="2")
        self.Canvas1.configure(highlightbackground="#000000")
        self.Canvas1.configure(highlightcolor="black")
        self.Canvas1.configure(insertbackground="#0080c0")
        self.Canvas1.configure(relief="ridge")
        self.Canvas1.configure(selectbackground="#c4c4c4")
        self.Canvas1.configure(selectforeground="#000000")

        self.Label1 = tk.Label(self.Canvas1)
        self.Label1.place(relx=0.259, rely=0.036, height=47, width=324)
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(activeforeground="black")
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(highlightbackground="#d9d9d9")
        self.Label1.configure(highlightcolor="black")
        self.Label1.configure(text='''DATABASE ADMIN CONSOLE''')

        self.Label2 = tk.Label(self.Canvas1)
        self.Label2.place(relx=0.014, rely=0.145, height=77, width=674)
        self.Label2.configure(activeforeground="#000000")
        self.Label2.configure(background="#a5a5a5")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(highlightbackground="#000000")
        self.Label2.configure(highlightcolor="#000000")
        self.Label2.configure(text='''DATABASE COMMAND''')

        self.Label3 = tk.Label(self.Canvas1)
        self.Label3.place(relx=0.014, rely=0.362, height=47, width=403)
        self.Label3.configure(background="#d9d9d9")
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(foreground="#000000")
        self.Label3.configure(text='''INSERT''')

        self.Label4 = tk.Label(self.Canvas1)
        self.Label4.place(relx=0.014, rely=0.47, height=37, width=393)
        self.Label4.configure(background="#d9d9d9")
        self.Label4.configure(disabledforeground="#a3a3a3")
        self.Label4.configure(foreground="#000000")
        self.Label4.configure(text='''VIEW''')

        self.Label5 = tk.Label(self.Canvas1)
        self.Label5.place(relx=0.029, rely=0.579, height=37, width=375)
        self.Label5.configure(background="#d9d9d9")
        self.Label5.configure(disabledforeground="#a3a3a3")
        self.Label5.configure(foreground="#000000")
        self.Label5.configure(text='''EXIT''')

        self.Button1 = tk.Button(self.Canvas1)
        self.Button1.place(relx=0.607, rely=0.362, height=35, width=90)
        self.Button1.configure(activebackground="#ececec")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#d9d9d9")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''Show''')


        self.Button2 = tk.Button(self.Canvas1)
        self.Button2.place(relx=0.607, rely=0.47, height=35, width=90)
        self.Button2.configure(activebackground="#ececec")
        self.Button2.configure(activeforeground="#000000")
        self.Button2.configure(background="#d9d9d9")
        self.Button2.configure(disabledforeground="#a3a3a3")
        self.Button2.configure(foreground="#000000")
        self.Button2.configure(highlightbackground="#d9d9d9")
        self.Button2.configure(highlightcolor="black")
        self.Button2.configure(pady="0")
        self.Button2.configure(text='''Show''')

        self.Button3 = tk.Button(self.Canvas1)
        self.Button3.place(relx=0.605, rely=0.579, height=35, width=90)
        self.Button3.configure(activebackground="#ececec")
        self.Button3.configure(activeforeground="#000000")
        self.Button3.configure(background="#d9d9d9")
        self.Button3.configure(disabledforeground="#a3a3a3")
        self.Button3.configure(foreground="#000000")
        self.Button3.configure(highlightbackground="#d9d9d9")
        self.Button3.configure(highlightcolor="black")
        self.Button3.configure(pady="0")
        self.Button3.configure(text='''Exit''')

        self.menubar = tk.Menu(self.top,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
        self.top.configure(menu = self.menubar)

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

if __name__ == '__main__':
    toplevel1()





