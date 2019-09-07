from tkinter import *
from PIL import ImageTk,Image
from json import load

Constants = load(open('utils/constants.json'))


def startMenu_open():
    window = Toplevel()
    window.geometry('600x400+600+300')
    window['bg'] = ('white')
    window.iconbitmap(Constants['AIM_ICON'])
    window.title('Aims - Aprenda inglês de modo simples')

class App:



    def __init__(self, parent):
        
        self.parent = parent
        self.parent.geometry('500x500+600+300')
        self.parent['bg'] ='white'
        self.parent.title('Aims- Aprenda inglês de modo simples')
        self.parent.iconbitmap(Constants['AIM_ICON'])

        self.parent.brazilFlagImg = brazilFlagImg = ImageTk.PhotoImage(Image.open(Constants['BR_FLAG']))
        self.parent.brFlagLabel = brFlagLabel = Label(image=brazilFlagImg)
        self.parent.brFlagLabel = brFlagLabel.place(relx=0.5, rely=0.4, anchor=CENTER)

        self.parent.usFlagImg = usFlagImg = ImageTk.PhotoImage(Image.open(Constants['US_FLAG_FIXED']))
        self.parent.usFlagLabel = usFlagLabel = Label(image=usFlagImg)
        self.parent.usFlagLabel = usFlagLabel.place(relx=0.5, rely=0.595, anchor=CENTER)

        self.parent.greatDayLabel = greatDayLabel = Label(text='Tenha um ótimo dia!!', bg='white', width=20)
        self.parent.greatDayLabel = greatDayLabel.pack(side=TOP)

        self.parent.greatDayLabel = startButton = Button(text='Aprender', width=20, bg='white', command=startMenu_open)
        self.parent.greatDayLabel = startButton.place(relx=0.5, rely=0.5, anchor=CENTER)
        self.parent.greatDayLabel = startButton.bind('<Button-1>', startMenu_open)

        self.parent.quitButton = quitButton = Button(text='Fechar', bg='white')
        self.parent.quitButton.place = quitButton.place(relx=0.0, rely=0.95)
        self.parent.quitButton.bind = quitButton.bind('<Button-1>', quit)




root = Tk()
App(root)
root.mainloop()