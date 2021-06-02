from tkinter import *
import os
import tkinter as tk 
from PIL import ImageTk,Image
from tkinter import messagebox
import sys

def submit_application():
    MsgBox=tk.messagebox.showinfo("Confirm","Η αίτηση σας καταχωρήθηκε.") 
    if MsgBox == 'ok':
        sys.exit()


       
       
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
        
        
        #app logo
        load = Image.open('frienvilogo.png')
        render = ImageTk.PhotoImage(load)
        logo = Label(self, image=render)
        logo.image = render

        global storename
        global details
        global eco
        global info
        storename=StringVar()
        details=StringVar()
        eco=StringVar()
        info=StringVar()

        #labels
        label_1=Label(self, text="Αίτηση εισαγωγής",font=('ariel', 20,'bold'))
        label_2=Label(self, text="Όνομα Καταστήματος",font=('ariel', 10))
        label_3=Label(self, text="Πείτε μας λίγα λόγια για την επιχειρησή σας",font=('ariel', 10))
        label_4=Label(self, text="Ενημερώστε μας για την επίπτωση που έχει το κατάστημά σας στο περιβάλλον",font=('ariel', 10))
        label_5=Label(self, text="Γιατί πιστεύεται πρέπει να σας προσθέσουμε στην εφαρμογή;",font=('ariel', 10))

        #entry boxes
        storename=Entry(self,textvariable=storename)
        details=Entry(self,textvariable=details)
        eco=Entry(self,textvariable=eco)
        info=Entry(self,textvariable=info)

        #buttons
        confirm=tk.Button(self,text='Επιβεβαίωση',width=20, height=1,bg='black',fg='white',command=lambda: controller.show_frame(DocumentsList))
        goback=tk.Button(self,text='Επιστροφή',width=20, height=1,bg='black',fg='white',command=lambda: controller.show_frame(Store_login))

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
        

        #app logo
        load = Image.open('frienvilogo.png')
        render = ImageTk.PhotoImage(load)
        logo = Label(self, image=render)
        logo.image = render

        global storelist
        global adeia
        global ecoinfo
        global storedetails
        storelist=StringVar()
        adeia=StringVar()
        ecoinfo=StringVar()
        storedetails=StringVar()

        #labels
        label_1=Label(self, text="Λίστα δικαιολογητικών",font=('ariel', 20,'bold'))
        label_2=Label(self, text="Άδεια λειτουργίας καταστήματος",font=('ariel', 10))
        label_3=Label(self, text="Έγγραφο οικολογικού αντίκτυπου",font=('ariel', 10))
        label_4=Label(self, text="Πληροφορίες επικοινωνίας",font=('ariel', 10))
        label_5=Label(self, text="Πληροφορίες καταστήματος",font=('ariel', 10))

        #entry boxes
        storelist=Entry(self,textvariable=storelist)
        adeia=Entry(self,textvariable=adeia)
        ecoinfo=Entry(self,textvariable=ecoinfo)
        storedetails=Entry(self,textvariable=storedetails)

        #buttons
        confirm=tk.Button(self,text='Επιβεβαίωση',width=20, height=1,bg='black',fg='white',command=submit_application)
        goback=tk.Button(self,text='Επιστροφή',width=20, height=1,bg='black',fg='white',command=lambda: controller.show_frame(EntryRequest))

        #the document list screen
        logo.grid(row=0,column=0)
        label_1.grid(row=1,column=0)
        label_2.grid(row=2,column=0)
        storelist.grid(row=2,column=1)
        label_3.grid(row=3,column=0)
        adeia.grid(row=3,column=1,ipadx=30,ipady=30)
        label_4.grid(row=4,column=0)
        ecoinfo.grid(row=4,column=1,ipadx=30,ipady=30)
        label_5.grid(row=5,column=0)
        storedetails.grid(row=5,column=1,ipadx=30,ipady=30)
        confirm.grid(row=6,column=1)
        goback.grid(row=6,column=2)

        #list of buttons
        obj_list=[logo,label_1,label_2,storelist,label_3,adeia,label_4,ecoinfo,label_5,storedetails,confirm,goback]
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
        window.grid_columnconfigure(0, minsize=800)

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
app.maxsize(800, 500)
app.mainloop()
