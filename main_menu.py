from tkinter import *
import os
from PIL import ImageTk,Image

window = Tk()
window.title('Frienvi Main Menu')
window.geometry("700x700")
window.configure(bg='lightblue')


#for logo
logo = Canvas(window, width = 285, height = 126)
img = PhotoImage(file = 'C:\\Users\\mario\\Desktop\\Μαθήματα\\8ο εξάμηνο\\Τεχνολογία Λογισμικού\\εικόνες\\logo.png')
logo.create_image(10,10,anchor=NW, image=img)
logo.grid(row=0,column=0)

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



#buttons
search = Entry(window,width=30,borderwidth=1)
search.insert(0, "Αναζήτηση")
search.grid(row=1,column=0)

news=Button(window, text="Ειδήσεις",height=3,width=30)
news.grid(row=2,column=0)

secondh=Button(window, text="Μεταχειρισμένα",font=('bold'),heigh=3,width=30)
secondh.grid(row=3,column=0)

estiash=Button(window, text="Χώροι εστίασης",font=('bold'),heigh=3,width=30)
estiash.grid(row=4,column=0)

food=Button(window, text="Καταστήματα τροφίμων",font=('bold'),heigh=3,width=30)
food.grid(row=5,column=0)

#list of buttons
obj_list=[logo,search,news,secondh,estiash,food]
#loop thru the list and config
row_num=0
for button in obj_list:
    Grid.rowconfigure(window,row_num,weight=1)
    row_num+=1

Grid.columnconfigure(window,0,weight=1)



window.mainloop()
