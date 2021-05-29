from tkinter import *
import os
from PIL import ImageTk,Image

global logo
store_login=Tk()
store_login.title('Frienvi Store login page')
store_login.geometry("500x500")
#app logo
logo= Canvas(store_login, width = 190, height = 91)
img = ImageTk.PhotoImage(Image.open('frienvilogo.png'))
logo.create_image(10,10,anchor=NW, image=img)
logo.theimage=img

#entry request screen
def entryRequest():
    global entryRequest_screen
    entryRequest_screen=Toplevel(store_login)
    entryRequest_screen.title("Frienvi Store Entry Request")
    entryRequest_screen.geometry("800x800")

    logo2=Canvas(entryRequest_screen, width = 190, height = 91)
    img2=ImageTk.PhotoImage(Image.open('frienvilogo.png'))
    logo2.create_image(10,10,anchor=NW, image=img)
    global name
    global storeinfo
    global ecoinfo
    global answer
    name=StringVar()
    storeinfo=StringVar()
    ecoinfo=StringVar()
    answer=StringVar()
    
    name=Entry(entryRequest_screen,textvariable=name)
    application=Label(entryRequest_screen, text="Αίτηση εισαγωγής",font=('ariel', 10))
    storename=Label(entryRequest_screen, text="Όνομα Καταστήματος",font=('ariel', 10))
    enterdetails=Label(entryRequest_screen, text="Πείτε μας λίγα λόγια για την επιχειρησή σας",font=('ariel', 10))
    storeinfo=Entry(entryRequest_screen,textvariable=storeinfo)
    ecodetails=Label(entryRequest_screen, text="Ενημερώστε μας για την επίπτωση που έχει το κατάστημά σας στο περιβάλλον",font=('ariel', 10))
    ecoinfo=Entry(entryRequest_screen,textvariable=ecoinfo)
    question=Label(entryRequest_screen, text="Γιατί πιστεύεται πρέπει να σας προσθέσουμε στην εφαρμογή;",font=('ariel', 10))
    answer=Entry(entryRequest_screen,textvariable=answer)
    confirm=Button(entryRequest_screen,text='Επιβεβαίωση',width=20, height=1,bg='black',fg='white')
    goback=Button(entryRequest_screen,text='Επιστροφή',width=20, height=1,bg='black',fg='white' )

    logo2.grid(row=0,column=0)
    application.grid(row=1,column=0)
    storename.grid(row=2,column=0)
    name.grid(row=2,column=1)
    enterdetails.grid(row=3,column=0)
    storeinfo.grid(row=3,column=1,ipadx=30,ipady=30)
    ecodetails.grid(row=4,column=0)
    ecoinfo.grid(row=4,column=1,ipadx=30,ipady=30)
    question.grid(row=5,column=0)
    answer.grid(row=5,column=1,ipadx=30,ipady=30)
    confirm.grid(row=6,column=1)
    goback.grid(row=6,column=2)

    #list of buttons
    obj_list=[logo2,application,storename,name,enterdetails,storeinfo,ecodetails,ecoinfo,question,answer,confirm,goback]
    #loop thru the list and config
    row_num=0
    for button in obj_list:
        Grid.rowconfigure(entryRequest_screen,row_num,weight=1)
        row_num+=1

    Grid.columnconfigure(entryRequest_screen,0,weight=1)



    
    




label_1=Label(store_login, text="Έχετε επιβεβαιώσει την εισαγωγή σας ως κατάστημα;",font=('ariel', 10))
button_1=Button(store_login, text='Αίτηση εισαγωγής',width=40, height=2,bg='black',fg='white', command=entryRequest)
button_2=Button(store_login, text='Δημιουργία Προφίλ Καταστήματος',width=40, height=2,bg='black',fg='white')

logo.grid(row=0,column=0)
label_1.grid(row=1,column=0)
button_1.grid(row=2,column=0)
button_2.grid(row=3,column=0)

#list of buttons
obj_list=[logo,label_1,button_1,button_2]
#loop thru the list and config
row_num=0
for button in obj_list:
    Grid.rowconfigure(store_login,row_num,weight=1)
    row_num+=1

Grid.columnconfigure(store_login,0,weight=1)

store_login.mainloop()
