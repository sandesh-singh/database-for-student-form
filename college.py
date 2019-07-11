import sqlite3
import tkinter as tk
from tkinter import messagebox

mainwindow = tk.Tk()
mainwindow.title("Registration form")
connection = sqlite3.connect('student2.db')
print("Database opened successfully")

TABLE_NAME = "student_table"
STUDENT_ID = "student_id"
STUDENT_NAME = "student_name"
STUDENT_COLLEGE = "student_college"
STUDENT_ADDRESS = "student_address"
STUDENT_PHONE = "student_phone"

connection.execute(
    " CREATE TABLE IF NOT EXISTS " + TABLE_NAME + " ( " + STUDENT_ID + " INTEGER PRIMARY KEY " " AUTOINCREMENT, " +
    STUDENT_NAME + " TEXT, " + STUDENT_COLLEGE + " TEXT, " + STUDENT_ADDRESS + " TEXT, " + STUDENT_PHONE +
    " INTEGER);")
print("table created successfully")

name1 = tk.Label(mainwindow, text="STUDENT_NAME")
name1.pack()
name_field1 = tk.Entry(mainwindow)
name_field1.pack()

college1 = tk.Label(mainwindow, text="STUDENT_COLLEGE")
college1.pack()
name_field2 = tk.Entry(mainwindow)
name_field2.pack()

address1 = tk.Label(mainwindow, text="STUDENT_ADDRESS")
address1.pack()
name_field3 = tk.Entry(mainwindow)
name_field3.pack()

phone1 = tk.Label(mainwindow, text="STUDENT_PHONE")
phone1.pack()
name_field4 = tk.Entry(mainwindow)
name_field4.pack()

def database():
    name = name_field1.get()
    college = name_field2.get()
    address = name_field3.get()
    phone = name_field4.get()

    connection.execute("INSERT INTO " + TABLE_NAME + " ( " + STUDENT_NAME + " , " + STUDENT_COLLEGE + " , "
                       + STUDENT_ADDRESS + " , " + STUDENT_PHONE + " ) VALUES ( '" + name + "', '" + college + "' , " + " '"
                       + address + "' , " + phone + ");")
    connection.commit()
    messagebox.showinfo("info", "data saved")
button = tk.Button(mainwindow, text="submit", command=lambda: database())
button.pack()

def retrive():
    cursor = connection.execute("SELECT * FROM " + TABLE_NAME + " ;")
    for row in cursor:
        print("student id is : ", row[0])
        print("student name is: ", row[1])
        print("student college is:", row[2])
        print("student address is", row[3])
        print("student phone number is ", row[4])
button1 = tk.Button(mainwindow, text="retrive", command=lambda: retrive())
button1.pack()


mainwindow.mainloop()
