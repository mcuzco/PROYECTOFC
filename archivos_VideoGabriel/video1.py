from tkinter import *

obj1 = Tk()

obj1.resizable(1,1)

obj1.title("MI PRIMERA VENTANA")

obj1.iconbitmap("c++.ico")

obj1.geometry("400x650")

obj1.config(bg="yellow")

obj2 = Frame()

obj2.config(bg="white",width=300,height=300)

obj2.pack()

obj2.config(relief="raised",bd=35)

obj2.config(cursor="hand2")

obj1.mainloop()