from tkinter import *
import os
import tkinter as tk 
from PIL import ImageTk,Image


#Register menu
class Register_menu(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        #app logo
        load = Image.open('frienvilogo.png')
        render = ImageTk.PhotoImage(load)
        logo = Label(self, image=render)
        logo.image = render

        label_1=Label(self, text="Καλώς ήρθατε στη Frievni!",font=('ariel', 10))

        button_1=tk.Button(self, text='Δημιουργία Προφίλ',width=40, height=2,bg='black',fg='white', command=lambda: controller.show_frame(Create_a_profile))

        logo.grid(row=0,column=0)
        label_1.grid(row=1,column=0)
        button_1.grid(row=2,column=0)
        

        #list of buttons
        obj_list=[logo,label_1,button_1]
        #loop thru the list and config
        row_num=0
        for button in obj_list:
            Grid.rowconfigure(self,row_num,weight=1)
            row_num+=1

        Grid.columnconfigure(self,0,weight=1)

        

#Create a profile
class Create_a_profile(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        #app logo
        load = Image.open('frienvilogo.png')
        render = ImageTk.PhotoImage(load)
        logo = Label(self, image=render)
        logo.image = render
        
        global name
        global surname
        global email
        global password
        global conf_password
        name=StringVar()
        surname=StringVar()
        email=StringVar()
        password=StringVar()
        conf_password=StringVar()

        #labels
        label_1=Label(self, text="Δημιουργήστε το προφίλ σας στη Frienvi!",font=('ariel', 15,'bold'))
        label_2=Label(self, text="Όνομα",font=('ariel', 10))
        label_3=Label(self, text="Επώνυμο",font=('ariel', 10))
        label_4=Label(self, text="email",font=('ariel', 10))
        label_5=Label(self, text="Κωδικός",font=('ariel', 10))
        label_6=Label(self, text="Επιβεβαίωση κωδικού",font=('ariel',10))

        #entry boxes
        name=Entry(self,textvariable=name)
        surname=Entry(self,textvariable=surname)
        email=Entry(self,textvariable=email)
        password=Entry(self,textvariable=password)
        conf_password=Entry(self,textvariable=conf_password)

        #buttons
        confirm=tk.Button(self,text='Επιβεβαίωση',width=20, height=1,bg='black',fg='white',command=lambda: controller.show_frame(Info_view))
        goback=tk.Button(self,text='Επιστροφή',width=20, height=1,bg='black',fg='white',command=lambda: controller.show_frame(Register_menu))

        #the entry request screen
        logo.grid(row=0,column=0)
        label_1.grid(row=1,column=0)
        label_2.grid(row=2,column=0)
        name.grid(row=2,column=1,ipadx=30)
        label_3.grid(row=3,column=0)
        surname.grid(row=3,column=1,ipadx=30)
        label_4.grid(row=4,column=0)
        email.grid(row=4,column=1,ipadx=30)
        label_5.grid(row=5,column=0)
        password.grid(row=5,column=1,ipadx=30)
        label_6.grid(row=6,column=0)
        conf_password.grid(row=6,column=1,ipadx=30)
        confirm.grid(row=7,column=1)
        goback.grid(row=7,column=2)

        #list of buttons
        obj_list=[logo,label_1,label_2,name,label_3,surname,label_4,email,label_5,password,label_6,conf_password,confirm,goback]
        #loop thru the list and config
        row_num=0
        for button in obj_list:
            Grid.rowconfigure(self,row_num,weight=1)
            row_num+=1

        Grid.columnconfigure(self,0,weight=1)

        

#View profile info
class Info_view(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        

        #app logo
        load = Image.open('frienvilogo.png')
        render = ImageTk.PhotoImage(load)
        logo = Label(self, image=render)
        logo.image = render

        #global storelist
        #global adeia
        #global ecoinfo
        #global storedetails
        #storelist=StringVar()
        #adeia=StringVar()
        #ecoinfo=StringVar()
        #storedetails=StringVar()

        #labels
        label_1=Label(self, text="Τα στοιχεία σας ειναι τα παρακάτω",font=('ariel', 15,'bold'))
        label_2=Label(self, text="Όνομα",font=('ariel', 10))
        label_3=Label(self, text="Επώνυμο",font=('ariel', 10))
        label_4=Label(self, text="email",font=('ariel', 10))
        label_5=Label(self, text="Κωδικός",font=('ariel', 10))

        #entry boxes
        #storelist=Entry(self,textvariable=storelist)
        #adeia=Entry(self,textvariable=adeia)
        #ecoinfo=Entry(self,textvariable=ecoinfo)
        #storedetails=Entry(self,textvariable=storedetails)

        #buttons
        confirm=tk.Button(self,text='Επιβεβαίωση',width=20, height=1,bg='black',fg='white')
        goback=tk.Button(self,text='Επιστροφή',width=20, height=1,bg='black',fg='white',command=lambda: controller.show_frame(Create_a_profile))

        #the document list screen
        logo.grid(row=0,column=0)
        label_1.grid(row=1,column=0)
        label_2.grid(row=2,column=0)
        #storelist.grid(row=2,column=1)
        label_3.grid(row=3,column=0)
        #adeia.grid(row=3,column=1,ipadx=30,ipady=30)
        label_4.grid(row=4,column=0)
        #ecoinfo.grid(row=4,column=1,ipadx=30,ipady=30)
        label_5.grid(row=5,column=0)
        #storedetails.grid(row=5,column=1,ipadx=30,ipady=30)
        confirm.grid(row=6,column=0)
        goback.grid(row=6,column=1)

        #list of buttons
        obj_list=[logo,label_1,label_2,label_3,label_4,label_5,confirm,goback]
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
        for F in (Register_menu, Create_a_profile,Info_view):
            frame = F(window, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(Register_menu)

    def show_frame(self, page):
        frame = self.frames[page]
        frame.tkraise()
        self.title("Frienvi")
        


app = Application()
app.maxsize(800, 500)
app.mainloop()
