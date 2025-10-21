#import necessasry libraries
from tkinter import *

#create window
root = Tk()
root.title('login app')
root.geometry('400x400')

#create a frame to organize elements better
frame = Frame(master=root, height=200, width=360, bg="#d0efff")

#add widgets
#add label
lbl1 = Label(frame, text = "full Name", bg="#3895D3", fg='white', width=12)
lbl2 = Label(frame, text = "Email Id", bg="#3895D3", fg='white', width=12)
lbl3 = Label(frame, text = "Enter Password", bg="#3895D3", fg='white', width=12)

#use entry widgets to create a text box for user to enter details
name_entry = Entry(frame)
email_entry = Entry(frame)
pass_entry = Entry(frame, show="*")

#function to display message
def display():
    name = name_entry.get()
    greet = "hey "+name
    message = "\nCongratulations for your new account!"
    textbox.insert(END, greet)
    textbox.insert(END, message)

#textbox to display message
textbox = Text(bg="#BEBEBE", fg="black")

#add button, when pressed, message will be displayed
btn = Button(text = "create account", command=display, bg="red")

#arrange all widgets
frame.place(x=20,y=0)
lbl1.place(x=20, y=20)
name_entry.place(x=150, y=20)
lbl2.place(x=20, y=80)
email_entry.place(x=150, y=80)
lbl3.place(x=20, y=140)
pass_entry.place(x=150, y=140)
btn.place(x=130, y=210)
textbox.place(y=250)

#start the GUI event loop
root.mainloop()