from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
from time import strftime
from datetime import datetime
import cv2
import os
import csv
from tkinter import filedialog
import numpy as np

mydata = []


class Attendance:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1920x1080+0+0")
        self.root.title("Face Recognition System")

        # ======== Text variables ==========
        self.var_atten_id = StringVar()
        self.var_atten_roll = StringVar()
        self.var_atten_name = StringVar()
        self.var_atten_dep = StringVar()
        self.var_atten_time = StringVar()
        self.var_atten_date = StringVar()
        self.var_atten_attendance = StringVar()

        # Top img
        img = Image.open(
            r"C:\Users\KIIT01\Face Recognition System\images\img11.jpg")
        img = img.resize((1800, 200), Image.BILINEAR)
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=-10, width=1800, height=200)

        # bg img
        img3 = Image.open(
            r"C:\Users\KIIT01\Face Recognition System\images\bg.jpg")
        img3 = img3.resize((1530, 710), Image.BILINEAR)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=190, width=1530, height=710)

        title_lbl = Label(bg_img, text="STUDENT ATTENDANCE MANAGEMENT SYSTEM", font=(
            "20th Century Font", 30, "bold"), bg="white", fg="darkgreen")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        main_frame = Frame(bg_img, bd=2)
        main_frame.place(x=10, y=50, width=1500, height=650)

        # Left Side Label Frame
        Left_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE,
                                text="Student Attendance Details", font=("times new roman", 14, "bold"))
        Left_frame.place(x=0, y=0, width=750, height=580)

        img_left = Image.open(
            r"C:\Users\KIIT01\Face Recognition System\image\smart-attendance.jpg")
        img_left = img_left.resize((750, 280), Image.BILINEAR)
        self.photoimg_left = ImageTk.PhotoImage(img_left)

        f_lbl = Label(Left_frame, image=self.photoimg_left)
        f_lbl.place(x=5, y=0, width=736, height=220)

        # ============= Left Inside Frame =========================
        left_inside__frame = LabelFrame(
            Left_frame, bd=2, bg="white", relief=RIDGE, font=("times new roman", 14, "bold"))
        left_inside__frame.place(x=6, y=224, width=738, height=324)

        # Student ID
        studentId_label = Label(left_inside__frame, text="StudentId:", font=(
            "times new roman", 13, "bold"), bg="white")
        studentId_label.grid(row=0, column=0, padx=10, pady=10, sticky=W)

        studentID_entry = ttk.Entry(left_inside__frame, width=20, textvariable=self.var_atten_id, font=(
            "times new roman", 13, "bold"))
        studentID_entry.grid(row=0, column=1, padx=10, sticky=W)

        # Student name
        studenName_label = Label(left_inside__frame, text="Student Name:", font=(
            "times new roman", 13, "bold"), bg="white")
        studenName_label.grid(row=1, column=0, padx=10, sticky=W)

        studentName_entry = ttk.Entry(
            left_inside__frame, width=20, textvariable=self.var_atten_name, font=("times new roman", 13, "bold"))
        studentName_entry.grid(row=1, column=1, padx=10, sticky=W)

        # Roll Number
        roll_no_label = Label(left_inside__frame, text="Roll No:", font=(
            "times new roman", 13, "bold"), bg="white")
        roll_no_label.grid(row=0, column=2, padx=10, sticky=W)

        roll_no_entry = ttk.Entry(left_inside__frame,   width=20, textvariable=self.var_atten_roll, font=(
            "times new roman", 13, "bold"))
        roll_no_entry.grid(row=0, column=3, padx=10, sticky=W)

        # Department
        dep_label = Label(left_inside__frame, text="Department:", font=(
            "times new roman", 13, "bold"), bg="white")
        dep_label.grid(row=1, column=2, padx=10, sticky=W)

        dep_entry = ttk.Entry(left_inside__frame,  width=20, textvariable=self.var_atten_dep, font=(
            "times new roman", 13, "bold"))
        dep_entry.grid(row=1, column=3, padx=10, sticky=W)

        # time
        timeLabel = Label(left_inside__frame, text="Time:", font=(
            "times new roman", 13, "bold"), bg="white")
        timeLabel.grid(row=2, column=0)

        atten_time = ttk.Entry(
            left_inside__frame,  width=20, textvariable=self.var_atten_time, font=(
                "times new roman", 13, "bold"))
        atten_time.grid(row=2, column=1, pady=8)

        # Date
        dateLabel = Label(left_inside__frame, text="Date:", font=(
            "times new roman", 13, "bold"), bg="white")
        dateLabel.grid(row=2, column=2)

        atten_date = ttk.Entry(
            left_inside__frame,  width=20, textvariable=self.var_atten_date, font=(
                "times new roman", 13, "bold"))
        atten_date.grid(row=2, column=3, pady=8)

        # Attendance
        attendance_label = Label(
            left_inside__frame, text="Attendance Status", bg="white", font="comicsansns 11 bold")
        attendance_label.grid(row=3, column=0)

        atten_status = ttk.Combobox(
            left_inside__frame, width=20, textvariable=self.var_atten_attendance, font="comicsansns 11 bold", state="readonly")
        # Note the lowercase "values"
        atten_status["values"] = ("Status", "Present", "Absent")
        atten_status.grid(row=3, column=1, pady=8)
        atten_status.current(0)
        # ============ Main button Frame =============
        btn_frame = Frame(left_inside__frame,
                          bd=0, relief=RIDGE, bg="white")
        btn_frame.place(x=0, y=230, width=735, height=100)

        # Import button
        import_btn = Button(btn_frame, text="Import csv", command=self.importCsv, width=30, font=(
            "times new roman", 16, "bold"), bg="blue", fg="white")
        import_btn.grid(row=0, column=0)

        # Export button
        export_btn = Button(btn_frame, text="Export csv", command=self.exportCsv, width=30, font=(
            "times new roman", 16, "bold"), bg="blue", fg="white")
        export_btn.grid(row=0, column=1)

        # Update button
        import_btn = Button(btn_frame, text="Update", command=self.update_data,  width=30, font=(
            "times new roman", 16, "bold"), bg="blue", fg="white")
        import_btn.grid(row=1, column=0)

        # reset button
        reset_btn = Button(btn_frame, text="Reset", command=self.reset_data,  width=30, font=(
            "times new roman", 16, "bold"), bg="blue", fg="white")
        reset_btn.grid(row=1, column=1)

        # Right Side Label Frame
        Right_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE,
                                 text="Attendance Details", font=("times new roman", 14, "bold"))
        Right_frame.place(x=752, y=0, width=745, height=580)

        # Frame Inside Right Table
        table_frame = Frame(Right_frame,
                            bd=2, relief=RIDGE, bg="white")
        table_frame.place(x=10, y=5, width=720, height=535)

        # ============= Scroll Bar =================
        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.AttendanceReportTable = ttk.Treeview(table_frame, column=(
            "id", "roll", "name", "department", "time", "date", "attendance"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)

        # Column
        self.AttendanceReportTable.heading("id", text="Student Id")
        self.AttendanceReportTable.heading("roll", text="Roll")
        self.AttendanceReportTable.heading("name", text="Name")
        self.AttendanceReportTable.heading("department", text="Department")
        self.AttendanceReportTable.heading("time", text="Time")
        self.AttendanceReportTable.heading("date", text="Date")
        self.AttendanceReportTable.heading("attendance", text="Attendance")

        # For removing Table Gap
        self.AttendanceReportTable["show"] = "headings"

        # Width Set of Attributes
        self.AttendanceReportTable.column("id", width=100)
        self.AttendanceReportTable.column("roll", width=100)
        self.AttendanceReportTable.column("name", width=100)
        self.AttendanceReportTable.column("department", width=100)
        self.AttendanceReportTable.column("time", width=100)
        self.AttendanceReportTable.column("date", width=100)
        self.AttendanceReportTable.column("attendance", width=100)

        self.AttendanceReportTable.pack(fill=BOTH, expand=TRUE)

        # Binding Table
        self.AttendanceReportTable.bind("<ButtonRelease>", self.get_cursor)

    # =============== Fetch Data ============================
    def fetchData(self, rows):
        self.AttendanceReportTable.delete(
            *self.AttendanceReportTable.get_children())
        for i in rows:
            self.AttendanceReportTable.insert("", END, values=i)

    # ===============Import CSV ===============================
    def importCsv(self):
        global mydata
        mydata.clear()
        fln = filedialog.askopenfilename(initialdir=os.getcwd(), title="Open csv", filetypes=(
            # show an "Open" dialog box that
            ("CSV File", "*.csv"), ("All File", "*.*")), parent=self.root)
        with open(fln) as myfile:
            csvread = csv.reader(myfile, delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchData(mydata)

    # ===============Export CSV ===============================
    def exportCsv(self):
        try:
            if len(mydata) < 1:
                messagebox.showerror(
                    "No Data", "No Data found to export", parent=self.root)
                return False
            fln = filedialog.asksaveasfilename(initialdir=os.getcwd(), title="Open csv", filetypes=(
                # show an "Open" dialog box that
                ("CSV File", "*.csv"), ("All File", "*.*")), parent=self.root)
            with open(fln, "w", newline="") as myfile:
                exp_write = csv.writer(myfile, delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo(
                    "Data Export", "Your data exported to " + os.path.basename(fln) + " successfully ")
        except Exception as es:
            messagebox.showerror("Error", f"Due To :{
                str(es)}", parent=self.root)

    # ===========Function to Show Data in Entry Fill ===============
    def get_cursor(self, event=""):
        cursor_row = self.AttendanceReportTable.focus()
        content = self.AttendanceReportTable.item(cursor_row)
        rows = content['values']
        self.var_atten_id.set(rows[0])
        self.var_atten_roll.set(rows[1])
        self.var_atten_name.set(rows[2])
        self.var_atten_dep.set(rows[3])
        self.var_atten_time.set(rows[4])
        self.var_atten_date.set(rows[5])
        self.var_atten_attendance.set(rows[6])

    # =================== Update =================
    def update_data(self):
        # Get the selected row
        cursor_row = self.AttendanceReportTable.focus()

        # Check if a row is selected
        if not cursor_row:
            messagebox.showerror(
                "Error", "Please select a row to update", parent=self.root)
            return

        # Get the content of the selected row
        content = self.AttendanceReportTable.item(cursor_row)

        # Get the index of the selected row
        index = self.AttendanceReportTable.index(cursor_row)

        # Update the data associated with the selected row
        content['values'] = (
            self.var_atten_id.get(),
            self.var_atten_roll.get(),
            self.var_atten_name.get(),
            self.var_atten_dep.get(),
            self.var_atten_time.get(),
            self.var_atten_date.get(),
            self.var_atten_attendance.get()
        )

        # Refresh the Treeview to reflect the changes
        self.AttendanceReportTable.item(cursor_row, values=content['values'])

        # Update the mydata list with the updated row data
        mydata[index] = content['values']

        # Show success message
        messagebox.showinfo(
            "Success", "Data updated successfully", parent=self.root)

    # =============== RESET ==================

    def reset_data(self):
        self.var_atten_id.set("")
        self.var_atten_roll.set("")
        self.var_atten_name.set("")
        self.var_atten_dep.set("")
        self.var_atten_time.set("")
        self.var_atten_date.set("")
        self.var_atten_attendance.set("")


if __name__ == "__main__":
    root = Tk()
    obj = Attendance(root)
    root.mainloop()
