from tkinter import *

window = Tk()

window.title("Hello World!")
window.geometry('350x200')

label = Label(window, text="Hi", font=("Arial Bold", 30))
label.grid(column=0, row=0)

btn = Button(window, text="Start!")
btn.grid(column=1, row=0)

window.mainloop()