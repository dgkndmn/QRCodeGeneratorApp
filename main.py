import tkinter
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import io
import pyqrcode
#UI
window = Tk()
window.geometry("450x300")
window.resizable(height=False,width=False)

font = ["Ariel",14,"normal"]
label1 = Label(text="Enter URL Adress:",font=font)
label1.place(x=20,y=20)

entry1 = Entry(width=30)
entry1.place(x=150,y=18)

frame = Frame(window, width=200, height=200, bd=1, relief=tkinter.SOLID)
frame.place(x=30,y=70)





generatebutton = Button(text="Generate QR",font=font,width=8,height=2)
generatebutton.place(x=270,y=68)

clearbutton = Button(text="Clear",font=font,width=8,height=2)
clearbutton.place(x=270,y=118)


window.mainloop()