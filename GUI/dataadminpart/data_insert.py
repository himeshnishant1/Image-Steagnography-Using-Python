import sys
import tkinter as tk
import tkinter.ttk as ttk
import data_insert_support

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

        self.top.geometry("600x450+650+150")
        self.top.minsize(152, 1)
        self.top.maxsize(1924, 1055)
        self.top.resizable(1, 1)
        self.top.title("New self.toplevel")
        self.top.configure(background="#d9d9d9")

        self.Label1 = tk.Label(self.top)
        self.Label1.place(relx=0.083, rely=0.089, height=57, width=493)
        self.Label1.configure(background="#c0c0c0")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(text='''INSERT DATA''')

        self.Label2 = tk.Label(self.top)
        self.Label2.place(relx=0.1, rely=0.311, height=37, width=143)
        self.Label2.configure(background="#d9d9d9")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(text='''USER NAME''')

        self.Label2_2 = tk.Label(self.top)
        self.Label2_2.place(relx=0.1, rely=0.444, height=37, width=143)
        self.Label2_2.configure(activebackground="#f9f9f9")
        self.Label2_2.configure(activeforeground="black")
        self.Label2_2.configure(background="#d9d9d9")
        self.Label2_2.configure(disabledforeground="#a3a3a3")
        self.Label2_2.configure(foreground="#000000")
        self.Label2_2.configure(highlightbackground="#d9d9d9")
        self.Label2_2.configure(highlightcolor="black")
        self.Label2_2.configure(text='''EMAIL''')

        self.Label2_3 = tk.Label(self.top)
        self.Label2_3.place(relx=0.1, rely=0.578, height=37, width=143)
        self.Label2_3.configure(activebackground="#f9f9f9")
        self.Label2_3.configure(activeforeground="black")
        self.Label2_3.configure(background="#d9d9d9")
        self.Label2_3.configure(disabledforeground="#a3a3a3")
        self.Label2_3.configure(foreground="#000000")
        self.Label2_3.configure(highlightbackground="#d9d9d9")
        self.Label2_3.configure(highlightcolor="black")
        self.Label2_3.configure(text='''PASSWORD''')

        self.Entry1 = tk.Entry(self.top)
        self.Entry1.place(relx=0.417, rely=0.311,height=34, relwidth=0.473)
        self.Entry1.configure(background="white")
        self.Entry1.configure(disabledforeground="#a3a3a3")
        self.Entry1.configure(font="TkFixedFont")
        self.Entry1.configure(foreground="#000000")
        self.Entry1.configure(insertbackground="black")

        self.Entry1_4 = tk.Entry(self.top)
        self.Entry1_4.place(relx=0.417, rely=0.578,height=34, relwidth=0.473)
        self.Entry1_4.configure(background="white")
        self.Entry1_4.configure(disabledforeground="#a3a3a3")
        self.Entry1_4.configure(font="TkFixedFont")
        self.Entry1_4.configure(foreground="#000000")
        self.Entry1_4.configure(highlightbackground="#d9d9d9")
        self.Entry1_4.configure(highlightcolor="black")
        self.Entry1_4.configure(insertbackground="black")
        self.Entry1_4.configure(selectbackground="#c4c4c4")
        self.Entry1_4.configure(selectforeground="black")

        self.Entry1_5 = tk.Entry(self.top)
        self.Entry1_5.place(relx=0.417, rely=0.444,height=34, relwidth=0.473)
        self.Entry1_5.configure(background="white")
        self.Entry1_5.configure(disabledforeground="#a3a3a3")
        self.Entry1_5.configure(font="TkFixedFont")
        self.Entry1_5.configure(foreground="#000000")
        self.Entry1_5.configure(highlightbackground="#d9d9d9")
        self.Entry1_5.configure(highlightcolor="black")
        self.Entry1_5.configure(insertbackground="black")
        self.Entry1_5.configure(selectbackground="#c4c4c4")
        self.Entry1_5.configure(selectforeground="black")

        self.Button1 = tk.Button(self.top)
        self.Button1.place(relx=0.35, rely=0.778, height=45, width=150)
        self.Button1.configure(activebackground="#ececec")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#d9d9d9")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''INSERT''')

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





