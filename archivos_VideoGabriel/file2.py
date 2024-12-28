from tkinter import *

ventana = Tk()
frame = Frame(ventana,width=600,height=600)
frame.pack()
texto = Label(text="HOLA MUNDO :D",fg="red", font=("Comic Sans MS",40))
texto.place(x=300,y=300)
gato = PhotoImage(file="gato.png")#PNG / GIF
Label(frame,image=gato).place(x=100,y=200)
ventana.mainloop()