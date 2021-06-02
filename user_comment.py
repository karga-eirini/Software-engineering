from tkinter import *
import os
from PIL import ImageTk,Image

global username

platforma= Tk()
platforma.title('Frienvi')
platforma.geometry("450x450")

#app logo
logo= Canvas(platforma, width = 290, height = 120)
img = ImageTk.PhotoImage(Image.open('frienvilogo.png'))
logo.create_image(10,10,anchor=NW, image=img)

#sxolio
platforma_screen= Label(platforma,text='Πλατφόρμα επικοινωνίας',font=('arial', 15,'bold'))
message=Label(platforma,text='Προσθέστε κάποιο σχόλιο',font=('calibri', 10),fg='grey')
usertext = Label(platforma, text='Σχόλιο')
user = Text(platforma,width="50", height="5")


check=Checkbutton(platforma,text='Είστε σίγουρος;')

def epityxia():
    global epityxia_screen
    epityxia_screen = Toplevel(platforma_screen)
    epityxia_screen.title("Frienvi")
    epityxia_screen.geometry("450x450")

    #second screen
    logo2 = Canvas(epityxia_screen, width = 290, height = 120)
    img2 = ImageTk.PhotoImage(Image.open('frienvilogo.png'))
    logo2.create_image(5,5,anchor=NW, image=img)

    logo2.pack(pady=(0,20))
    Label(epityxia_screen, text="Επιτυχία υποβολής!").pack(pady=(0,20))
    Label(epityxia_screen, text="Επιτυχής αποθήκευση σχολίου!").pack(pady=(0,20))



logo.pack(pady=(0,20 ))
platforma_screen.pack(pady=(0,20))
message.pack()
usertext.pack()
user.pack(pady=(0,20))
check.pack(pady=(20,0))
Button(text='Υποβολή',width=16, height=1,bg='green',fg='white',command=epityxia).pack()


platforma.mainloop()