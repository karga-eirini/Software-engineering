from tkinter import *
import os


window = Tk()
window.title('Frienvi log in')
window.geometry("450x450")
#app logo
logo= Canvas(window, width = 190, height = 91)
img = PhotoImage(file = 'C:\\Users\\Ειρήνη Αναστασία\\Desktop\\python\\n.png')
logo.create_image(10,10,anchor=NW, image=img)
#log in input,username,password
login_screen= Label(window,text='Log in',font=('calibri', 20,'bold'))
message=Label(window,text='Log in to access your acount',font=('calibri', 8),fg='grey')
usertext = Label(window, text='Username')
passwordtext = Label(window, text='Password')
user = Entry(window, textvariable=StringVar())
password = Entry(window, show='*', textvariable=StringVar())
check=Checkbutton(window,text='Keep me signed in')


#register window
def register():
    global register_screen
    register_screen = Toplevel(window)
    register_screen.title("Frienvi Register")
    register_screen.geometry("450x450")
 
    global username
    global password
    global username_entry
    global password_entry
    username = StringVar()
    password = StringVar()
 
    logo= Canvas(register_screen, width = 190, height = 91)
    img = PhotoImage(file = 'C:\\Users\\Ειρήνη Αναστασία\\Desktop\\python\\n.png')
    logo.create_image(10,10,anchor=NW, image=img)
    username_lable = Label(register_screen, text="Username")
    username_entry = Entry(register_screen, textvariable=username)
    password_lable = Label(register_screen, text="Password")
    password_entry = Entry(register_screen, textvariable=password, show='*')
   
    logo.pack()
    Label(register_screen, text="Enter your acount details").pack()
    Label(register_screen, text="").pack()
    username_lable.pack()
    username_entry.pack()
    password_lable.pack()
    password_entry.pack()
    Label(register_screen, text="").pack()
    Button(register_screen, text="Register", width=10, height=1).pack()



#main log in window
logo.pack()
Label(text="").pack()
login_screen.pack()
Label(text="").pack()
message.pack()
usertext.pack()
user.pack()
passwordtext.pack()
password.pack()
check.pack()
Label(text="").pack()
Button(text='Log in', bg='black', fg='white',width=16, height=1).pack()
Label(text="Dont't have any acounts?",font=('calibri', 8)).pack()
Button(text="Sign up", height="1", width="5", command=register).pack()

window.mainloop()
