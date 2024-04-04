# Python Imaging Library (expansion of PIL) is the de facto image processing package for Python language
from tkinter import *  # It is library used for making GUI application & software
from tkinter import ttk, Button, Toplevel  # for stylying purposes
from PIL import Image, ImageTk  # For opening and displaying image files
# Importing from student .py file which contains class 'Student'
import os
from student import Student
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance
from developer import Developer
from help import Help
import concurrent.futures


class Face_Recognition_System:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1920x1080+0+0")
        self.root.title("Face Recognition System")

        # Top img
        img = Image.open(
            r"C:\Users\KIIT01\Face Recognition System\images\img11.jpg")
        img = img.resize((1700, 130), Image.BILINEAR)
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=0, width=1700, height=130)

        # bg img
        img3 = Image.open(
            r"C:\Users\KIIT01\Face Recognition System\images\bg.jpg")
        img3 = img3.resize((1530, 710), Image.BILINEAR)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=130, width=1530, height=710)

        title_lbl = Label(bg_img, text="CHECKING SYSTEM COMPABILITY INSIGHTS", font=(
            "20th Century Font", 30), bg="white", fg="darkgreen")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        # Student Details
        img4 = Image.open( 
            r"C:\Users\KIIT01\Face Recognition System\images\stu.png")
        img4 = img4.resize((200, 200), Image.BILINEAR)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        b1 = Button(bg_img, image=self.photoimg4,
                    command=self.student_details, cursor="hand2")
        b1.place(x=200, y=100, width=200, height=200)

        b1_1 = Button(bg_img, text="Student Details", command=self.student_details,
                      cursor="hand2", font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=200, y=300, width=200, height=40)

        # ============= Attendance need to Complete Priority==============
        img5 = Image.open(
            r"C:\Users\KIIT01\Face Recognition System\images\Illustration.png")
        img5 = img5.resize((200, 200), Image.BILINEAR)
        self.photoimg5 = ImageTk.PhotoImage(img5)

        b1 = Button(bg_img, image=self.photoimg5,
                    cursor="hand2", command=self.attendance_data)
        b1.place(x=500, y=100, width=200, height=200)

        b1_1 = Button(bg_img, text="Student Database", cursor="hand2", command=self.attendance_data,  font=(
            "times new roman", 15, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=500, y=300, width=200, height=40)

        # Face Detector
        img6 = Image.open(
            r"C:\Users\KIIT01\Face Recognition System\images\det.jpg")
        img6 = img6.resize((200, 200), Image.BILINEAR)
        self.photoimg6 = ImageTk.PhotoImage(img6)

        b1 = Button(bg_img, image=self.photoimg6,
                    cursor="hand2", command=self.face_data)
        b1.place(x=800, y=100, width=200, height=200)

        b1_1 = Button(bg_img, text="Face Detector", cursor="hand2", command=self.face_data, font=(
            "times new roman", 15, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=800, y=300, width=200, height=40)

        # Help Desk
        img7 = Image.open(
            r"C:\Users\KIIT01\Face Recognition System\images\help.jpg")
        img7 = img7.resize((200, 200), Image.BILINEAR)
        self.photoimg7 = ImageTk.PhotoImage(img7)

        b1 = Button(bg_img, image=self.photoimg7,
                    cursor="hand2", command=self.help_data)
        b1.place(x=1100, y=100, width=200, height=200)

        b1_1 = Button(bg_img, text="Help Desk", cursor="hand2", command=self.help_data, font=(
            "times new roman", 15, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=1100, y=300, width=200, height=40)

        # Train data
        img8 = Image.open(
            r"C:\Users\KIIT01\Face Recognition System\images\train.jpg")
        img8 = img8.resize((200, 200), Image.BILINEAR)
        self.photoimg8 = ImageTk.PhotoImage(img8)

        b1 = Button(bg_img, image=self.photoimg8,
                    cursor="hand2", command=self.train_data)
        b1.place(x=200, y=370, width=200, height=200)

        b1_1 = Button(bg_img, text="Train Data", cursor="hand2",  command=self.train_data, font=(
            "times new roman", 15, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=200, y=570, width=200, height=40)

        # Photos
        img9 = Image.open(
            r"C:\Users\KIIT01\Face Recognition System\images\phot.jpg")
        img9 = img9.resize((200, 200), Image.BILINEAR)
        self.photoimg9 = ImageTk.PhotoImage(img9)

        b1 = Button(bg_img, image=self.photoimg9,
                    cursor="hand2", command=self.open_img)
        b1.place(x=500, y=370, width=200, height=200)

        b1_1 = Button(bg_img, text="Photos", cursor="hand2", command=self.open_img, font=(
            "times new roman", 15, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=500, y=570, width=200, height=40)

        # Developer
        img10 = Image.open(
            r"C:\Users\KIIT01\Face Recognition System\images\dev.jpg")
        img10 = img10.resize((200, 200), Image.BILINEAR)
        self.photoimg10 = ImageTk.PhotoImage(img10)

        b1 = Button(bg_img, image=self.photoimg10,
                    cursor="hand2", command=self.developer_data)
        b1.place(x=800, y=370, width=200, height=200)

        b1_1 = Button(bg_img, text="Developer", cursor="hand2", command=self.developer_data, font=(
            "times new roman", 15, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=800, y=570, width=200, height=40)

        # Exit
        img11 = Image.open(
            r"C:\Users\KIIT01\Face Recognition System\images\exit.jpg")
        img11 = img11.resize((200, 200), Image.BILINEAR)
        self.photoimg11 = ImageTk.PhotoImage(img11)

        b1 = Button(bg_img, image=self.photoimg11, cursor="hand2")
        b1.place(x=1100, y=370, width=200, height=200)

        b1_1 = Button(bg_img, text="Exit", cursor="hand2", font=(
            "times new roman", 15, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=1100, y=570, width=200, height=40)

    # ========== For Opening Photos Folder ==============

    def open_img(self):
        os.startfile("data")

    # =============== Function Buttons =============
    def student_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Student(self.new_window)

    # ============== Function Button for Train =============
    def train_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Train(self.new_window)

     # ============== Function for Face Recognition =============
    def face_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Face_Recognition(self.new_window)

    # ============== Function for Attendance System =============
    def attendance_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Attendance(self.new_window)

    # ============= Developers  Window ====================
    def developer_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Developer(self.new_window)

    # ================ Help Desk =========================
    def help_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Help(self.new_window)


if __name__ == "__main__":
    root = Tk()
    app = Face_Recognition_System(root)
    root.mainloop()
