import Tkinter
from time import strftime
rel = Tkinter.Label()
rel.pack()
rel['text'] = strftime('%H:%M:%S')
rel['font'] = 'Helvita 50 bold'
rel['foreground'] = 'lime'
rel['bg'] = 'black'


def contador():
        agora = strftime('%H:%M:%S')
        if rel['text'] != agora:
                rel['text'] = agora
        rel.after(100, contador)
contador()
rel.mainloop()
