from tkinter import *
import os
import tkinter as tk 
from PIL import ImageTk,Image
from tkinter import messagebox
import sys

# main store log in page
class main_menu(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        #app logo
        load = Image.open('frienvilogo.png')
        render = ImageTk.PhotoImage(load)
        logo = Label(self, image=render)
        logo.image = render
        self.configure(bg='lightgreen')

        logo.grid(row=0,column=0)


        #buttons
        search = Entry(self,width=30,borderwidth=1)
        search.insert(0, "Αναζήτηση")
        search.grid(row=1,column=0)

        news=tk.Button(self, text="Ειδήσεις",font=('bold'),height=3,width=30)
        news.grid(row=2,column=0)

        secondh=tk.Button(self, text="Μεταχειρισμένα",font=('bold'),heigh=3,width=30)
        secondh.grid(row=3,column=0)

        estiash=tk.Button(self, text="Χώροι εστίασης",font=('bold'),heigh=3,width=30)
        estiash.grid(row=4,column=0)

        food=tk.Button(self, text="Καταστήματα τροφίμων",font=('bold'),heigh=3,width=30)
        food.grid(row=5,column=0)

        platform=tk.Button(self, text="Πλατφόρμα επικοινωνίας",font=('bold'),heigh=3,width=30,command=lambda: controller.show_frame(comment))
        platform.grid(row=5,column=0)

        #list of buttons
        obj_list=[logo,search,news,secondh,estiash,food,platform]
        #loop thru the list and config
        row_num=0
        for button in obj_list:
            Grid.rowconfigure(self,row_num,weight=1)
            row_num+=1

        Grid.columnconfigure(self,0,weight=1)


def confirm_message():
    MsgBox=tk.messagebox.showinfo("Confirm","Επιτυχία υποβολής σχολίου!") 
    if MsgBox == 'ok':
        sys.exit()

class comment(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        #app logo
        load = Image.open('frienvilogo.png')
        render = ImageTk.PhotoImage(load)
        logo = Label(self, image=render)
        logo.image = render



        #sxolio
        self_screen= Label(self,text='Πλατφόρμα επικοινωνίας',font=('arial', 15,'bold'))
        message=Label(self,text='Προσθέστε κάποιο σχόλιο',font=('calibri', 10),fg='grey')
        usertext = Label(self, text='Σχόλιο')
        user = Text(self,width="50", height="5")


        check=Checkbutton(self,text='Είστε σίγουρος;')

        logo.pack(pady=(0,20))
        self_screen.pack(pady=(0,20))
        message.pack()
        usertext.pack()
        user.pack(pady=(0,20))
        check.pack(pady=(20,0))

        submit=tk.Button(self,text='Υποβολή',width=16, height=1,bg='green',fg='white',command=confirm_message).pack(pady=20)
        goback=tk.Button(self,text='Επιστροφή',width=16, height=1,bg='black',fg='white',command=lambda: controller.show_frame(main_menu)).pack()


        
class Application(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        # creating a window
        window = tk.Frame(self)
        window.pack()

        window.grid_rowconfigure(0, minsize=500)
        window.grid_columnconfigure(0, minsize=800)

        self.frames = {}
        for F in (main_menu,comment):
            frame = F(window, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(main_menu)

    def show_frame(self, page):
        frame = self.frames[page]
        frame.tkraise()
        self.title("admin page")
        


app = Application()
app.maxsize(800, 500)
app.mainloop()

