from Tkinter import *
import DesStart

top = Tk()
top.geometry("400x200")
top.title("DES Algorithm")
# Code to add widgets will go here...

def encrypt():
    result = DesStart.encrypt_decrypt(keyInputext.get(), plainInputtext.get(), False)
    T.delete('1.0', END)
    T.insert(END,result)


def descrypt():
    result = DesStart.encrypt_decrypt(keyInputext.get(), plainInputtext.get(), True)
    T.delete('1.0', END)
    T.insert(END, result)


abutton = Button(top, text ="Encriptar", command = encrypt)
abutton.pack()
abutton.place(x=250, y=30)

abutton = Button(top, text ="Desencriptar",command = descrypt)
abutton.pack()
abutton.place(x=250, y=60)

keyLabel = Label(top,text= "Key")
keyLabel.place(x=20, y=15)

keyInputext = Entry(top)
keyInputext.insert(END,"133457799BBCDFF1")
keyInputext.place(x=20,y=30)

plainLabel = Label(top,text="Plaintext")
plainLabel.place(x=20, y=60)

plainInputtext = Entry(top)
plainInputtext.insert(END,"0123456789ABCDEF")
plainInputtext.place(x=20,y=80)


T = Text(top, height=2, width=40)
T.pack()
T.insert(END,"Resultado")
T.place(x=50,y=130)



top.mainloop()
