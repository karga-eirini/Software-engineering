from tkinter import *
from PIL import ImageTk, Image
import sqlite3


root=Tk()
root.geometry("400x400")

#Delete empty/false rows
def delete():
    #Connect to the database
    conn=sqlite3.connect('users_book.db')
    #Create Cursor
    c=conn.cursor()
    #Insert into table

    c.execute("DELETE from users WHERE username='' OR password='' Or email='' ")

    #commit changes
    conn.commit()

    #close connection
    conn.close()


def submit():
    #Connect to the database
    conn=sqlite3.connect('users_book.db')
    #Create Cursor
    c=conn.cursor()
    #Insert into table
    c.execute("INSERT INTO users VALUES (:username, :password, :email, :phone_num, :birth_date)",
    {
        'username': username.get(),
        'password': password.get(),
        'email': email.get(),
        'phone_num': phone_num.get(),
        'birth_date': birth_date.get()
    }
)

    username.delete(0,END)
    password.delete(0,END)
    email.delete(0,END)
    phone_num.delete(0,END)
    birth_date.delete(0,END)


    #commit changes
    conn.commit()

    #close connection
    conn.close()


#create Query function
def query():
    #Connect to the database
    conn=sqlite3.connect('users_book.db')
    #Create Cursor
    c=conn.cursor()

    #Query the database
    c.execute("SELECT *, oid FROM users")
    records = c.fetchall()
    #print(records)

    #Loop Thru Results
    print_records=''
    for record in records:
        print_records += str(record) +"\n"

    query_label = Label(root, text= print_records)
    query_label.grid(row=15,column=1,rowspan=2)

    #commit changes
    conn.commit()

    #close connection
    conn.close()

#Create text boxes
username=Entry(root,width=30)
username.grid(row=0,column=1,padx=20,pady=(10,0))
password=Entry(root,width=30)
password.grid(row=1,column=1,padx=20)
email=Entry(root,width=30)
email.grid(row=2,column=1,padx=20)
phone_num=Entry(root,width=30)
phone_num.grid(row=3,column=1,padx=20)
birth_date=Entry(root,width=30)
birth_date.grid(row=4,column=1,padx=20)
delete_box=Entry(root, width=30)
delete_box.grid(row=8,column=1)

#Create text box Labels
username_label=Label(root,text="Όνομα Χρήστη")
username_label.grid(row=0,column=0,pady=(10,0))
password_label=Label(root,text="Κωδικός Πρόσβασης")
password_label.grid(row=1,column=0)
email_label=Label(root,text="Email")
email_label.grid(row=2,column=0)
phone_num_label=Label(root,text="Τηλέφωνο Επικοινωνίας")
phone_num_label.grid(row=3,column=0)
birth_date_label=Label(root,text="Ημερομηνία Γέννησης")
birth_date_label.grid(row=4,column=0)
delete_box_label=Label(root,text="Delete ID")
delete_box_label.grid(row=8,column=0)
#Create submit button
submit_btn=Button(root,text="Πρόσθήκη στη Βάση Δεδομένων",command=submit)
submit_btn.grid(row=5,column=0,columnspan=2,pady=10,padx=10,ipadx=100)

#Create a Query Button
query_btn= Button(root,text="Εμφάνισε Στοιχεία Χρηστών",command=query)
query_btn.grid(row=6,column=0,columnspan=2,pady=10,padx=10,ipadx=100)

#Create a Delete Button
delete_btn= Button(root,text="Διαγραφή Κενών Χρηστών",command=delete)
delete_btn.grid(row=9,column=0,columnspan=2,pady=10,padx=10,ipadx=100)

root.mainloop()
