from datetime import date, datetime
from sqlite3.dbapi2 import Date
from tkinter import *
import os
from PIL import ImageTk,Image
from tkinter import messagebox
import sqlite3

database=r"C:\Users\user\Desktop\CEID\Τεχνολογια Λογισμ\users_book.db"


main_screen = Tk()
main_screen.title('Frienvi log in')
main_screen.geometry("450x450")
#app logo
logo= Canvas(main_screen, width = 190, height = 91)
img = ImageTk.PhotoImage(Image.open('frienvilogo.png'))
logo.create_image(10,10,anchor=NW, image=img)
#log in input,username,password
login_screen=Label(main_screen,text='Log in',font=('calibri', 20,'bold'))
message=Label(main_screen,text='Log in to access your account',font=('calibri', 8),fg='grey')
usertext = Label(main_screen, text='Username')
passwordtext = Label(main_screen, text='Password')
user = Entry(main_screen, textvariable=StringVar())
password = Entry(main_screen, show='*', textvariable=StringVar()) #the password isn't showinng instead it shows only *
check=Checkbutton(main_screen,text='Keep me signed in')


#register main_screen
def register():
    global register_screen
    register_screen = Toplevel(main_screen)
    register_screen.title("Frienvi Register")
    register_screen.geometry("450x450")

    #showing logo to the new window
    logo2 = Canvas(register_screen, width = 190, height = 91)
    img2 = ImageTk.PhotoImage(Image.open('frienvilogo.png'))
    logo2.create_image(10,10,anchor=NW, image=img)

    global username
    global pssword
    global email
    global phonenumb
    global birthdate
    username = StringVar()
    pssword = StringVar()
    email = StringVar()
    phonenumb=IntVar()
    birthdate=datetime(1900,1,1)

    def submit():
        #Connect to the database
        conn=sqlite3.connect(database)
        #Create Cursor
        c=conn.cursor()
        #Insert into table
        c.execute("INSERT INTO users VALUES (:username, :password, :email, :phone_num, :birth_date)",
        {
            'username': username.get(),
            'password': pssword.get(),
            'email': email.get(),
            'phone_num': phonenumb.get(),
            'birth_date': birthdate.date()
        }
        )
        row=c.fetchall()
        if row==None:
            messagebox.showerror("Error",f"Μη έγκυρα στοιχεία. Προσπαθήστε ξανά!",parent=register_screen)
        else:
            messagebox.showinfo("Success",f"Επιτυχής Καταχώρηση Στοιχείων!",parent=main_screen)
        
        #commit changes
        conn.commit()

        #close connection
        conn.close()


    username_lable = Label(register_screen, text="Username")
    username_entry = Entry(register_screen, textvariable=username)
    password_lable = Label(register_screen, text="Password")
    password_entry = Entry(register_screen, textvariable=pssword)    
    email_lable = Label(register_screen, text="Email")
    email_entry = Entry(register_screen, textvariable=email)
    phonenum_lable = Label(register_screen, text="Τηλέφωνο Επικοινωνίας")
    phonenum_entry = Entry(register_screen, textvariable=phonenumb)
    birthdate_lable = Label(register_screen, text="Ημερομηνία Γέννησης")
    birthdate_entry = Entry(register_screen, textvariable=birthdate)

    logo2.pack()
    Label(register_screen, text="Enter your account details").pack(pady=(0,20))
    username_lable.pack()
    username_entry.pack()
    password_lable.pack()
    password_entry.pack(pady=(0,20))
    email_lable.pack()
    email_entry.pack()
    phonenum_lable.pack()
    phonenum_entry.pack()
    birthdate_lable.pack()
    birthdate_entry.pack()
    
    Button(register_screen, text="Register", width=10, height=1,command=submit).pack()       


def login():
    if user.get()=="" or password.get()=="":
        messagebox.showerror("Error","Όλα τα πεδία είναι υποχρεωτικά",parent=main_screen)
    else:
        try:
            #Connect to the database
            conn=sqlite3.connect(database)
            #Create Cursor
            c=conn.cursor()
            c.execute("select * from users where username=? and password=?",(user.get(),password.get()))
            row=c.fetchone()
            if row==None:
                messagebox.showerror("Error",f"Μη έγκυρα στοιχεία. Προσπαθήστε ξανά!",parent=main_screen)
            else:
                messagebox.showinfo("Success",f"Καλωσήρθατε",parent=main_screen)
            #commit changes
            conn.commit()
            #close connection
            conn.close()
        except Exception as es: 
            messagebox.showerror("Error",f"Σφάλμα εξαιτίας : {str(es)}",parent=main_screen)

#main log in screen
logo.pack(pady=(0,20))
login_screen.pack(pady=(0,20))
message.pack()
usertext.pack()
user.pack()
passwordtext.pack()
password.pack()
check.pack(pady=(20,0))
Button(text="Log in",width=16, height=1,bg='black',fg='white',command=login).pack()
Label(text="Dont't have any accounts?",font=('calibri', 8)).pack()
Button(text="Sign up", height="1", width="5", command=register).pack()

main_screen.mainloop()        
