from tkinter import *
from tkinter.ttk import *
import random
import pyperclip

screen = Tk()

screen.title("Password Generator")
screen.configure(background="#16697A")
screen.resizable(height=False, width=False)


style = Style()
var = IntVar()
var.set(1)

style.configure("Custom.TButton", background="#16697A", foreground="black")
style.configure("Custom.TRadiobutton", background="#16697A", foreground="white")

letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvqwxyz"
numbers = "0123456789"
symbols = "!@#$%^&*-=."
characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvqwxyz0123456789!@#$%^&*-=."


def copypass():
    pyperclip.copy(p.get())



def encrypt():
    shift = 3
    password = p.get()
    encr_password = ""

    for i in password:
        if i not in characters:
            encr_password += i
        else:
            position = characters.index(i)
            new_position = (position + shift) % len(characters)
            encr_password += characters[new_position]
            e.delete(0, END)
            e.insert(0, encr_password)


def decrypt():
    shift = -3
    password = e.get()
    encr_password = ""

    for i in password:
        if i not in characters:
            encr_password += i
        else:
            position = characters.index(i)
            new_position = (position + shift) % len(characters)
            encr_password += characters[new_position]
            d.delete(0, END)
            d.insert(0, encr_password)




def generate():
    length = int(combo.get())
    strength = var.get()
    password = ""

    if strength == 1:
        for i in range(length):
            a = random.choice(letters)
            password += a
    elif strength == 2:
        ln = letters + numbers
        for i in range(length):
            a = random.choice(ln)
            password += a
    elif strength == 3:
        lns = letters + numbers + symbols
        for i in range(length):
            a = random.choice(lns)
            password += a
    p.delete(0,END)
    p.insert(0, password)



combo = Combobox(screen)
combo['values'] = (8, 9, 10, 11, 12, 13, 14, 15, 16, 20, 32)
combo.current(0)
combo.grid(column=1, row=1)

lo = Radiobutton(screen, text = "Low",style="Custom.TRadiobutton", variable=var, value=1)
me = Radiobutton(screen, text = "Medium",style="Custom.TRadiobutton", variable=var, value=2)
st = Radiobutton(screen, text = "Strong", style="Custom.TRadiobutton",variable=var, value=3)
lo.grid(row=1, column=2)
me.grid(row=1, column=3)
st.grid(row=1, column=4)

pw = Label(screen, text = "Password",background="#16697A", foreground="white")
pw.grid(row= 0, column=0)
p = Entry(screen)
p.grid(row=0, column=1)
cp = Button(screen, text = "Copy", style="Custom.TButton", command=copypass)
cp.grid(row=0, column=2)
gp = Button(screen, text = "Generate", style="Custom.TButton", command=generate)
gp.grid(row=0, column=3)
lth = Label(screen, text = "Length", background="#16697A", foreground="white")
lth.grid(row= 1, column=0)
ec = Label(screen, text = "Encrypted Password", background="#16697A", foreground="white")
ec.grid(row= 2, column=0)
e = Entry(screen)
e.grid(row=2, column=1)
en = Button(screen, text = "Encrypt", style="Custom.TButton", command = encrypt)
en.grid(row=2, column=2)
dn = Label(screen, text = "Decrypted Password", background="#16697A", foreground="white")
dn.grid(row= 3, column=0)
d = Entry(screen)
d.grid(row=3, column=1)
en = Button(screen, text = "Decrypt", style="Custom.TButton", command = decrypt)
en.grid(row=3, column=2)



screen.mainloop()