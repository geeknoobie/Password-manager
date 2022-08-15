from tkinter import *
import random
from password import *
from csv import *
from tkinter import messagebox
import pyperclip
import pandas

s4 = 0


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def passwrd():
    global s4
    a = []
    b = []
    c = []
    s4 = 0
    for i in range(0, 8):
        a1 = random.choice(letters)
        a.append(a1)
    for j in range(0, 5):
        b1 = random.choice(symbols)
        b.append(b1)
    for k in range(0, 5):
        c1 = random.choice(numbers)
        c.append(c1)
    s1 = ''.join(map(str, b))
    s2 = ''.join(map(str, a))
    s3 = ''.join(map(str, c))
    s4 = ''.join(random.sample((s1 + s2 + s3), len(s1 + s2 + s3)))
    textEntry.set(value=s4)
    pyperclip.copy(s4)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def add():
    lst = [site_inp.get(), name_inp.get(), pass_inp.get()]
    ok = messagebox.askokcancel(title="your credentials",
                                message=f"these are your credentials\n website:{site_inp.get()}\n "
                                        f"username:{name_inp.get()}\npassword:{pass_inp.get()}\n "
                                        f"would you like to save")
    if ok:
        with open('data_file.csv', 'a') as data_file:
            writer_object = writer(data_file)
            writer_object.writerow(lst)
            data_file.close()
        pass_inp.delete(0, "end")
        name_inp.delete(0, "end")
        site_inp.delete(0, "end")


# ---------------------------- PASSWORD SEARCH ------------------------------- #
def search():
    data = pandas.read_csv("data_file.csv")
    p = site_inp.get()
    ps = data[data.website == p].values.tolist()
    for i in ps:
        pass_key = i
    messagebox.showinfo(title="your credentials",message=f"Website:{pass_key[0]}\nUsername:{pass_key[1]}\n"
                                                        f"Password:{pass_key[2]}")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.minsize(width=1000, height=700)
window.config(padx=100, pady=100)
# ---------------------------- IMAGE SETUP ------------------------------- #
canvas = Canvas(width=200, height=189, highlightthickness=0)
img = PhotoImage(file="logo.png")
canvas.create_image(100, 94, image=img)
canvas.grid(row=0, column=1)
# ---------------------------- LEFT TEXT ------------------------------- #
website = Label(text="WEBSITE:", font=("Courier", 20))
website.grid(row=1, column=0)
username = Label(text="EMAIL/USERNAME:", font=("Courier", 20))
username.grid(row=2, column=0)
password = Label(text="Password:", font=("Courier", 20))
password.grid(row=3, column=0)
# ---------------------------- INPUT SETUP ------------------------------- #
site_inp = Entry(highlightthickness=2, width=25)
site_inp.grid(row=1, column=1, )
name_inp = Entry(highlightthickness=2, width=50)
name_inp.grid(row=2, column=1, columnspan=2)
textEntry = StringVar()
pass_inp = Entry(highlightthickness=2, width=25, textvariable=textEntry)
pass_inp.grid(row=3, column=1)
# ---------------------------- BUTTON SETUP ------------------------------- #
generate = Button(text="Generate", width=25, fg="black", command=passwrd)
generate.grid(row=3, column=2)
add = Button(text="Add", width=50, fg="black", command=add)
add.grid(row=4, column=1, columnspan=2)
srch = Button(text="Search", width=25, fg="black", command=search)
srch.grid(row=1, column=2)
window.mainloop()
