import tkinter as tk
from tkinter import font as tkfont


class MenuBar(tk.Menu):
    def __init__(self, parent, controller):
        tk.Menu.__init__(self, controller)
        self.controller = controller

        fileMenu = tk.Menu(self, tearoff=0)
        self.add_cascade(label="File", underline=0, menu=fileMenu)
        fileMenu.add_command(label="New Test", underline=1,
                             command=lambda: SampleApp().show_frame("NewTestWindow"))
        fileMenu.add_separator()
        fileMenu.add_command(label="Exit", underline=2, command=self.onexit)

    def onexit(self):
        quit()


class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(
            family='Helvetica', size=18, weight="bold", slant="italic")

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (MainWindow, NewTestWindow):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("MainWindow")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()


class MainWindow(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.menubar = MenuBar(self, parent)
        self.controller.config(menu=self.menubar)

        label = tk.Label(self, text="This is the main page",
                         font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        button1 = tk.Button(self, text="Start new test",
                            command=lambda: controller.show_frame("NewTestWindow"))
        button1.pack()


class NewTestWindow(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        label = tk.Label(self, text="This is page 1",
                         font=controller.title_font)
        label.grid(row=1, column=0)
        button = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("MainWindow"))
        button.grid(row=2, column=0)


if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()
