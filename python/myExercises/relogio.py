#!/usr/bin/env python3
import Tkinter
from time import strftime
 
def tic():
    rel['text'] = strftime('%H:%M:%S')
 
def tac():
    tic()
    rel.after(1000, tac)
 
rel = Tkinter.Label()
rel['font'] = 'Helvetica 120 bold'
rel.pack()
tac()
rel.mainloop()