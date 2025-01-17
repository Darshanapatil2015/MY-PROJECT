from tkinter import *
from PIL import Image,ImageTk
import os
from stegano import lsb
from tkinter import filedialog,messagebox
win = Tk()
win.geometry('900x680')
win.config(bg='black')
#Buttonn function
def open_img():
    global open_file
    open_file=filedialog.askopenfilename(initialdir=os.getcwd(),
                                         title='Select File Type', filetypes=(('PNG file','*.png'),('JPG file','*.jpg'),('All file','*.txt')))
    img= Image.open(open_file)
    img= ImageTk.PhotoImage(img)
    lf1.configure(image=img)
    lf1.image=img


def hide():
    global hide_msg
    password=code.get()
    if password == '1234':
      msg = text1.get(1.0,END)
      hide_msg = lsb.hide(str(open_file),msg)
      messagebox.showinfo('Success','Your message is successfully hidden in a image,please save your image')

    elif password == '':
             messagebox.showerror('Error','Please Enter Secrete key')
    else:
       messagebox.showerror('Error','Wrong secrete key')
    code.set('')

def save():
    hide_msg.save('Secret file.png')
    messagebox.showinfo('Success','Successfully saved image')

def show():
    password = code.get()
    if password == '1234':        
      show_msg= lsb.reveal(open_file)
      text1.delete(1.0,END)
      text1.insert(END,show_msg)
    elif password == '': 
     messagebox.showerror('Error','Please enter secrete key')
    else:
        messagebox.showinfo('Error', 'Wrong secrete key')
#Logo
logo = PhotoImage(file='download.png',width=350,height=150)
Label(win, image=logo ,bd=0,bg='black').place(x=10,y=10)
#heading
Label(win,text='Steganography',font='impack 50 bold',bg='black',fg='red',).place(x=360,y=12)
#Frame 1
f1 = Frame(win,width=250,height=220 ,bd=5,bg='purple')
f1.place(x=100,y=200)
lf1 = Label(f1,bg='purple')
lf1.place(x=0,y=0,width=250,height=220)

#frame 2
f2 = Frame(win,width=320,height=220,bd=5,bg='white')
f2.place(x=500,y=200)
text1= Text(f2,font='arial 15 bold',wrap=WORD)
text1.place(x=0,y=0,width=320, height=200)

#Label for secrete key
Label(win,text='Enter Secrete key',font='10',bg='black',fg='yellow').place(x=340,y=450)

#Entry bigest for secret key
code = StringVar()

e = Entry(win,textvariable=code,bd=2,font='impact 10 bold',show='*')
e.place(x=350,y=500)


#Buttons
open_button= Button(win,text='Open Image',bg='blue',fg='white',font='arial 12 bold',cursor='hand2', command=open_img)
open_button.place(x=100,y=600)

save_button= Button(win,text='Save Data',bg='green',fg='white',font='arial 12 bold',cursor='hand2',command=save)
save_button.place(x=250,y=600)

hide_button= Button(win,text='Hide Data',bg='red',fg='white',font='arial 12 bold',cursor='hand2',command=hide)
hide_button.place(x=550,y=600)

show_button= Button(win,text='Show Data',bg='orange',fg='white',font='arial 12 bold',cursor='hand2',command=show)
show_button.place(x=700,y=600)
mainloop()
