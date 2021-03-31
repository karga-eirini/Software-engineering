from tkinter import *
import os


window = Tk()
window.title('Frienvi Main Menu')
window.geometry("700x700")
logo= Canvas(window, width = 285, height = 126)
window.configure(bg='lightblue')
Grid.columnconfigure(window,0,weight=1)
Grid.rowconfigure(window,0,weight=1)
Grid.rowconfigure(window,1,weight=1)
Grid.rowconfigure(window,2,weight=1)
Grid.rowconfigure(window,3,weight=1)
Grid.rowconfigure(window,4,weight=1)
Grid.rowconfigure(window,5,weight=1)
Grid.rowconfigure(window,5,weight=1)
Grid.rowconfigure(window,6,weight=1)
Grid.rowconfigure(window,7,weight=1)


#for logo
img = PhotoImage(file = 'C:\\Users\\mario\\Desktop\\Μαθήματα\\8ο εξάμηνο\\Τεχνολογία Λογισμικού\\εικόνες\\logo.png')
logo.create_image(10,10,anchor=NW, image=img)

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




search = Entry(window,width=30,borderwidth=1)
search.insert(0, "Αναζήτηση")

news=Button(window, text="Ειδήσεις",height=3,width=30)
news.grid(row=3,column=0)

clothes=Button(window, text="Μεταχειρισμένα",font=('bold'),heigh=3,width=30)
clothes.grid(row=4,column=0)

obj=Button(window, text="Χώροι εστίασης",font=('bold'),heigh=3,width=30)
obj.grid(row=5,column=0)

estiash=Button(window, text="Καταστήματα τροφίμων",font=('bold'),heigh=3,width=30)
estiash.grid(row=6,column=0)




#placement
logo.grid(row=0 ,column=0)
search.grid(row=2,column=0)






window.mainloop()