from tkinter import *
from PIL import Image,ImageTk
def func():
    pass
root=Tk()
root.title("SMART INDIA HACKATHON")
root.geometry("1350x800")
root.minsize(1350,800)
root.iconbitmap("q.ico.ico")
img=Image.open("MM.jpg")
img=img.resize((1570,800))
photo=ImageTk.PhotoImage(img)
canvas=Canvas(root,width=1400,height=800)
canvas.create_image(0,0,image=photo,anchor="nw")
canvas.pack()
Button(root,text="<<BACK",command=func,font="comicsansms 10 bold").place(x=5,y=650)
Button(root,text="SCHOOL DETAILS",command=func,font="default 25 bold").place(x=540,y=273)
Button(root,text="MAINTENANCE REQUEST",command=func,font="default 25 bold").place(x=475,y=373)
Button(root,text="UPDATE",command=func,font="default 25 bold").place(x=620,y=473)
root.mainloop()