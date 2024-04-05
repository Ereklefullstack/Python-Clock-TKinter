from tkinter import *
from tkinter.ttk import *
from time import strftime
root = Tk()
root.title('Clock')
def clock():
    tick = strftime('%H:%M:%S %p')
    Label.config(text = tick)
    Label.after(1000, clock)
Label = Label(root, font = ('ds-digital', 100),
background = 'aqua', foreground = 'black')
Label.pack(anchor = 'center')
clock()
mainloop()