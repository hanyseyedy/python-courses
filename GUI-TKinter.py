from tkinter import *

root = Tk()

root.title("GUL Tkinter")

label = Label(root, text='this is test label')
label.place(x=50, y=50)

label2 = Label(root, text='this is second test label')
label2.place(x=50, y=70)

root.mainloop()