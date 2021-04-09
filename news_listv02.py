from tkinter import *
from PIL import ImageTk,Image
from tkinter import ttk
import tkinter as tk
import os


window = Tk()
window.title('Frienvi News')
window.geometry("500x500")
window.configure(bg='lightblue')


#for logo
logo = Canvas(window, width = 250, height = 250)
img = ImageTk.PhotoImage(Image.open("frienvilogo.png"))
logo.create_image(10,10,anchor=NW, image=img)
logo.pack()

#menubar
menu=Menu(window)
window.config(menu=menu)


subm1=Menu(menu)
menu.add_cascade(label="Ρυθμίσεις",menu=subm1)
subm1.add_command(label="Πληροφορίες")

subm2=Menu(menu)
menu.add_cascade(label="Λογαριασμός",menu=subm2)
subm2.add_command(label="Αποσύνδεση")

subm3=Menu(menu)
menu.add_cascade(label="Αγαπημένα",menu=subm3)

subm4=Menu(menu)
menu.add_cascade(label="Αξιολόγη",menu=subm4)
subm4.add_command(label="Υποβολή σχολίου")
subm4.add_command(label="Πρόταση καταστήματος")

helpmenu = Menu(menu)
menu.add_cascade(label="Βοήθεια", menu=helpmenu)
helpmenu.add_command(label="Σχετικά...",)

#Label
newslabel = Label(window,text='Ειδήσεις',font=('calibri', 20,))
newslabel.pack(pady=15)


#Listbox
my_listbox = Listbox(window,width=50,height=30)
my_listbox.pack()




Grid.rowconfigure(window,0,weight=1)
Grid.columnconfigure(window,0,weight=1)


window.mainloop()
