#creating-window
from tkinter import*
window = Tk()
window.geometry("600x600")
window.title("Drive (C)")
#creating widget
theLabel = Label(window, cursor="dot",text="Welcome to the python gui", fg="seagreen", bg="silver" ,font=("Arial", 16, "bold"))
theLabel.pack()
#Button
x=Button(window,text='button1', fg="blue", bg="skyblue")
y=Button(window,text='button2', fg="green", bg="seagreen")
z=Button(window,text='button1', fg="silver", bg="red")


window.mainloop()
#label widget
# theLabel = Label(window, cursor='dot', text="Introduction to py")