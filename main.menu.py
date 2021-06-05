from tkinter import *
from PIL import ImageTk,Image
from tkinter import ttk
import tkinter as tk
import os
import sqlite3
from database_store import *  

window = Tk()
window.title('Frienvi Main Menu')
window.geometry("500x500")
window.configure(bg='lightblue')


 #for logo
logo = Canvas(window, width = 210, height = 210)
img = ImageTk.PhotoImage(Image.open("frienvilogo.png"))
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

def open() :
            # Create new page if open Metaxeirismena 
        top= Toplevel()
        top.geometry("500x500")
        top.title("Aναζήτησες με κριτήριο : Μεταχειρισμένα ")
        top.configure(bg='lightblue')
        # when clickarw metaxeirismena,new page me auto
        query_label= Label(top,text="Eμφάνισε τα μεταχειρισμένα!")
        query_label.grid(row=1,column=0)

    

            
        def metaxeirismena():
                    conn = sqlite3.connect("test.db") 
                    cursor = conn.cursor() 

                    cursor.execute(" SELECT name FROM Store WHERE category='Metaxeirismena' limit 30 ")
                    records=cursor.fetchall()
                    print(records)
                    print_records=''
                    for record in records[0]:
                        print_records += str(record)+ "\n"


                    query_label= Label(top, text=print_records).grid(row=3,column=0,columnspan=2)

                    conn.commit()
                    cursor.close()


        button_query= Button(top, text="CLICK ME!", command=metaxeirismena).grid(row=2,column=0,columnspan=2)
        top.maxsize(800,800)


def OpenFood() :
            # Create new page if open Food
        top= Toplevel()
        top.geometry("500x500")
        top.title("Aναζήτησες με κριτήριο : Eστίαση ")
        top.configure(bg='lightblue')
        # when clickarw estiasi,new page me auto
        query_label= Label(top,text="Eμφάνισε τα καταστήματα εστίασης!")
        query_label.grid(row=1,column=0)

    

            
        def estiasi():
                    conn = sqlite3.connect("test.db") 
                    cursor = conn.cursor() 

                    cursor.execute(" SELECT name FROM Store WHERE category='Food' limit 30 ")
                    records=cursor.fetchall()
                    print(records)
                    print_records=''
                    for record in records[0]:
                        print_records += str(record)+ "\n"


                    query_label= Label(top, text=print_records).grid(row=3,column=0,columnspan=2)

                    conn.commit()
                    cursor.close()


        button_query= Button(top, text="CLICK ME!", command=estiasi).grid(row=2,column=0,columnspan=2)
        top.maxsize(800,800)



def OpenGrocery() :
            # Create new page if open Groceries
        top= Toplevel()
        top.geometry("500x500")
        top.title("Aναζήτησες με κριτήριο : Καταστήματα Φαγητού !")
        top.configure(bg='lightblue')
        # when clickarw groceries,new page me auto
        query_label= Label(top,text="Eμφάνισε τα καταστήματα!")
        query_label.grid(row=1,column=0)

    

            
        def Groceries():
                    conn = sqlite3.connect("test.db") 
                    cursor = conn.cursor() 

                    cursor.execute(" SELECT name FROM Store WHERE category='Groceries' limit 30 ")
                    records=cursor.fetchall()
                    print(records)
                    print_records=''
                    for record in records[0]:
                        print_records += str(record)+ "\n"


                    query_label= Label(top, text=print_records).grid(row=3,column=0,columnspan=2)

                    conn.commit()
                    cursor.close()


        button_query= Button(top, text="CLICK ME!", command=Groceries).grid(row=2,column=0,columnspan=2)
        top.maxsize(800,800)




















def search_bar():
        wind=Tk()
        wind.title("Search by store's name")
        wind.geometry("500x500")
        wind.configure(bg='lightblue')


        search_box = Entry(wind,width=30,borderwidth=2)
        search_box.insert(0, "Αναζήτηση")
        search_box.grid(row=4,column=0)

        # when clickarw metaxeirismena,new page me auto
        query_label= Label(wind,text="Γράψε το όνομα του καταστήματος που επιθυμείς!")
        query_label.grid(row=1,column=0)
        
        #Edw ginetai olo to search
        def search_now():
            conn = sqlite3.connect("test.db") 
            cursor = conn.cursor() 

             
            searched = search_box.get()
            sql = "SELECT * FROM Store WHERE name = %s"
            store_name = (searched,  )
             #to execute!1!!1
            result = cursor.execute(sql, store_name)
            result= cursor.fetchall( ) #thee mou den prepei na to 3ana3exasw!!!

            if not result :
                result= "Store not Found..."

            
                
            search_label= Label(wind, text= result )
            search_label.grid(row=6,column=0,padx=10)
        
        search_button = Button (wind,text="Click me!",command= search_now)
        search_button.grid(row=5,column=0,columnspan=2)
        

        
        
    #buttons

button_search= Button(window,text='Click to Search by name!',command=search_bar)
button_search.grid(row=1,column=0,columnspan=2)

news=Button(window, text="Ειδήσεις",height=1,width=20)
news.grid(row=2,column=0)

secondh=Button(window, text="Μεταχειρισμένα",font=('bold'),heigh=1,width=20,command=open)
secondh.grid(row=3,column=0)

estiash=Button(window, text="Χώροι εστίασης",font=('bold'),heigh=1,width=20,command= OpenFood)
estiash.grid(row=4,column=0)

food=Button(window, text="Καταστήματα τροφίμων",font=('bold'),heigh=1,width=20,command=OpenGrocery)
food.grid(row=5,column=0)

    #list of buttons
obj_list=[logo,news,secondh,estiash,food]
    #loop thru the list and config
row_num=0
for button in obj_list:
        Grid.rowconfigure(window,row_num,weight=1)
        row_num+=1

        Grid.columnconfigure(window,0,weight=1)




window.mainloop()