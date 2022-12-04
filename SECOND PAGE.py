from tkinter import *
from PIL import Image,ImageTk
def func():
    pass
root=Tk()
root.title("SMART INDIA HACKATHON")
root.geometry("1350x800")
root.minsize(1350,800)
root.iconbitmap("q.ico.ico")
root.wm_attributes("-transparentcolor", 'grey')
img=Image.open("rashtra.jpg")
img=img.resize((1370,700))
photo=ImageTk.PhotoImage(img)
canvas=Canvas(root,width=1400,height=700)
canvas.create_image(0,0,image=photo,anchor="nw")
canvas.pack()
Button(root,text="GOVERNMENT OFFICIALS",command=func,bg="white",fg="blue",font="courier 25 bold",activebackground="orange",activeforeground="black",relief=RAISED,borderwidth=15).place(x=205,y=510)
Button(root,text="SCHOOL ADMINISTRATION",command=func,bg="white",fg="blue",font="courier 25 bold",activebackground="orange",activeforeground="black",relief=RAISED,borderwidth=15).place(x=710,y=510)
Button(root,text="<<BACK",command=func,font="comicsansms 10 bold",bg="red",fg="white").place(x=10,y=660)
Button(root,text="STUDENT SERVICES",command=func,font="comicsansms 10 bold",fg="white",bg="red").place(x=1190,y=660)
lbl2 = Label(root, font=('calibri', 25, 'bold'),foreground='black',background="white")
lbl2.place(x=1100,y=550)
root.mainloop()