from tkinter import *
from PIL import ImageTk,Image
from json import load

Constants = load(open('utils/constants.json'))


def startMenu_open(self):
    window = Toplevel()
    window.geometry('600x400+600+300')
    window['bg'] = ('white')
    window.iconbitmap(Constants['AIM_ICON'])
    window.title('Aims - Aprenda inglês de modo simples')

class App:



    def __init__(self, parent):
        
        self.parent = parent

        self.load_hud()
        self.load_images()

        self.parent.brFlagLabel = Label(image=self.parent.BR_FLAG)
        self.parent.brFlagLabel.place(relx=0.5, rely=0.4, anchor=CENTER)

        self.parent.usFlagLabel = Label(image=self.parent.US_FLAG)
        self.parent.usFlagLabel.place(relx=0.5, rely=0.595, anchor=CENTER)

        self.parent.greatDayLabel = Label(text='Tenha um ótimo dia!!', bg='white', width=20)
        self.parent.greatDayLabel.pack(side=TOP)

        self.parent.greatDayLabel =  Button(text='Aprender', width=20, bg='white', command=startMenu_open)
        self.parent.greatDayLabel.place(relx=0.5, rely=0.5, anchor=CENTER)
        self.parent.greatDayLabel.bind('<Button-1>', startMenu_open)

        self.parent.quitButton  = Button(text='Fechar', bg='white')
        self.parent.quitButton.place(relx=0.0, rely=0.95)
        self.parent.quitButton.bind('<Button-1>', quit)

    def load_hud (self):
        self.parent.geometry('500x500+600+300')
        self.parent['bg'] ='white'
        self.parent.title('Aims- Aprenda inglês de modo simples')
        self.parent.iconbitmap(Constants['AIM_ICON'])

    def load_images (self):
        self.parent.BR_FLAG = ImageTk.PhotoImage(Image.open(Constants['BR_FLAG']))
        self.parent.US_FLAG = ImageTk.PhotoImage(Image.open(Constants['US_FLAG_FIXED']))




root = Tk()
App(root)
root.mainloop()