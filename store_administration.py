from tkinter import *
import os
from PIL import ImageTk,Image


store_adm = Tk()
store_adm.title('Frienvi Store administration')
store_adm.geometry("500x500")
#app logo
logo= Canvas(store_adm, width = 190, height = 91)
img = ImageTk.PhotoImage(Image.open('frienvilogo.png'))
logo.create_image(10,10,anchor=NW, image=img)
logo.theimage = img

#second hand stores administration
def secondhand():
    global sh_screen
    #adding the new window to the top level window
    sh_screen = Toplevel(store_adm)
    sh_screen.title("Frienvi Καταστήματα με μεταχειρισμένα")
    sh_screen.geometry("500x500")
    #showing logo to the new window
    logo2 = Canvas(sh_screen, width = 190, height = 91)
    img2 = ImageTk.PhotoImage(Image.open('frienvilogo.png'))
    logo2.create_image(10,10,anchor=NW, image=img)
    #defining all the global attributes
    global name
    global location
    global schedule
    global number
    global time
    global newproduct
    #setting them as stringvar 
    name= StringVar()
    location= StringVar()
    schedule= StringVar()
    number= StringVar()
    time= StringVar()
    newproduct= StringVar()

    #creating a list for the products of the store
    listbox = Listbox(sh_screen, height = 10, width = 15, bg = "white",activestyle = 'dotbox', font = "Helvetica",fg = "grey")
    listbox.insert(1, "Φόρεμα")
    listbox.insert(2, "Φούστα")
    listbox.insert(3, "Γάντια")
    listbox.insert(4, "Καπέλο")
    listbox.insert(5, "Ζακέτα")
   

    label1=Label(sh_screen,text="Όνομα καταστήματος:")
    name=Entry(sh_screen, textvariable=name )
    menu=Label(sh_screen, text="Βασικό μενού: προϊόντα")
    label2=Label(sh_screen, text="Διεύθυνση καταστήματος:")
    location=Entry(sh_screen, textvariable=location)
    label3=Label(sh_screen, text="Ωράριο λειτουργίας:")
    schedule=Entry(sh_screen, textvariable=schedule)
    label4=Label(sh_screen, text="Τηλέφωνο:")
    number=Entry(sh_screen, textvariable=number)
    label5=Label(sh_screen, text="Χρόνος αναμονής:")
    time=Entry(sh_screen, textvariable=time)
    label6=Label(sh_screen,text="Προσθήκη νέου προϊόντος")
    #adding funcion to be able to add products to list with the entry box
    newproduct=Entry(sh_screen, textvariable=newproduct)
    def additem():
        #starting index sets 6 because there are already 5 products in the list
        index=6
        listbox.insert(index,newproduct.get())
        index= index + 1
    submit=Button(sh_screen,text='Προσθήκη', height='1', width='10', bg='white', fg='grey',command=additem)

    #the screen will show
    logo2.grid(row=0,column=0)
    label1.grid(row=1,column=0)
    name.grid(row=1,column=1)
    menu.grid(row=2,column=0)
    listbox.grid(row=3)
    label2.grid(row=4,column=0)
    location.grid(row=4,column=1)
    label3.grid(row=5,column=0)
    schedule.grid(row=5,column=1)
    label4.grid(row=6,column=0)
    number.grid(row=6,column=1)
    label5.grid(row=7,column=0)
    time.grid(row=7,column=1)
    label6.grid(row=8,column=0)
    newproduct.grid(row=9,column=0)
    submit.grid(row=10,column=0)
    

    
    obj_list=[logo,label1,name,menu,label2,location,label3,schedule,label4,number,label5,time,label6,newproduct,submit]
    #loop thru the list and config
    row_num=0
    for button in obj_list:
        Grid.rowconfigure(sh_screen,row_num,weight=1)
        row_num+=1

    Grid.columnconfigure(sh_screen,0,weight=1)
    
    
#creating the same functions for the two other categories
def restaurant():
    global res_screen
    res_screen = Toplevel(store_adm)
    res_screen.title("Frienvi Χώροι εστίασης")
    res_screen.geometry("500x500")
    #showing logo to the new window
    logo2 = Canvas(res_screen, width = 190, height = 91)
    img2 = ImageTk.PhotoImage(Image.open('frienvilogo.png'))
    logo2.create_image(10,10,anchor=NW, image=img)
    global name
    global location
    global schedule
    global nymber
    global time
    global newproduct
    name= StringVar()
    location= StringVar()
    schedule= StringVar()
    number= StringVar()
    time= StringVar()
    newproduct= StringVar()


    listbox = Listbox(res_screen, height = 10, width = 15, bg = "white",activestyle = 'dotbox', font = "Helvetica",fg = "grey")
    listbox.insert(1, "Σαλάτα")
    listbox.insert(2, "Τοτίγια")
    listbox.insert(3, "Σάντουιτς")
    listbox.insert(4, "Πίτσα")
    listbox.insert(5, "Γλυκό")
    
    
    label1=Label(res_screen,text="Όνομα καταστήματος:")
    name=Entry(res_screen, textvariable=name )
    menu=Label(res_screen, text="Βασικό μενού: Προϊόντα")
    label2=Label(res_screen, text="Διεύθυνση καταστήματος:")
    location=Entry(res_screen, textvariable=location)
    label3=Label(res_screen, text="Ωράριο λειτουργίας:")
    schedule=Entry(res_screen, textvariable=schedule)
    label4=Label(res_screen, text="Τηλέφωνο:")
    number=Entry(res_screen, textvariable=number)
    label5=Label(res_screen, text="Χρόνος αναμονής:")
    time=Entry(res_screen, textvariable=time)
    label6=Label(res_screen,text="Προσθήκη νέου προϊόντος")
    newproduct=Entry(res_screen, textvariable=newproduct)
    def additem():
        index=6
        listbox.insert(index,newproduct.get())
        index= index + 1
    submit=Button(res_screen,text='Προσθήκη', height='1', width='10', bg='white', fg='grey',command=additem)
    

    logo2.grid(row=0,column=0)
    label1.grid(row=1,column=0)
    name.grid(row=1,column=1)
    menu.grid(row=2,column=0)
    listbox.grid(row=3)
    label2.grid(row=4,column=0)
    location.grid(row=4,column=1)
    label3.grid(row=5,column=0)
    schedule.grid(row=5,column=1)
    label4.grid(row=6,column=0)
    number.grid(row=6,column=1)
    label5.grid(row=7,column=0)
    time.grid(row=7,column=1)
    label6.grid(row=8,column=0)
    newproduct.grid(row=9,column=0)
    submit.grid(row=10,column=0)

    
    obj_list=[logo,label1,name,menu,listbox,label2,location,label3,schedule,label4,number,label5,time,label6,newproduct,submit]
    #loop thru the list and config
    row_num=0
    for button in obj_list:
        Grid.rowconfigure(res_screen,row_num,weight=1)
        row_num+=1

    Grid.columnconfigure(res_screen,0,weight=1)


#creating the same functions for the two other categories
def grocery():
    global gro_screen
    gro_screen = Toplevel(store_adm)
    gro_screen.title("Frienvi Καταστήματα τροφίμων")
    gro_screen.geometry("500x500")
    #showing logo to the new window
    logo2 = Canvas(register_screen, width = 190, height = 91)
    img2 = ImageTk.PhotoImage(Image.open('frienvilogo.png'))
    logo2.create_image(10,10,anchor=NW, image=img)
    global name
    global location
    global schedule
    global nymber
    global time
    global newproduct
    name= StringVar()
    location= StringVar()
    schedule= StringVar()
    number= StringVar()
    time= StringVar()
    newproduct= StringVar()

  

    listbox = Listbox(gro_screen, height = 10, width = 15, bg = "white",activestyle = 'dotbox', font = "Helvetica",fg = "grey")
    listbox.insert(1, "Μέλι")
    listbox.insert(2, "Καφέ")
    listbox.insert(3, "Ταχίνι")
    listbox.insert(4, "Φυστικοβούτυρο")
    listbox.insert(5, "Μπλούμπερις")

    label1=Label(gro_screen,text="Όνομα καταστήματος:")
    name=Entry(gro_screen, textvariable=name )
    menu=Label(gro_screen, text="Βασικό μενού: προϊόντα")
    label2=Label(gro_screen, text="Διεύθυνση καταστήματος:")
    location=Entry(gro_screen, textvariable=location)
    label3=Label(gro_screen, text="Ωράριο λειτουργίας:")
    schedule=Entry(gro_screen, textvariable=schedule)
    label4=Label(gro_screen, text="Τηλέφωνο:")
    number=Entry(gro_screen, textvariable=number)
    label5=Label(gro_screen, text="Χρόνος αναμονής:")
    time=Entry(gro_screen, textvariable=time)
    label6=Label(gro_screen,text="Προσθήκη νέου προϊόντος")
    newproduct=Entry(gro_screen, textvariable=newproduct)
    def additem():
        index=6
        listbox.insert(index,newproduct.get())
        index= index + 1
    submit=Button(gro_screen,text='Προσθήκη', height='1', width='10', bg='white', fg='grey',command=additem)

    logo2.grid(row=0,column=0)
    label1.grid(row=1,column=0)
    name.grid(row=1,column=1)
    menu.grid(row=2,column=0)
    listbox.grid(row=3)
    label2.grid(row=4,column=0)
    location.grid(row=4,column=1)
    label3.grid(row=5,column=0)
    schedule.grid(row=5,column=1)
    label4.grid(row=6,column=0)
    number.grid(row=6,column=1)
    label5.grid(row=7,column=0)
    time.grid(row=7,column=1)
    label6.grid(row=8,column=0)
    newproduct.grid(row=9,column=0)
    submit.grid(row=10,column=0)

    
    obj_list=[logo,label1,name,menu,label2,location,label3,schedule,label4,number,label5,time]
    #loop thru the list and config
    row_num=0
    for button in obj_list:
        Grid.rowconfigure(gro_screen,row_num,weight=1)
        row_num+=1

    Grid.columnconfigure(gro_screen,0,weight=1)




label1=Label(text='Επίλεξε κατηγορία καταστήματος:',font=('calibri', 10))
#each button connects to each function(one for every category)
btn1=Button(text='Μεταχειρισμένα', height='2', width='20', bg='green', fg='white',command=secondhand)
btn2=Button(text='Χώροι εστίασης', height='2', width='20', bg='red', fg='white',command=restaurant)
btn3=Button(text='Καταστήματα τροφίμων', height='2', width='20', bg='black', fg='white',command=grocery)

#the top level screen will show
logo.grid(row=0,column=0)
label1.grid(row=1,column=0)
btn1.grid(row=2,column=0)
btn2.grid(row=3,column=0)
btn3.grid(row=4,column=0)

#list of buttons
obj_list=[logo,label1,btn1,btn2,btn3]
#loop thru the list and config
row_num=0
for button in obj_list:
    Grid.rowconfigure(store_adm,row_num,weight=1)
    row_num+=1

Grid.columnconfigure(store_adm,0,weight=1)

store_adm.mainloop()
