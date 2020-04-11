from tkinter import *


root = Tk()
root.geometry("1200x700+110+55")


def Encoder():
    #D: \gUI\LSB_Module\encoder.py
    window = Tk.Toplevel(root)
    frame = Frame(root, Label="Encoder")
    var = StringVar()
    msg = Message(frame, text="Encoder")
    frame.pack()
    msg.pack()


def Decoder():
    #D: \gUI\LSB_Module\decoder.py
    frame = Frame(root, Label="Decoder")

main_menu = Menu(root)


fileMenu = Menu(main_menu,tearoff=0)
main_menu.add_cascade(label ="Operation" ,menu=fileMenu)
#UserMenu = Menu(main_menu)
# main_menu.add_cascade(Label="....", menu=UserMenu) # add user name after complete login and database
fileMenu.add_command(label="Encoder",command=Encoder)
fileMenu.add_command(label="Decoder", command=Decoder)
main_menu.add_command(label="Quit!", command=root.quit)

root.config(menu=main_menu)

root.mainloop()
