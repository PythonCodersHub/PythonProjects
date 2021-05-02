from tkinter import *
root = Tk()
root.geometry("300x300")
mylabel = Label(root, text ="Welcome to GUI")
mybutton = Button(root, text ="Click Dell")
mybutton.pack()
mylabel.pack()
root.mainloop()