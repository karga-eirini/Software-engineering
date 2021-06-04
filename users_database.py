from tkinter import *
from PIL import ImageTk, Image
import sqlite3

root= Tk()
root.geometry("400x400")

#Databases 

#Create a database 
conn=sqlite3.connect('users_book.db')

#Create cursor
c= conn.cursor()

#Create table
c.execute("""CREATE TABLE users (
    username text,
    password text,
    email text,
    phone_num integer,
    birth_date date
)""")


#Commit Changes
conn.commit()

#Close Connection
conn.close()

root.mainloop()