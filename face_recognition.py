from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
from time import strftime
from datetime import datetime
import cv2
import os
import numpy as np


class Face_Recognition:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1920x1080+0+0")
        self.root.title("Face Recognition System")

        # ========== TOP IMAGE ====================
        img_top = Image.open(
            r"C:\Users\KIIT01\Face Recognition System\face_recognition\Group 72.png")
        img_top = img_top.resize((1920, 220), Image.BILINEAR)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0, y=0, width=1920, height=160)

        # b1_1 = Button(self.root, text="Train Data", cursor="hand2", font=(
        #     "times new roman", 15, "bold"), bg="darkblue", fg="white")
        # b1_1.place(x=1100, y=300, width=200, height=40)

        # =============== Bottom Image ==============
        img_bottom = Image.open(
            r"C:\Users\KIIT01\Face Recognition System\face_recognition\Group 73.png")
        img_bottom = img_bottom.resize((800, 620), Image.BILINEAR)
        self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)

        f_lbl = Label(self.root, image=self.photoimg_bottom)
        f_lbl.place(x=100, y=180, width=1300, height=650)

        # =========== Button =====================
        b1_1 = Button(self.root, text="FACE RECOGNITION", command=self.face_recog, cursor="hand2", font=(
            "times new roman", 18, "bold"), bg="green", fg="white")
        b1_1.place(x=590, y=700, width=300, height=60)

    # ============= Attendance =================
    def mark_attendance(self, i, r, n, d):
        with open("bijay.csv", "r+", newline="\n") as f:
            myDataList = f.readlines()
            name_list = []
            for line in myDataList:
                entry = line.split((","))
                name_list.append(entry[0])

            if ((i not in name_list) and (r not in name_list) and (n not in name_list) and (d not in name_list)):
                now = datetime.now()
                d1 = now.strftime("%d/%m/%Y")
                dtString = now.strftime("%H:%M:%S")
                f.writelines(f"\n{i},{r},{n},{d},{dtString},{d1},Present")

    # =========== Face Recognition Function ===============

    def face_recog(self):
        def draw_boundary(img, classifier, scaleFactor, minNeighbors, color, text, clf):
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(
                gray_image, scaleFactor, minNeighbors)

            coord = []

            for (x, y, w, h) in features:
                cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
                id, predict = clf.predict(gray_image[y:y+h, x:x+w])
                confidence = int((100*(1-predict/300)))

                conn = mysql.connector.connect(
                    host="localhost", username="root", password="Aang@123", database="face_recognizer")
                my_cursor = conn.cursor()

                my_cursor.execute(
                    f"SELECT Name FROM student WHERE Student_id={id}")
                n = my_cursor.fetchone()
                if n:
                    n = "+".join(n)

                my_cursor.execute(
                    f"SELECT Roll FROM student WHERE Student_id={id}")
                r = my_cursor.fetchone()
                if r:
                    r = "+".join(r)

                my_cursor.execute(
                    f"SELECT Dep FROM student WHERE Student_id={id}")
                d = my_cursor.fetchone()
                if d:
                    d = "+".join(d)

                my_cursor.execute(
                    f"SELECT Student_id FROM student WHERE Student_id={id}")
                i = my_cursor.fetchone()
                if i:
                    i = "+".join(i)

                # if confidence >= 45 and confidence <= 85:  # Adjust these thresholds as needed
                if confidence > 77:
                    cv2.putText(
                        img, f"ID:{i}", (x, y-75), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(
                        img, f"Roll:{r}", (x, y-55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    # cv2.putText(
                    #     # (B,G,R)_
                    #     img, f"Name:{n}", (x, y-30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 0, 255), 1.8)

                    cv2.putText(
                        # (B,G,R)_
                        img, f"Name:{n}", (x, y-30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(img, f"Department:{d}", (x, y-5),
                                cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    self.mark_attendance(i, r, n, d)

                else:
                    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 3)
                    cv2.putText(img, f"Unknown face", (x, y-5),
                                cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)

                    coord = [x, y, w, h]
            return coord

        def recognize(img, clf, faceCascade):
            coord = draw_boundary(img, faceCascade, 1.1,
                                  10, (255, 255, 255), "Face", clf)
            return img

        faceCascade = cv2.CascadeClassifier(
            "haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap = cv2.VideoCapture(0)

        while True:
            ret, img = video_cap.read()

            if not ret:
                break

            img = recognize(img, clf, faceCascade)
            cv2.imshow("Welcome To Face recognition", img)

            if cv2.waitKey(1) == 27:
                break

        video_cap.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition(root)
    root.mainloop()
