import random
import string
from tkinter import *
app = Tk()
app.title("Password Generator")
app.geometry("500x500")
app.resizable()
label1 = Label(app, text="Password Generator", font=("David",20))
label1.pack()
label2 = Label(app, text="Please enter password's length", font=("David",12))
label2.place(x=40, y=30)
length = StringVar()
entry1 = Entry(app,width=7, textvariable=length)
entry1.place(x=250, y=30)
entry1.focus()
label_idle = Label(app,font=("David",40))
label_idle.pack()
text = Text(app, width="50",height="15")
def Pass_Generator(): #יוצר סיסמאות
    text.delete("1.0", "end")
    len=int(length.get())
    if len>4:
        char = (string.ascii_letters).replace(" ","").lower()
        password = ''.join(random.choice(char) for _ in range(len-2))
        first = random.choice(string.ascii_letters.upper())
        sign = random.choice(string.punctuation)
        text.insert(1.0, f"Random password is: {first+password+sign}")
    else:
        text.insert(1.0,"Password would be too short")
    text.pack()
btn1 = Button(app, text="Generate!",command=Pass_Generator)
btn1.place(x=320, y=30)
app.mainloop()