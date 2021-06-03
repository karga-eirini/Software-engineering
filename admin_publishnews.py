import tkinter as tk 
from PIL import ImageTk,Image
from tkinter import messagebox
from tkcalendar import*
from tkinter import filedialog as fd


#to open files 
def callback():
    name= fd.askopenfilename() 
    print(name)

errmsg = 'Error!'


#confirmation messagebox for updating an article
def submit_article():
    MsgBox=tk.messagebox.askquestion("Confirm","Είστε σίγουροι;")
    if MsgBox == 'no':
         exit
    else:
        tk.messagebox.showinfo('Return','Επιτυχής δημοσίευση')       

# admin log in page 
class admin_login(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        #app logo
        load = Image.open('frienvilogo.png')
        render = ImageTk.PhotoImage(load)
        logo = Label(self, image=render)
        logo.image = render

        

        #admin choices
        label_1=Label(self, text="Ενημέρωση καταστημάτων(Προσθήκη ή Κατάργηση)",font=('ariel', 14,'bold'))
        label_2=Label(self, text="Ενημέρωση Σελίδας νέων",font=('ariel', 14,'bold'))
        label_3=Label(self, text="Διαφήμιση μέσω admob",font=('ariel', 14,'bold'))
        label_4=Label(self, text="Quiz της ημέρας",font=('ariel', 14,'bold'))

        button_1=tk.Button(self, text='Update',width=40, height=2,bg='black',fg='white')
        button_2=tk.Button(self, text='Update',width=40, height=2,bg='black',fg='white',command=lambda: controller.show_frame(Newsfeed))
        button_3=tk.Button(self, text='Update',width=40, height=2,bg='black',fg='white')
        button_4=tk.Button(self, text='Update',width=40, height=2,bg='black',fg='white')

        logo.grid(row=0,column=0)
        label_1.grid(row=1,column=0)
        button_1.grid(row=2,column=0)
        label_2.grid(row=3,column=0)
        button_2.grid(row=4,column=0)
        label_3.grid(row=5,column=0)
        button_3.grid(row=6,column=0)
        label_4.grid(row=7,column=0)
        button_4.grid(row=8,column=0)

        
        obj_list=[logo,label_1,button_1,label_2,button_2,label_3,button_3,label_4,button_4]
        #loop thru the list and config
        row_num=0
        for button in obj_list:
            Grid.rowconfigure(self,row_num,weight=1)
            row_num+=1

        Grid.columnconfigure(self,0,weight=1)

        

#update newsfeed page
class Newsfeed(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        #app logo
        load = Image.open('frienvilogo.png')
        render = ImageTk.PhotoImage(load)
        logo = Label(self, image=render)
        logo.image = render

        global article
        article=StringVar()

        
        i=StringVar()
        R1=tk.Radiobutton(self,text='Ενημερωτικό άρθρο',value=1,variable=i)
        R2=tk.Radiobutton(self,text='Άρθρο για το περιβάλλον',value=2,variable=i)
        R3=tk.Radiobutton(self,text='Άρθρο για τα νέα της εφαρμογής',value=3,variable=i)

        '''
        if (i.get() ==1):
           print("you picked option1")
        '''
        
        label_1=Label(self, text="Επίλεξε το είδος του άρθρου:",font=('ariel', 20,'bold'))
        label_2=Label(self, text="Προσθήκη άρθρου:",font=('ariel', 20,'bold'))

        article=tk.Button(self,text='Click to Open File',command=callback)
        confirm=tk.Button(self,text='Επιβεβαίωση',width=20, height=2,bg='black',fg='white',command=submit_article)
        goback=tk.Button(self,text='Επιστροφή',width=20, height=1,bg='black',fg='white',command=lambda: controller.show_frame(admin_login))
        schedule=tk.Button(self,text='Προγραμματισμός',width=20, height=2,bg='black',fg='white',command=lambda: controller.show_frame(Schedule_update))
        
        logo.grid(row=0,column=0)
        label_1.grid(row=1,column=0)
        R1.grid(row=2,column=0)
        R2.grid(row=3,column=0)
        R3.grid(row=4,column=0)
        label_2.grid(row=5,column=0)
        article.grid(row=5,column=1)
        goback.grid(row=6,column=0)
        confirm.grid(row=6,column=1)
        schedule.grid(row=7,column=1)

        
        obj_list=[logo,label_1,R1,R2,R3,label_2,article,goback,confirm,schedule]
        #loop thru the list and config
        row_num=0
        for button in obj_list:
            Grid.rowconfigure(self,row_num,weight=1)
            row_num+=1

        Grid.columnconfigure(self,0,weight=1)

        

#schedule update for article page
class Schedule_update(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        

        load = Image.open('frienvilogo.png')
        render = ImageTk.PhotoImage(load)
        logo = Label(self, image=render)
        logo.image = render

        label_1=Label(self, text="Επίλεξε ημερομηνία δημοσίευσης",font=('ariel', 20,'bold'))

        cal=Calendar(self,selectmode='day',year=2021,month=6)

        #messagebox to confirm schedule date
        def submit_date():
        
            if cal.get_date() == '':
                tk.messagebox.showinfo('Return','Δεν έχετε επιλέξει ημερομηνία για δημοσίευση. Προσπαθήστε ξανά!')
            else:
                MsgBox=tk.messagebox.askquestion("Confirm","Είστε σίγουροι;")
                if MsgBox == 'no':
                    exit
                else:
                    tk.messagebox.showinfo('Return','Το άρθρο έχει προγραμματιστεί να δημοσιευθεί '+cal.get_date())
                

        confirm=tk.Button(self,text='Επιβεβαίωση',width=20, height=1,bg='black',fg='white',command=submit_date)
        goback=tk.Button(self,text='Επιστροφή',width=20, height=1,bg='black',fg='white',command=lambda: controller.show_frame(Newsfeed))
        

      
        logo.grid(row=0,column=0)
        label_1.grid(row=1,column=0)
        cal.grid(row=2,column=0)
        goback.grid(row=3,column=0)
        confirm.grid(row=3,column=1)

        #list of buttons
        obj_list=[logo,label_1,cal,goback,confirm]
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
        for F in (admin_login, Newsfeed,Schedule_update):
            frame = F(window, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(admin_login)

    def show_frame(self, page):
        frame = self.frames[page]
        frame.tkraise()
        self.title("admin page")
        


app = Application()
app.maxsize(800, 500)
app.mainloop()
