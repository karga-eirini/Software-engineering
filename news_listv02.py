from tkinter import *
import os
from tkinter import messagebox

window = Tk()
window.title('Frienvi News')
window.geometry("500x700")
window.configure(bg='lightblue')


#for logo
logo = Canvas(window, width = 285, height = 126)
img = PhotoImage(file = 'C:\\Users\\mario\\Desktop\\Μαθήματα\\8ο εξάμηνο\\Τεχνολογία Λογισμικού\\εικόνες\\logo.png')
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