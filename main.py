import tkinter
from tkinter import *
from tkinter import messagebox
import subprocess
from PIL import Image, ImageTk
import pyqrcode

# UI
window = Tk()
window.geometry("450x300")
window.resizable(height=False, width=False)
window.title("QR Code Generator")

font = ["Arial", 14, "normal"]
label1 = Label(text="Enter URL Address:", font=font)
label1.place(x=20, y=20)

entry1 = Entry(width=30)
entry1.place(x=150, y=18)

frame = Frame(window, width=200, height=200, bd=1, relief=tkinter.SOLID)
frame.place(x=30, y=70)


# Fonksiyonlar
def generate():
    if len(entry1.get()) == 0:
        messagebox.showerror(title="Error!", message="Please enter a URL address.")
    else:
        # Eski QR kodunu temizle
        for widget in frame.winfo_children():
            widget.destroy()

        url_address = entry1.get()
        qr_code = pyqrcode.create(url_address)
        qr_code.svg('qrcode.svg', scale=7)
        svg_to_png("qrcode.svg", "qrcode.png")
        png_image = Image.open("qrcode.png")
        tk_image = ImageTk.PhotoImage(png_image)
        qr_label = Label(frame, image=tk_image)
        qr_label.image = tk_image  # Garbage collection'dan kaçınmak için referansı tut
        qr_label.pack()


def clear():
    # Eski QR kodunu temizle
    for widget in frame.winfo_children():
        widget.destroy()
    # Entry'yi temizle
    entry1.delete(0, 'end')


def svg_to_png(svg_file, png_file):
    subprocess.run(['rsvg-convert', '-f', 'png', '-o', png_file, svg_file])


# Butonlar
generatebutton = Button(text="Generate QR", font=font, width=8, height=2, command=generate)
generatebutton.place(x=270, y=68)

clearbutton = Button(text="Clear", font=font, width=8, height=2, command=clear)
clearbutton.place(x=270, y=118)

window.mainloop()
