

import mysql.connector as mc
from mysql.connector import Error
import tkinter as tk
import tkinter.messagebox as tmb
from tkinter import *

def create1():
    global e, w2d, E
    p = E.get()
    
    
    try:
        conn_ob=mc.connect(host="localhost",user="root",password = p)

        if (conn_ob.is_connected()):
            q1="create database if not exists hospital;"
            query_ob=conn_ob.cursor()
            query_ob.execute(q1)
            conn_ob.commit()

            q2="use hospital;"
            query_ob=conn_ob.cursor()
            query_ob.execute(q2)
            conn_ob.commit()

            q3=("create table if not exists patient"+
                "(pid int primary key not null, pname varchar(30) not null, gender char(1) not null, address varchar(50) not null, blood_group varchar(5) not null,"+
                "reg_pat_date datetime not null, check(gender in('M','F','O')),check (blood_group in('A+ve','A-ve','B+ve','B-ve','AB+ve','AB-ve','O+ve','O-ve')));")
            query_ob=conn_ob.cursor()
            query_ob.execute(q3)
            conn_ob.commit()

            q4=("create table if not exists doctor"+
                "(did int primary key not null, dname varchar(30) not null, speciality varchar(50) not null, gender char(1) not null," +
                "check(gender in ('M','F','O')));")
            query_ob=conn_ob.cursor()
            query_ob.execute(q4)
            conn_ob.commit()

            q5=("create table if not exists d_patient"+
                "(pid int references patient(pid), did int references doctor(did), disease varchar(30) not null, iop char(1) not null,"+
                "status char(1) not null, check (iop in('I','O')));")
            query_ob=conn_ob.cursor()
            query_ob.execute(q5)
            conn_ob.commit()

            q6="create table if not exists login(username char(20) primary key, password char(20), role int(1), id int, check( role in (1,2,3)));"
            query_ob=conn_ob.cursor()
            query_ob.execute(q6)
            conn_ob.commit()

            q7="insert into login (username, password, role) values('u1','p1',1),('u2','p2',2);"
            query_ob=conn_ob.cursor()
            query_ob.execute(q7)
            conn_ob.commit()

            q8="insert into login values ('u3','p3',3, 1);"
            query_ob=conn_ob.cursor()
            query_ob.execute(q8)
            conn_ob.commit()

            q9 = "insert into doctor values(1, 'Test doctor', 'Test Speciality', 'O');"
            query_ob=conn_ob.cursor()
            query_ob.execute(q9)
            conn_ob.commit()

            

            tmb.showinfo("Installing...","INSTALLATION COMPLETED !!!")
            window1.destroy()

            window2 = tk.Tk()

            window2.title("3 sample users for testing")
            window2.geometry("1000x600")

            L1 = tk.Label(window2, text = "3 sample users for testing", font = ("Arial",20)).place(x=0, y=0)
            L2 = tk.Label(window2, text = "These are as follows:-", font = ("Arial",20)).place(x=0, y=25)
            L3 = tk.Label(window2, text = "1. Username_1 = u1,      Password_1 = p1", font = ("Arial",20)).place(x=0, y=50)
            L4 = tk.Label(window2, text = "2. Username_2 = u2,      Password_2 = p2", font = ("Arial",20)).place(x=0, y=75)
            L5 = tk.Label(window2, text = "3. Username_3 = u3,      Password_3 = p3      id(did) = 1", font = ("Arial",20)).place(x=0, y=100)           
            
            B1 = tk.Button(window2, text = "DONE", font=("ComicSansMS", 20), fg="red", command = window2.destroy).pack(side = 'right')
            
            

            window2.resizable(False, False)
            window2.mainloop()

    except Error as e:
        tk.messagebox.showinfo("Error while connecting to MySQL",e)

def back1():
    window1.destroy()
    w()


def create():
    global E, window1
    window1 = tk.Tk()

    window1.title("PASSWORD (MySql)")
    window1.geometry("1000x600")

    l1 = tk.Label(window1, text = "Enter your MySQL password: ", font = ("Arial", 40), bg = "pink", fg = "blue").pack(fill='x')
    E = tk.Entry(window1, width = 50, bg="black", fg="white", show="*")
    E.pack(pady=10)
    l2 = tk.Label(window1, text = "Click next to continue.", font = ("Arial", 20)).pack(side = 'left')
    B1 = tk.Button(window1, text = "Next", font=("ComicSansMS", 20), fg="green", command = create1).place(x=940,y=500)

    B2 = tk.Button(window1, text = "Back", font=("ComicSansMS", 20), fg="red", command = back1).place(x=10, y=500)

    
    window1.resizable(False, False)
    window1.mainloop()

def next1():
    window.destroy()
    create()
    

def w():
    global window
    window = tk.Tk()

    window.title("Hospital Management Sysytem Installation Wizard")
    window.geometry("1000x600")

    F1 = tk.Frame(window, borderwidth = 6).pack(side = 'top', fill='x')
    F2 = tk.Frame(window, borderwidth = 6).pack(side = 'left', fill='y')
    F3 = tk.Frame(window, borderwidth = 6).pack(side = 'bottom', fill='x')

    L1 = tk.Label(F1, text = "Hospital Management System Installation Wizard", font = ("Arial", 40), bg = "pink", fg = "blue").pack(fill="x")
    L2 = tk.Label(F2, text = "Created by:- Apoorva Jadhav, Aayushi Kapoor & Anubhav Utkarsh [12th SCIENCE, session: 2020-21]", font = ("Arial", 20), fg = "purple").pack()
    L3 = tk.Label(F2, text = "==> Initially a databases will be created containing 4 tables as follows:", font = ("Arial", 20)).place(x=0,y=130)
    L4 = tk.Label(F2, text = "    1. Doctor table                          2. Patient table", font = ("Arial", 20)).place(x=0,y=155)
    L5 = tk.Label(F2, text = "    3. Diagnosise of patient table   4. Login table", font = ("Arial", 20)).place(x=0,y=180)
    L6 = tk.Label(F2, text = "==> MySQL must be installed before continuing.\nModules: mysql-connector, tkcalendar must be installed first ",font=("Arial", 20), fg = 'red').place(x=0,y=205)
    L7 = tk.Label(F2, text = "==> System requirements:", font = ("Arial", 20)).place(x=0,y=255)
    L8 = tk.Label(F2, text = "  (1) Storage minimum 1Gb, RAM minimum 1GB",font = ("Arial", 20)).place(x=0,y=280)
    L9 = tk.Label(F2, text = "  (2) Operating system :- MacOS Catalina",font = ("Arial", 20)).place(x=0,y=305)
    L10 = tk.Label(F3, text = "To continue, click next.", font = ("Arial", 20), fg = 'green').place(x=0,y=340)
     
    b1 = tk.Button(window, text="Next", font=("ComicSansMS", 20), fg="green", command = next1).place(x=940,y=500)
    b2 = tk.Button(window, text="Exit", font=("ComicSansMS", 20), fg="red", command = window.destroy).place(x=10, y=500)

    window.resizable(False, False)
    window.mainloop()


#main start
w()

if __name__ == '__main__':
    w()
