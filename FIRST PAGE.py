from tkinter import *
from PIL import Image,ImageTk
def time():
    from time import strftime
    string = strftime('%H:%M:%S %p')
    lbl.config(text=string)
    lbl.after(1000, time)
def date():
    from datetime import datetime
    now = datetime.now()
    timestamp = datetime.timestamp(now)
    date_time = datetime.fromtimestamp(timestamp)
    d = date_time.strftime("%d %B, %Y")
    lbl2.config(text=d.upper())
def func():
    pass
root=Tk()
root.title("SMART INDIA HACKATHON")
root.geometry("1350x800")
root.minsize(1350,800)
root.iconbitmap("q.ico.ico")
img=Image.open("maxx2.jpeg")
img=img.resize((1370,700))
photo=ImageTk.PhotoImage(img)
canvas=Canvas(root,width=1400,height=700)
canvas.create_image(0,0,image=photo,anchor="nw")
canvas.pack()
Button(root,text="ENTER Ne-VA PORTAL ",command=func,fg="blue",font="default 20 bold",activebackground="orange",activeforeground="black",relief=SUNKEN,borderwidth=15,bg="white").place(x=530,y=560)
lbl2 = Label(root, font=('calibri', 25, 'bold'),foreground='black',background="white")
lbl2.place(x=1100,y=550)
date()
lbl = Label(root, font=('calibri', 10, 'bold'),background='white',foreground='black')
lbl.place(x=1190,y=590)
time()
root.mainloop()