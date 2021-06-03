from tkinter import *
from tkinter import messagebox
import os
from PIL import ImageTk,Image

import sqlite3
#databases

root= Tk()
root.title("This is from Database!")
root.geometry("400x400")

conn = sqlite3.connect("test.db") # connect to test.db 
cursor = conn.cursor() # get a cursor to the sqlite database (CREATE CURSOR)
###cursor is the object here, you can use any name
#cursor.commit() #commit changes 
#cursor.close()  #close connection


 
 #Create Submit Function For Database Store
def submit() : 
    conn = sqlite3.connect("test.db") 
    cursor = conn.cursor() 


    #Insert Into Table
    cursor.execute("INSERT INTO Store VALUES (:store_name, :store_location, :store_hours, :store_products, :store_category )",
        {
            'store_name':store_name.get(),
            'store_location':store_location.get(),
            'store_hours':store_hours.get(),
            'store_products':store_products.get(),
            'store_category':store_category.get()
    
        }
     )




    conn.commit()
    cursor.close()

    #delete για να μπαίνουν  νέα στοιχεία κάθε φορά 
    store_name.delete(0,END)
    store_location.delete(0,END)
    store_hours.delete(0,END)
    store_products.delete(0,END)
    store_category.delete(0,END)





#create table Store 

#cursor.execute(""" CREATE TABLE Store (name text, location text, products text, 
               # hours text, category text)""")




#create TextBoxes to insert information to it 

store_name= Entry(root,width=30)
store_name.grid(row=0, column=1, padx=20)

store_location= Entry(root,width=30)
store_location.grid(row=1, column=1, padx=20)

store_products= Entry(root,width=30)
store_products.grid(row=2, column=1, padx=20)

store_hours= Entry(root,width=30)
store_hours.grid(row=3, column=1, padx=20)

store_category= Entry(root,width=30)
store_category.grid(row=4, column=1, padx=20)

#create TextBoxLabels

store_name_label= Label(root,text="Store's name")
store_name_label.grid(row=0, column=0)

store_location_label= Label(root,text=" Location")
store_location_label.grid(row=1, column=0)

store_products_label= Label(root,text='Plithos proionton')
store_products_label.grid(row=2, column=0)

store_hours_label = Label (root, text ='Hours open')
store_hours_label.grid(row=3, column=0)

store_category_label= Label(root,text='Category')
store_category_label.grid(row=4, column=0)

#lista me ola osa einai sthn bash na print
def query():

    conn = sqlite3.connect("test.db") 
    cursor = conn.cursor() 
    #query the database 
    cursor.execute("SELECT * , oid FROM Store")
    records=cursor.fetchall()
    print(records)
    #print_records = ''
    #for records in records[0] :
       # print_records += str (records)+ "\n"

    #query_label= Label(root,text='print_records')
    #query_label.grid(row=0,column=0,columnspan=0)
    


#Create Submit Button
SubmitButton = Button (root,text="Add to record to Database",command=submit)
SubmitButton.grid(row=6,column=0,columnspan=2,pady=10,padx=10,ipadx=100)

#Create Button Query

koumpi= Button(root,text='MΕΤΑΧΕΙΡΙΣΜΕΝΑ:',command=query )
koumpi.grid(row=8, column=0, columnspan=2,padx=2,pady=2,ipadx=138)













root.mainloop()
