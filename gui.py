import Tkinter

top = Tkinter.Tk()
top.geometry("400x200")
# Code to add widgets will go here...

abutton = Tkinter.Button(top, text ="Encriptar")

abutton.pack()
abutton.place(x=200, y=30)

plainInputtext = Tkinter.Entry(top)
plainInputtext.place(x=20,y=30)

keyInputext = Tkinter.Entry(top)
keyInputext.place(x=20,y=80)


top.mainloop()
