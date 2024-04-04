from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class Developer:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1920x1080+0+0")
        self.root.title("Face Recognition System")

   # Top img
        img = Image.open(
            r"C:\Users\KIIT01\Face Recognition System\images\Group 75.png")
        img = img.resize((1550, 200), Image.BILINEAR)
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=0, width=1550, height=200)

    # Title = developers Team
    # bg img
        img3 = Image.open(
            r"C:\Users\KIIT01\Face Recognition System\images\bg.jpg")
        img3 = img3.resize((1530, 710), Image.BILINEAR)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=190, width=1530, height=810)

        title_lbl = Label(bg_img, text="Developers Team", font=(
            "20th Century Font", 30, "bold"), bg="white", fg="darkgreen")
        title_lbl.place(x=0, y=0, width=1530, height=55)


if __name__ == "__main__":
    root = Tk()
    obj = Developer(root)
    root.mainloop()
