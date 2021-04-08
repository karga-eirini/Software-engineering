from tkinter import *
import os
from PIL import ImageTk,Image



main_screen = Tk()
main_screen.title('Frienvi log in')
main_screen.geometry("450x450")
#app logo
logo= Canvas(main_screen, width = 190, height = 91)
img = ImageTk.PhotoImage(Image.open('frienvilogo.png'))
logo.create_image(10,10,anchor=NW, image=img)
#log in input,username,password
login_screen= Label(main_screen,text='Log in',font=('calibri', 20,'bold'))
message=Label(main_screen,text='Log in to access your acount',font=('calibri', 8),fg='grey')
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
    global password
    global password2
    username = StringVar()
    password = StringVar()
    password2 = StringVar()
    
    username_lable = Label(register_screen, text="Username")
    username_entry = Entry(register_screen, textvariable=username)
    password_lable = Label(register_screen, text="Password")
    password_entry = Entry(register_screen, textvariable=password, show='*')
    password_lable2 = Label(register_screen, text="Επαλήθευση Password")
    password_entry2 = Entry(register_screen, textvariable=password2, show='*')
   
    logo2.pack()
    Label(register_screen, text="Enter your acount details").pack(pady=(0,20))
    username_lable.pack()
    username_entry.pack()
    password_lable.pack()
    password_entry.pack(pady=(0,20))
    password_lable2.pack()
    password_entry2.pack(pady=(0,20))

    Button(register_screen, text="Register", width=10, height=1).pack()



#main log in screen
logo.pack(pady=(0,20))
login_screen.pack(pady=(0,20))
message.pack()
usertext.pack()
user.pack()
passwordtext.pack()
password.pack()
check.pack(pady=(20,0))
Button(text='Log in',width=16, height=1).pack()
Label(text="Dont't have any acounts?",font=('calibri', 8)).pack()
Button(text="Sign up", height="1", width="5", command=register).pack()

main_screen.mainloop()
