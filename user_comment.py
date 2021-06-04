from tkinter import *
import os
from PIL import ImageTk,Image
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox

def confirm_message():
    MsgBox=tk.messagebox.showinfo("Confirm","Επιτυχία υποβολής σχολίου!") 
    if MsgBox == 'ok':
        sys.exit()

platform= Tk()
platform.title('Frienvi')
platform.geometry("450x450")


#app logo
logo= Canvas(platform, width = 290, height = 120)
img = ImageTk.PhotoImage(Image.open('frienvilogo.png'))
logo.create_image(10,10,anchor=NW, image=img)

#sxolio
platform_screen= Label(platform,text='Πλατφόρμα επικοινωνίας',font=('arial', 15,'bold'))
message=Label(platform,text='Προσθέστε κάποιο σχόλιο',font=('calibri', 10),fg='grey')
usertext = Label(platform, text='Σχόλιο')
user = Text(platform,width="50", height="5")


check=Checkbutton(platform,text='Είστε σίγουρος;')

logo.pack(pady=(0,20 ))
platform_screen.pack(pady=(0,20))
message.pack()
usertext.pack()
user.pack(pady=(0,20))
check.pack(pady=(20,0))
Button(text='Υποβολή',width=16, height=1,bg='green',fg='white',command=confirm_message).pack()


platform.mainloop()
