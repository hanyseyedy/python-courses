from tkinter import *

root = Tk()
root.title("GUL Tkinter")
root.geometry('400x300')
root.resizable(width=False, height=False)

my_name = StringVar()

def print_my_name():
    my_name.set(entry.get())

label = Label(root, text="this is test label")
label.place(x=50, y=50)

label2 = Label(root, text='this is second test label')
label2.place(x=50, y=70)

label3 = Label(root, text="enter yor text: ")
label3.place(x=50, y=100)

entry = Entry(root)
entry.place(x=50, y=120)

btn = Button(root, text="print input text", command=lambda: print_my_name())
btn.place(x=50, y=150)

label4 = Label(root, textvariable=my_name)
label4.place(x=50, y=180)

root.mainloop()