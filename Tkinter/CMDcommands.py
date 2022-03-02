from tkinter import *
import os
app = Tk()
app.title("CMD Commands Generator")
app.geometry("500x500")
app.resizable()
label1 = Label(app, text="CMD Commands Generator", font=("David",20))
label1.pack()
label2 = Label(app, text="Command", font=("David",12))
label2.place(x=40, y=30)
command = StringVar()
entry1 = Entry(app,width=25, textvariable=command)
entry1.place(x=140, y=30)
entry1.focus()
def clickme():
    text.delete("1.0","end")
    if command.get()=="whoami":
        new_command = "whoami"
        new_command = os.popen(new_command).read()
        text.insert(1.0, new_command)
    if command.get()=="ipconfig":
        new_command = "ipconfig"
        new_command = os.popen(new_command).read()
        text.insert(1.0, new_command)
    if command.get()=="ping 127.0.0.1":
        new_command = "ping 127.0.0.1"
        new_command = os.popen(new_command).read()
        text.insert(1.0, new_command)
label_idle = Label(app,font=("David",40))
label_idle.pack()
btn1 = Button(app, text="Execute!",command=clickme)
btn1.place(x=300, y=30)
text = Text(app, width="50",height="20")
text.pack()
app.mainloop()