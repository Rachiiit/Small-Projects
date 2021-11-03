import tkinter
window=tkinter.Tk()
window.title("GUI")
label=tkinter.Label(window,text="Hello World!").pack()
window.mainloop()
'''
l1=label(window,text="edureka!",font=("Arial Bold",50))
l1.grid(column=0,row=0)
'''
import tkinter
from tkinter.ttk import *
combo=Combobox(window)
combo['values']=(1,2,3,4,5,"Text")
combo.current(3)
combo.grid(column=0,row=0)
'''
bt=Button(window,text="Enter")
bt.grid(column=1,row=0)
'''
