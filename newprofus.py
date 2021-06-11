from tkinter import *
import os
import tkinter as tk 
from tkinter import ttk
from typing import Container
from PIL import ImageTk,Image
from tkinter import messagebox
import sys
from tkinter import filedialog as fd
import sqlite3


database=r"C:\Users\user\Desktop\CEID\Texnologia Logism\users_book.db"


class Application(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        # creating a window
        container = tk.Frame(self)
       
        container.pack(side="top",fill="both",expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        
        for F in (Main_menu,Info_view,Change_Username,Change_Password,Change_Email,Change_Phonenum):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(Main_menu)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


#View Main menu
class Main_menu(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.controller=controller 
        #app logo
        load = Image.open('frienvilogo.png')
        render = ImageTk.PhotoImage(load)
        logo = Label(self, image=render)
        logo.image = render
 
        #menubar
        menu=Menu(self.controller)
        self.controller.config(menu=menu)

        subm1=Menu(menu)
        menu.add_cascade(label="Ρυθμίσεις",menu=subm1)
        subm1.add_command(label="Πληροφορίες")
        subm1.add_command(label="Αλλαγή Στοιχείων Χρήστη",command=lambda: controller.show_frame(Info_view))

        subm2=Menu(menu)
        menu.add_cascade(label="Λογαριασμός",menu=subm2)
        subm2.add_command(label="Αποσύνδεση")

        subm3=Menu(menu)
        menu.add_cascade(label="Αγαπημένα",menu=subm3)

        subm4=Menu(menu)
        menu.add_cascade(label="Αξιολόγηση",menu=subm4)
        subm4.add_command(label="Υποβολή σχολίου")
        subm4.add_command(label="Πρόταση καταστήματος")

    #btn1=Button(root, text="Ρυθμίσεις",command=CreateUserToolsWindow).pack()
    #btn1.grid(row=1,column=3)
       
    #,pady=10,padx=10
    #root.mainloop()

#View profile info
class Info_view(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        def messge():
            MsgBox=messagebox.showinfo('Error','Δυστυχώς δεν μπορείτε να αλλάξετε την ημερομηνία γέννησής σας!')
            

        #tk.Frame.__init__(self,  master)
        usernlbl=Label(self, text="Username", font=('arial', 14))
        usernlbl.pack(side="top", fill="x", pady=5)
        usrnbt=Button(self,cursor="hand2", text='Άλλαξε το username σου',width=35, height=2,bg='white',fg='black',
                    command=lambda: controller.show_frame(Change_Username))
        usrnbt.pack()
        passlbl=Label(self, text="Password", font=('arial', 14))
        passlbl.pack(side="top", fill="x", pady=5)
        passbtn=Button(self,cursor="hand2", text='Άλλαξε το password σου',width=35, height=2,bg='white',fg='black', 
                    command=lambda: controller.show_frame(Change_Password))
        passbtn.pack()
        #tk.Button3(self, text="Άλλαξε την ημερομηνία γέννησής σου").pack()
        emllbl=Label(self, text="Email", font=('arial', 14))
        emllbl.pack(side="top", fill="x", pady=5)
        emlbtn=Button(self,cursor="hand2", text='Άλλαξε το email σου',width=35, height=2,bg='white',fg='black', 
                    command=lambda: controller.show_frame(Change_Email))
        emlbtn.pack()
        #tk.Button4(self, text="Άλλαξε το email σου").pack()
        phnnumlbl=Label(self, text="Τηλέφωνο επικοινωνίας", font=('arial', 14))
        phnnumlbl.pack(side="top", fill="x", pady=5)
        phnumbtn=Button(self,cursor="hand2", text='Άλλαξε το τηλέφωνό επικοινωνίας σου',width=35, height=2,bg='white',fg='black',
                    command=lambda: controller.show_frame(Change_Phonenum))
        phnumbtn.pack()
         #tk.Button2(self, text="Άλλαξε το password σου").pack()
        bdtlbl=Label(self,cursor="hand2", text="Hμερομηνία Γέννησης", font=('arial', 14))
        bdtlbl.pack(side="top", fill="x", pady=5)
        bdtbtn=Button(self,cursor="hand2", text='Άλλαξε την ημερομηνία γέννησής σου',width=35, height=2,bg='white',fg='black',
                     command=messge)
        bdtbtn.pack()
        #tk.Button5(self, text="Άλλαξε το τηλέφωνό επικοινωνίας σου").pack()
        #Label5=Label(self, text="Page one", font=('ariel', 18, "bold")).pack(side="top", fill="x", pady=5)
        #tk.Button(self,cursor="hand2", text="Επιστροφή στην αρχική",command=self.destroy).pack()
        goback=tk.Button(self,text='Επιστροφή στην αρχική',width=20, height=1,command=lambda: controller.show_frame(Main_menu))
        goback.pack()

#Create a profile
class Change_Username(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        #app logo
        load = Image.open('frienvilogo.png')
        render = ImageTk.PhotoImage(load)
        logo = Label(self, image=render)
        logo.image = render
        
        global usrnme
        global usrnme_chnged

        def login():
            try:
                #Connect to the database
                conn=sqlite3.connect(database)
                #Create Cursor
                c=conn.cursor()

                #record_id = delete_box.get()
                c.execute("select * from users where username=?",(usrnme.get(),))
                row=c.fetchone()
                if row==None:
                    messagebox.showerror("Error",f"Μη έγκυρα στοιχεία. Προσπαθήστε ξανά!",parent=self)
                else:
                    messagebox.showinfo("Success",f"Επιτυχής Καταχώρηση Στοιχείων!",parent=self)                                  
                #commit changes
                conn.commit()
                #close connection
                conn.close()
            except Exception as es: 
                messagebox.showerror("Error",f"Σφάλμα εξαιτίας : {str(es)}",parent=self)

        def update():
                #Connect to the database
                conn=sqlite3.connect(database)
                #Create Cursor
                c=conn.cursor()

                #record_id = delete_box.get()
                c.execute("""UPDATE users SET 
                    username = ?          
                    WHERE username =?""",(usrnme_chnged.get(),usrnme.get()) 
                )
                #commit changes
                conn.commit()

                #close connection
                conn.close()

        #Create text boxes        
        usrnme= Entry(self,width=30)
        usrnme.grid(row=0,column=1,padx=20,pady=(10,0))

        usrnme_chnged= Entry(self,width=30)
        usrnme_chnged.grid(row=2,column=1,padx=20,pady=(10,0))

        #create text box label
        usrnme_label1=Label(self, text="Εισάγετε το τρέχον όνομα χρήστη σας")
        usrnme_label1.grid(row=0,column=0)
        usrnme_label2=Label(self, text="Εισάγετε το νέο όνομα χρήστη σας")
        usrnme_label2.grid(row=2,column=0)
        
        #create Submit button
        submit_btn= Button(self,text="Τρέχοντα Στοιχεία",command=login)
        submit_btn.grid(row=1,column=1,pady=10,padx=10)

        #Create Query Button
        query_btn= Button(self,text="Επιβεβαίωση",command=update)
        query_btn.grid(row=3,column=1,pady=10,padx=10)

        #Create an update button
        #update_btn= Button(editor,text="Update",command=update1)
        #update_btn.grid(row=4,column=0,pady=10,padx=10)

        #Create button to save edited record
        #save_btn= Button(editor,text="Αποθήκευση Αλλαγών",command=update)
        #save_btn.grid(row=4,column=0,pady=10,padx=10)

        #return back
        #goback=Button(editor,text='Επιστροφή',width=20, height=1,bg='black',fg='white',command=self.destroy)
        #goback.grid(row=5,column=1,pady=10,padx=10)

        goback=Button(self,text='Επιστροφή',width=20, height=1,bg='black',fg='white',command=lambda: controller.show_frame(Info_view))
        goback.grid(row=5,column=1)
       

#Create a profile
class Change_Password(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        #app logo
        load = Image.open('frienvilogo.png')
        render = ImageTk.PhotoImage(load)
        logo = Label(self, image=render)
        logo.image = render

        global password1
        global password1_chnged


        def login():
            try:
                #Connect to the database
                conn=sqlite3.connect(database)
                #Create Cursor
                c=conn.cursor()

                #record_id = delete_box.get()
                c.execute("select * from users where password=?",(password1.get(),))
                row=c.fetchone()
                if row==None:
                    messagebox.showerror("Error",f"Μη έγκυρα στοιχεία. Προσπαθήστε ξανά!",parent=self)
                else:
                    messagebox.showinfo("Success",f"Επιτυχής Καταχώρηση Στοιχείων!",parent=self)                                  
                #commit changes
                conn.commit()
                #close connection
                conn.close()
            except Exception as es: 
                messagebox.showerror("Error",f"Σφάλμα εξαιτίας : {str(es)}",parent=self)

        def submit():
            #Connect to the database
            conn=sqlite3.connect(database)
            #Create Cursor
            c=conn.cursor()
            #Insert into table
            c.execute("INSERT INTO users VALUES (:password)",
                {
                    'password': password1.get()
                }
            )

            #commit changes
            conn.commit()

            #close connection
            conn.close()

        def update():
            #Connect to the database
            conn=sqlite3.connect(database)
            #Create Cursor
            c=conn.cursor()

            #record_id = delete_box.get()
            c.execute("""UPDATE users  SET password =?          

                WHERE password = ?""",(password1_chnged.get(),password1.get())
            )
            
            #commit changes
            conn.commit()

            #close connection
            conn.close()

        password1= Entry(self,width=30)
        password1.grid(row=0,column=1)

        password1_chnged= Entry(self,width=30)
        password1_chnged.grid(row=2,column=1)

        #create text box label
        password1_label1=Label(self, text="Εισάγετε τον τρέχοντα κωδικό σας")
        password1_label1.grid(row=0,column=0)
        password1_chnged_label2=Label(self, text="Εισάγετε τον νέο κωδικό σας")
        password1_chnged_label2.grid(row=2,column=0)
        #create Submit button
        submit_btn= Button(self,text="Τρέχοντα Στοιχεία",command=login)
        submit_btn.grid(row=1,column=1,pady=10,padx=10)
        #Create Query Button
        query_btn= Button(self,text="Επιβεβαίωση",command=update)
        query_btn.grid(row=3,column=1,pady=10,padx=10)
        goback=tk.Button(self,text='Επιστροφή',width=20, height=1,bg='black',fg='white',command=lambda: controller.show_frame(Info_view))
        goback.grid(row=5,column=1)


        #Create a profile
class Change_Email(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        #app logo
        load = Image.open('frienvilogo.png')
        render = ImageTk.PhotoImage(load)
        logo = Label(self, image=render)
        logo.image = render

        global email1
        global email1_chnged

        def login():
            try:
                #Connect to the database
                conn=sqlite3.connect(database)
                #Create Cursor
                c=conn.cursor()

                #record_id = delete_box.get()
                c.execute("select * from users where email=?",(email1.get(),))
                row=c.fetchone()
                if row==None:
                    messagebox.showerror("Error",f"Μη έγκυρα στοιχεία. Προσπαθήστε ξανά!",parent=self)
                else:
                    messagebox.showinfo("Success",f"Επιτυχής Καταχώρηση Στοιχείων!",parent=self)                                  
                #commit changes
                conn.commit()
                #close connection
                conn.close()
            except Exception as es: 
                messagebox.showerror("Error",f"Σφάλμα εξαιτίας : {str(es)}",parent=self)

        def submit():
            #Connect to the database
            conn=sqlite3.connect(database)
            #Create Cursor
            c=conn.cursor()
            #Insert into table
            c.execute("INSERT INTO users VALUES (:email)",
                {
                    'email': email1.get()
                }
            )

            #commit changes
            conn.commit()

            #close connection
            conn.close()
        
        
        def update():
            #Connect to the database
            conn=sqlite3.connect(database)
            #Create Cursor
            c=conn.cursor()

            #record_id = delete_box.get()
            c.execute("""UPDATE users  SET email = ?              

                WHERE email = ?""",(email1_chnged.get(),email1.get())
            )
            
            #commit changes
            conn.commit()

            #close connection
            conn.close()

    
        email1= Entry(self,width=30)
        email1.grid(row=0,column=1)

        email1_chnged= Entry(self,width=30)
        email1_chnged.grid(row=2,column=1)

        #create text box label
        email1_label1=Label(self, text="Εισάγετε το τρέχον email σας")
        email1_label1.grid(row=0,column=0)
        email1_chnged_label2=Label(self, text="Εισάγετε τον νέο email σας")
        email1_chnged_label2.grid(row=2,column=0)
        #create Submit button
        submit_btn= Button(self,text="Τρέχοντα Στοιχεία",command=login)
        submit_btn.grid(row=1,column=1,pady=10,padx=10)
        #Create Query Button
        query_btn= Button(self,text="Επιβεβαίωση",command=update)
        query_btn.grid(row=3,column=1,pady=10,padx=10)
        #Create Query Button
        #query_btn= Button(editor2,text="Show change",command=query)
        #query_btn.grid(row=4,column=1,pady=10,padx=10)
        goback=tk.Button(self,text='Επιστροφή',width=20, height=1,bg='black',fg='white',command=lambda: controller.show_frame(Info_view))
        goback.grid(row=5,column=1)
        
        #Create a profile
class Change_Phonenum(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        #app logo
        load = Image.open('frienvilogo.png')
        render = ImageTk.PhotoImage(load)
        logo = Label(self, image=render)
        logo.image = render   

        global phone_num1
        global phone_num1_chnged

        def login():
            try:
                #Connect to the database
                conn=sqlite3.connect(database)
                #Create Cursor
                c=conn.cursor()

                #record_id = delete_box.get()
                c.execute("select * from users where phone_num=?",(phone_num1.get(),))
                row=c.fetchone()
                if row==None:
                    messagebox.showerror("Error",f"Μη έγκυρα στοιχεία. Προσπαθήστε ξανά!",parent=self)
                else:
                    messagebox.showinfo("Success",f"Επιτυχής Καταχώρηση Στοιχείων!",parent=self)                                  
                #commit changes
                conn.commit()
                #close connection
                conn.close()
            except Exception as es: 
                messagebox.showerror("Error",f"Σφάλμα εξαιτίας : {str(es)}",parent=self)



        def update():
            #Connect to the database
            conn=sqlite3.connect(database)
            #Create Cursor
            c=conn.cursor()

            #record_id = delete_box.get()
            c.execute("""UPDATE users  SET phone_num = ?             

                WHERE phone_num = ?""",(phone_num1_chnged.get(),phone_num1.get())
            )
            
            #commit changes
            conn.commit()

            #close connection
            conn.close()

        def submit():
            #Connect to the database
            conn=sqlite3.connect(database)
            #Create Cursor
            c=conn.cursor()
            #Insert into table
            c.execute("INSERT INTO users VALUES (:phone_num)",
                {
                    'phone_num': phone_num1.get()
                }
            )

            #commit changes
            conn.commit()

            #close connection
            conn.close()

        phone_num1= Entry(self,width=30)
        phone_num1.grid(row=0,column=1)

        phone_num1_chnged= Entry(self,width=30)
        phone_num1_chnged.grid(row=2,column=1)

        #create text box label
        phone_num1_label1=Label(self, text="Εισάγετε το τρέχον τηλέφωνο επικοινωνίας σας")
        phone_num1_label1.grid(row=0,column=0)
        phone_num1_chnged_label2=Label(self, text="Εισάγετε τον νέο τηλέφωνο επικοινωνίας σας")
        phone_num1_chnged_label2.grid(row=2,column=0)
        #create Submit button
        submit_btn= Button(self,text="Τρέχοντα Στοιχεία",command=login)
        submit_btn.grid(row=1,column=1,pady=10,padx=10)
        #Create Query Button
        query_btn= Button(self,text="Επιβεβαίωση",command=update)
        query_btn.grid(row=3,column=1,pady=10,padx=10)
        #Create Query Button
        #Create Query Button
        #query_btn= Button(editor3,text="Show change",command=query)
        #query_btn.grid(row=4,column=1,pady=10,padx=10)
        goback=tk.Button(self,text='Επιστροφή',width=20, height=1,bg='black',fg='white',command=lambda: controller.show_frame(Info_view))
        goback.grid(row=5,column=1)


        #Create a profile
#class Change_Birthdate(tk.Frame):
 #   def __init__(self, parent, controller):
  #     tk.Frame.__init__(self, parent)
        
        #app logo
   #    load = Image.open('frienvilogo.png')
    #   render = ImageTk.PhotoImage(load)
     #  logo = Label(self, image=render)
      # logo.image = render 

    #def submit_article():
       #tk.messagebox.showinfo('Error','Δυστυχώς δεν μπορείτε να αλλάξετε την ημερομηνία γέννησής σας!')
        #goback=tk.Button(self,text='Επιστροφή',width=20, height=1,bg='black',fg='white',command=lambda: controller.show_frame(Info_view))


app = Application()
app.mainloop()