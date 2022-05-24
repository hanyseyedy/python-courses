from tkinter import *

root = Tk()
root.title("GUL Tkinter")
root.geometry('400x300')
root.resizable(width=False, height=False)

my_name = StringVar()

def print_my_name():
    my_name.set("my name is hany")

label = Label(root, text="this is test label")
label.place(x=50, y=50)

label2 = Label(root, text='this is second test label')
label2.place(x=50, y=70)

btn = Button(root, text="show my name", command=lambda: print_my_name())
btn.place(x=50, y=100)

label3 = Label(root, textvariable=my_name)
label3.place(x=50, y=120)

root.mainloop()