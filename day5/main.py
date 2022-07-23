import imp
from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox

path = "/home/nabin/Music/python/day5/img.png"


def handleLogin():
    email = email_input.get()
    password = password_input.get()
    if email == 'creative201347@gmail.com' and password == "mypass":
        messagebox.showinfo("Successfully logged in!!!")
    else:
        messagebox.showerror("Opps, wrong credentials!!")


root = Tk()
root.title('Creative Nepal')
# root.iconbitmap("/home/nabin/Music/python/day5/img.png")


root.geometry('350x500')
root.configure(background='#0096DC')

img = Image.open(path)
resized_image = img.resize((100, 100))
img = ImageTk.PhotoImage(resized_image)

img_label = Label(root, image=img)
img_label.pack(pady=(10, 10))

text_label = Label(root, text="Flipkart", fg='white', bg='#0096DC')
text_label.pack()
text_label.config(font=('verdana', 24))


email_label = Label(root, text="Enter Email", fg='white', bg='#0096DC')
email_label.pack(pady=(20, 5))
email_label.config(font=('verdana', 13))
email_input = Entry(root, width=50)
email_input.pack(ipady=6, pady=(1, 15))


password_label = Label(root, text="Enter Password", fg='white', bg='#0096DC')
password_label.pack(pady=(20, 5))
password_label.config(font=('verdana', 13))
password_input = Entry(root, width=50)
password_input.pack(ipady=6, pady=(1, 15))


login_btn = Button(root, text="Login", bg='white',
                   fg='black', width=20, height=2, command=handleLogin)
login_btn.pack(pady=(10, 20))
login_btn.config(font=('verdana', 10))


root.mainloop()
