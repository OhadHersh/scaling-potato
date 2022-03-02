from tkinter import *
import os
app = Tk()
app.title("IP Communication Checker")
app.geometry("500x500")
app.resizable()
label1 = Label(app, text="IP Communication Checker", font=("David",18,"bold"))
label1.pack()
label2 = Label(app, text="Please enter the IP", font=("David",12,"bold"))
label2.place(x=40, y=30)
command = StringVar()
entry1 = Entry(app,width=20, textvariable = command, font=("David",12,"bold"))
entry1.pack()
entry1.focus()
text = Text(app, width="45", height="10", font=("David",12,"bold"))
def Ping_IP():
    text.delete("1.0","end")
    new_command = os.popen(f"ping {command.get()}").read()
    if "(0% loss)" in new_command and "Destination host unreachable" not in new_command:
        text.insert(1.0, f"The IP {command.get()} is up")
    elif "Destination host unreachable" in new_command and "(0% loss)" in new_command:
        text.insert(1.0, f"The IP {command.get()} is up but unreachable")
    else:
        text.insert(1.0, f"The IP {command.get()} is down")
    text.pack()
label_idle = Label(app,font=("David",30))
label_idle.pack()
btn1 = Button(app, text="Execute!",command=Ping_IP, font=("David",12,"bold"))
btn1.place(x=350, y=30)
app.mainloop()