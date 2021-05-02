from tkinter import *
root =Tk()
root.geometry("100x100")
Button(root, text="A").pack(side=LEFT, expand="Yes", fill=Y)
Button(root, text="B").pack(side=TOP, expand="Yes", fill=BOTH)
Button(root, text="C").pack(side=RIGHT, expand="Yes", fill=NONE)
Button(root, text="D").pack(side=LEFT, expand="No", fill=Y)
Button(root, text="E").pack(side=TOP, expand="Yes", fill=BOTH)
Button(root, text="F").pack(side=RIGHT, expand="No", fill=NONE)

root.mainloop()