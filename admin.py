from tkinter import *
from PIL import ImageTk,Image
from tkinter import ttk
import tkinter as tk


root= Tk()
root.title('')
root.geometry('500x500')
root.configure(bg='lightblue')

frame = LabelFrame(root,text="",padx=5,pady=5) #frame ola ta widgets
frame.pack(padx=30,pady=30)
frame.configure(bg="lightgreen")

canvas= Canvas (frame, width=250, height=250)
canvas.pack()

#for admin pic
l1 = Label (frame, text ="Admin Name ")
l1.pack() 
#AdminPic=ImageTk.PhotoImage(Image.open('FreeUserPic.png'))
#canvas.create_image(20,20,anchor=NW,image=AdminPic).pack(side=LEFT)  

img = ImageTk.PhotoImage(Image.open("frienvilogo.png"))  # print logo
canvas.create_image(30, 30, anchor=NW, image=img)    

ttk.Label(frame, text="Categories").pack(padx=5,pady=5) #button action

def click():
    action.configure(text="Stores" + numberChosen.get()) #button Creation
    action.ttk.Button( frame ,text= 'Stores' , bg='white',height='1' ,command = click)
    action.pack(padx=11,pady=11) #combobox creation
number = tk.StringVar()
numberChosen = ttk.Combobox(frame,width = 12, textvariable= number) #adding numbers
numberChosen[ 'values'] = ("Eateries","Groceries","Secondhand")
numberChosen.pack(padx=11,pady=11)
numberChosen.current() # calling Main

ttk.Label(frame, text="User Comments").pack(padx=6,pady=6) #button action

def click():
    action.configure(text="" + numberChosen.get()) #button Creation
    action.ttk.Button( frame ,text= "" , command = click)
    action.pack(padx=11,pady=13) #cobox creation

number = tk.StringVar()
numberChosen = ttk.Combobox(frame,width = 12, textvariable= number) #adding numbers
numberChosen[ 'values'] = ("Users")
numberChosen.pack(padx=11,pady=11)
numberChosen.current() # calling Main



root.mainloop() 