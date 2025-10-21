# import necessary libraries
from tkinter import *

#create window
root = Tk()
root.title('Number Pad')
root.geometry('750x300')

#create a frame to organize elements better
frame = Frame(master=root, height=200, width=360, bg="#d0efff")

nums = [[9, 8, 7], [6, 5, 4], [3, 2, 1], ['#', 0, '*']]

for i in range(4):
    #configure rows and columns to resize window
    root.columnconfigure(i, weight=1, minsize=75)
    root.rowconfigure(i, weight=1, minsize=50)
    for j in range(0, 3):
        frame = Frame(
            master=root,
            relief=SUNKEN,
            borderwidth=1
        )
        frame.grid(row=i, column=j)
        label = Label(master=frame, text=nums[i][j], bg='#d0efff')
        label.pack(padx=3, pady=3)

#start the GUI event loop
root.mainloop()        