from tkinter import *  # It is library used for making GUI application & software
from tkinter import ttk  # for stylying purposes
from PIL import Image, ImageTk  # For opening and displaying image files
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np


class Train:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1920x1080+0+0")
        self.root.title = ("Face Recognition System")

        title_lbl = Label(self.root, text="PHOTO SAMPLE TRAINING", font=(
            "20th Century Font", 32, "bold"), bg="white", fg="green")
        title_lbl.place(x=600, y=50, width=1530, height=120)

        # ========== TOP IMAGE ====================
        img_top = Image.open(
            r"C:\Users\KIIT01\Face Recognition System\train data\Group69.png")
        img_top = img_top.resize((1920, 325), Image.BILINEAR)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0, y=0, width=1920, height=200)

        b1_1 = Button(self.root, text="Train Data", cursor="hand2", font=(
            "times new roman", 15, "bold"), bg="darkblue", fg="white")
        b1_1.place(x=1100, y=300, width=200, height=40)

        # =============== Bottom Image ==============
        img_bottom = Image.open(
            r"C:\Users\KIIT01\Face Recognition System\train data\Group 71.png")
        img_bottom = img_bottom.resize((1200, 600), Image.BILINEAR)
        self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)

        f_lbl = Label(self.root, image=self.photoimg_bottom)
        f_lbl.place(x=100, y=220, width=1300, height=600)

        # =========== Button =====================
        b1_1 = Button(self.root, text="TRAIN DATA", command=self.train_classifier, cursor="hand2", font=(
            "times new roman", 18, "bold"), bg="green", fg="white")
        b1_1.place(x=630, y=700, width=300, height=60)

        # Back
        # img7 = Image.open(
        #     r"C:\Users\KIIT01\Face Recognition System\images\help.jpg")
        # img7 = img7.resize((200, 200), Image.BILINEAR)
        # self.photoimg7 = ImageTk.PhotoImage(img7)

        # b1 = Button(bg_img, image=self.photoimg7, cursor="hand2")
        # b1.place(x=1100, y=100, width=200, height=200)

        # b1_1 = Button(bg_img, text="Help Desk", cursor="hand2", font=(
        #     "times new roman", 15, "bold"), bg="darkblue", fg="white")
        # b1_1.place(x=1100, y=300, width=200, height=40)

    def train_classifier(self):
        data_dir = ("data")
        path = [os.path.join(data_dir, file)
                for file in os.listdir(data_dir)]

        faces = []
        ids = []

        for image in path:
            img = Image.open(image).convert('L')  # Gray scale Image
            imageNp = np.array(img, dtype='uint8')
            id = int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training", imageNp)
            cv2.waitKey(1) == 13
        ids = np.array(ids)

        # ================= Train the Classifier & Save the data ==============
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces, ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result", "Training datasets completed")


if __name__ == "__main__":
    root = Tk()
    obj = Train(root)
    root.mainloop()
