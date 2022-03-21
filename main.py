from tkinter import *

window = Tk()

window.title("Hello World!")
window.geometry('350x200')

label = Label(window, text="Hi", font=("Arial Bold", 30))
label.grid(column=0, row=0)

def start():
    label.configure(text="Start typing!")

text = Entry(window, width=10)
text.grid(column=1, row=0)
text.focus()

btn = Button(window, text="Start!", command=start)
btn.grid(column=2, row=0)

window.mainloop()