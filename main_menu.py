from tkinter import *
import os
import tkinter as tk 
from PIL import ImageTk,Image
from tkinter import messagebox
import sys


self = Tk()
self.title('Frienvi Main Menu')
self.geometry("500x500")
self.configure(bg='lightblue')


#app logo
load = Image.open('frienvilogo.png')
render = ImageTk.PhotoImage(load)
logo = Label(self, image=render)
logo.image = render

logo.grid(row=0,column=0)

#buttons
search = Entry(self,width=30,borderwidth=1)
search.insert(0, "Αναζήτηση")
search.grid(row=1,column=0)

news=Button(self, text="Ειδήσεις",height=3,width=30)
news.grid(row=2,column=0)

secondh=Button(self, text="Μεταχειρισμένα",font=('bold'),heigh=3,width=30)
secondh.grid(row=3,column=0)

estiash=Button(self, text="Χώροι εστίασης",font=('bold'),heigh=3,width=30)
estiash.grid(row=4,column=0)

food=Button(self, text="Καταστήματα τροφίμων",font=('bold'),heigh=3,width=30)
food.grid(row=5,column=0)

#list of buttons
obj_list=[logo,search,news,secondh,estiash,food]
#loop thru the list and config
row_num=0
for button in obj_list:
    Grid.rowconfigure(self,row_num,weight=1)
    row_num+=1

Grid.columnconfigure(self,0,weight=1)



self.mainloop()

