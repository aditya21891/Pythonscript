# This is a python script for Event handler

import Tkinter as tk

def doorbell(event):
    print("You rang the doorbell")

window=tk.Tk()
window.geometry("300*200")

alabel=tk.Label(text="banana")
alabel.grid(column=0,row=0)

blabel=tk.Label(text="Apple")
blabel.grid(column=1,row=0)

button=tk.Button(window,text="Doorbell")
button.grid(column=0)

button2=tk.Button(window,text="10")
button2.grid(column=1,row=1)

button.bind("<Button-1>",doorbell)

window.mainloop()


