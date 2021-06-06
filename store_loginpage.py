from tkinter import *
import os
import tkinter as tk 
from PIL import ImageTk,Image
from tkinter import messagebox
import sys
import sqlite3



# main store log in page
class Store_login(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        #app logo
        load = Image.open('frienvilogo.png')
        render = ImageTk.PhotoImage(load)
        logo = Label(self, image=render)
        logo.image = render

        label_1=Label(self, text="Έχετε επιβεβαιώσει την εισαγωγή σας ως κατάστημα;",font=('ariel', 10))

        button_1=tk.Button(self, text='Αίτηση εισαγωγής',width=40, height=2,bg='black',fg='white', command=lambda: controller.show_frame(EntryRequest))
        button_2=tk.Button(self, text='Δημιουργία Προφίλ Καταστήματος',width=40, height=2,bg='black',fg='white')

        logo.grid(row=0,column=0)
        label_1.grid(row=1,column=0)
        button_1.grid(row=2,column=0)
        button_2.grid(row=3,column=0)

        #list of buttons
        obj_list=[logo,label_1,button_1,button_2]
        #loop thru the list and config
        row_num=0
        for button in obj_list:
            Grid.rowconfigure(self,row_num,weight=1)
            row_num+=1

        Grid.columnconfigure(self,0,weight=1)

        

#entry request page
class EntryRequest(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        conn = sqlite3.connect("store_entryrequest.db") 
        cursor = conn.cursor()

        #create table Store 
        #cursor.execute(""" CREATE TABLE Store (storename text, details text, eco text, info text)""")

        def submit() : 
            conn = sqlite3.connect("store_entryrequest.db") 
            cursor = conn.cursor() 


            #Insert Into Table
            cursor.execute("INSERT INTO Store VALUES (:storename, :details, :eco, :info)",
                {
                    'storename':storename.get(),
                    'details':details.get("1.0",'end-1c'),
                    'eco':eco.get("1.0",'end-1c'),
                    'info':info.get("1.0",'end-1c'),
            
                }
            )


            conn.commit()
            cursor.close()

            #delete για να μπαίνουν  νέα στοιχεία κάθε φορά 
            storename.delete(0,END)
            details.delete(0,END)
            eco.delete(0,END)
            info.delete(0,END)
        '''        
        show the database info to see if it works 
        def query():
    
            conn = sqlite3.connect("store_entryrequest.db") 
            cursor = conn.cursor() 
            #query the database 
            cursor.execute("SELECT * , oid FROM Store")
            records=cursor.fetchall()
            print(records)

        '''
        
        #app logo
        load = Image.open('frienvilogo.png')
        render = ImageTk.PhotoImage(load)
        logo = Label(self, image=render)
        logo.image = render

        global storename
        storename=StringVar()
        

        #labels
        label_1=Label(self, text="Αίτηση εισαγωγής",font=('ariel', 20,'bold'))
        label_2=Label(self, text="Όνομα Καταστήματος",font=('ariel', 10))
        label_3=Label(self, text="Πείτε μας λίγα λόγια για την επιχειρησή σας",font=('ariel', 10))
        label_4=Label(self, text="Ενημερώστε μας για την επίπτωση που έχει το κατάστημά σας στο περιβάλλον",font=('ariel', 10))
        label_5=Label(self, text="Γιατί πιστεύεται πρέπει να σας προσθέσουμε στην εφαρμογή;",font=('ariel', 10))

        #entry boxes
        storename=Entry(self,textvariable=storename)
        details=Text(self,width="20", height="2")
        eco=Text(self,width="20", height="2")
        info=Text(self,width="20", height="2")

        #buttons
        confirm=tk.Button(self,text='Επιβεβαίωση',width=20, height=1,bg='black',fg='white',command=lambda: [submit,controller.show_frame(DocumentsList)]) 
        goback=tk.Button(self,text='Επιστροφή',width=20, height=1,bg='black',fg='white',command=lambda: controller.show_frame(Store_login))
        # to show the database info
        # show=tk.Button(self,text='show',width=20, height=1,bg='black',fg='white',command=query)

        #the entry request screen
        logo.grid(row=0,column=0)
        label_1.grid(row=1,column=0)
        label_2.grid(row=2,column=0)
        storename.grid(row=2,column=1)
        label_3.grid(row=3,column=0)
        details.grid(row=3,column=1,ipadx=30,ipady=30)
        label_4.grid(row=4,column=0)
        eco.grid(row=4,column=1,ipadx=30,ipady=30)
        label_5.grid(row=5,column=0)
        info.grid(row=5,column=1,ipadx=30,ipady=30)
        confirm.grid(row=6,column=1)
        goback.grid(row=6,column=2)
        #show.grid(row=7,column=0)
        

        #list of buttons
        obj_list=[logo,label_1,label_2,storename,label_3,details,label_4,eco,label_5,info,confirm,goback]
        #loop thru the list and config
        row_num=0
        for button in obj_list:
            Grid.rowconfigure(self,row_num,weight=1)
            row_num+=1

        Grid.columnconfigure(self,0,weight=1)

    

        

#document list page
class DocumentsList(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        global name
        name=StringVar()
        
        conn = sqlite3.connect("store_applications.db") 
        cursor = conn.cursor()

        #create table Store 
        #cursor.execute(""" CREATE TABLE Store_entry (sname text, adeia text, ecoinfo text, contactdetails text, storedetails text)""")

        def submit() : 
            conn = sqlite3.connect("store_applications.db") 
            cursor = conn.cursor() 


            #Insert Into Table
            cursor.execute("INSERT INTO Store_entry VALUES (:sname, :adeia, :ecoinfo, :contactdetails, :storedetails)",
                {
                    'sname':sname.get(),
                    'adeia':adeia.get("1.0",'end-1c'),
                    'ecoinfo':ecoinfo.get("1.0",'end-1c'),
                    'contackdetails':contactdetails.get("1.0",'end-1c'),
                    'storedetails':storedetails.get("1.0",'end-1c')
            
                }
            )


            conn.commit()
            cursor.close()

            #delete για να μπαίνουν  νέα στοιχεία κάθε φορά 
            sname.delete(0,END)
            adeia.delete(0,END)
            ecoinfo.delete(0,END)
            contactdetails.delete(0,END)
            storedetails.delete(0,END)

        '''
        #show the database info to see if it works 
        def query():
    
            conn = sqlite3.connect("store_applications.db") 
            cursor = conn.cursor() 
            #query the database 
            cursor.execute("SELECT * , oid FROM Store_entry")
            records=cursor.fetchall()
            print(records)
        '''
        
        def submit_application():
            MsgBox=tk.messagebox.showinfo("Confirm","Η αίτηση σας καταχωρήθηκε.") 
            if MsgBox == 'ok':
                sys.exit()


        #app logo
        load = Image.open('frienvilogo.png')
        render = ImageTk.PhotoImage(load)
        logo = Label(self, image=render)
        logo.image = render

        

        #labels
        label_1=Label(self, text="Λίστα δικαιολογητικών",font=('ariel', 20,'bold'))
        label_2=Label(self, text="Όνομα καταστήματος",font=('ariel', 10))
        label_3=Label(self, text="Άδεια λειτουργίας καταστήματος",font=('ariel', 10))
        label_4=Label(self, text="Έγγραφο οικολογικού αντίκτυπου",font=('ariel', 10))
        label_5=Label(self, text="Πληροφορίες επικοινωνίας",font=('ariel', 10))
        label_6=Label(self, text="Πληροφορίες καταστήματος",font=('ariel', 10))

        #entry boxes
        sname=Entry(self,textvariable=name)
        adeia=Text(self,width="10", height="1")
        ecoinfo=Text(self,width="10", height="1")
        contactdetails=Text(self,width="20", height="2")
        storedetails=Text(self,width="20", height="2")

        #buttons
        confirm=tk.Button(self,text='Επιβεβαίωση',width=20, height=1,bg='black',fg='white',command=lambda: [submit_application,submit])
        goback=tk.Button(self,text='Επιστροφή',width=20, height=1,bg='black',fg='white',command=lambda: controller.show_frame(EntryRequest))

        #show=tk.Button(self,text='show',width=20, height=1,bg='black',fg='white',command=query)

        #the document list screen
        logo.grid(row=0,column=0)
        label_1.grid(row=1,column=0)
        label_2.grid(row=2,column=0)
        sname.grid(row=2,column=1)
        label_3.grid(row=3,column=0)
        adeia.grid(row=3,column=1)
        label_4.grid(row=4,column=0)
        ecoinfo.grid(row=4,column=1,ipadx=30,ipady=30)
        label_5.grid(row=5,column=0)
        contactdetails.grid(row=5,column=1,ipadx=30,ipady=30)
        label_6.grid(row=6,column=0)
        storedetails.grid(row=6,column=1,ipadx=30,ipady=30)
        confirm.grid(row=7,column=1)
        goback.grid(row=7,column=2)
        #show.grid(row=8,column=0)

        #list of buttons
        obj_list=[logo,label_1,label_2,sname,label_3,adeia,label_4,ecoinfo,label_5,contactdetails,label_6,storedetails,confirm,goback]
        #loop thru the list and config
        row_num=0
        for button in obj_list:
            Grid.rowconfigure(self,row_num,weight=1)
            row_num+=1

        Grid.columnconfigure(self,0,weight=1)



class Application(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        # creating a window
        window = tk.Frame(self)
        window.pack()

        window.grid_rowconfigure(0, minsize=500)
        window.grid_columnconfigure(0, minsize=900)

        self.frames = {}
        for F in (Store_login, EntryRequest,DocumentsList):
            frame = F(window, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(Store_login)

    def show_frame(self, page):
        frame = self.frames[page]
        frame.tkraise()
        self.title("Store page")
        


app = Application()
app.maxsize(1000, 500)
app.mainloop()
