

import mysql.connector as mc
from mysql.connector import Error
import tkinter as tk
import tkinter.messagebox as tmb
from tkinter import *

def uninstall():
    global E, window
    p = E.get()
    
    try:
        conn_ob=mc.connect(host="localhost",user="root",password=p)

        if (conn_ob.is_connected()):
            q="drop database hospital;"
            query_ob=conn_ob.cursor()
            query_ob.execute(q)
            conn_ob.commit()
            conn_ob.close()

            tmb.showinfo("Uninstalling...","UNINSTALLATION COMPLETED !!!")

            window.destroy()

    except Error as e:
        tmb.showinfo("Error occured",e)
        
def w():
    global E,window
    window = tk.Tk()
    window.title("Hospital Management Sysytem Uninstallation Wizard")
    window.geometry("1000x600")

    L1 = tk.Label(window, text = "Hospital Management Sysytem Uninstallation Wizard", font = ("Arial", 20), bg = "pink", fg = "blue").pack(fill="x")
    L2 = tk.Label(window, text = "WARNING", font = ("Arial", 20), fg = "red").pack(pady=20)
    L3 = tk.Label(window, text = "All the data including database and all the tables will be deleted !!!", font = ("Arial", 20), fg = "red").pack(pady=10)
    L4 = tk.Label(window, text = "Enter your MySQL password: ", font = ("Arial", 20)).pack(pady=30)
    E = tk.Entry(window, width = 50, bg="black", fg="white", show="*")
    E.pack(pady = 20)
    B2 = tk.Button(window, text = "Exit", font = ("ComicSansMS", 20), fg = "green", command = window.destroy).place(x=0,y=500)
    B1 = tk.Button(window, text = "UNINSTALL NOW", font = ("ComicSansMS", 20), fg = "red", command = uninstall).place(x=805,y=500)


    window.resizable(False, False)
    window.mainloop()

        

#main start
w()
