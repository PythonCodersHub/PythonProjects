from tkinter import *
root = Tk()
x = Button(root, text="button1", fg="green", bg ="blue")
y = Button(root, text="button2", fg="orange", bg ="green")
z = Button(root, text="button3", fg="yellow", bg ="red")

x.grid(padx=20,pady=50,ipadx=5,ipady=20)
y.grid(padx=20,pady=100,ipadx=5,ipady=40)
z.grid(padx=20,pady=150,ipadx=5,ipady=60)
root.mainloop()