

import mysql.connector as mc
from mysql.connector import Error
import tkinter as tk
import tkinter.messagebox as tmb
from tkinter import ttk 
from tkinter import *
from tkcalendar import Calendar, DateEntry

e19 = '1000-01-01 00:00:00'
e20 = '1000-01-01 00:00:00'
e21 = '1000-01-01 00:00:00'
###########################

def backtolm_rg():
    window5.destroy()
    login_management()

def cdup():
    du = e0.get()
    dp = e00.get()
    drp = e000.get()

    q1 = "select username from login;"
    query_ob = conn_ob.cursor()
    query_ob.execute(q1)
    r = query_ob.fetchall()
    if du=='' or dp=='' or drp=='':
        tmb.showinfo('error','Enter every field correctly !!!')
    else:

        q2 = "select * from login where username = '{0}';".format(du)
        query_ob = conn_ob.cursor()
        query_ob.execute(q2)
        r2 = query_ob.fetchall()

        if r2==[]:
            if dp==drp:
                Q="insert into login values ('{0}', '{1}', 3, '{2}');".format(du, dp, did__)
                query_ob = conn_ob.cursor()
                query_ob.execute(Q)
                conn_ob.commit()
                tmb.showinfo('Completed', "Doctor id "+str(did__)+" created successfully.\nUsername: " + str(du) + "\nPassword: " + str(dp))
                window0.destroy()
                login_management()
            else:
                tmb.showinfo('error',"Password doesn't match !!!")
        else:
            tmb.showinfo('error','Username not available !!!')
                    
                
    
    
def exe_reg_doc():
    global did__, e0, e00, e000, window0
    
    query="select did from doctor;"
    query_ob = conn_ob.cursor()
    query_ob.execute(query)
    rdid = query_ob.fetchall()
    
    did__ = e3.get()
    name_doc = e4.get()
    name_doc = name_doc.capitalize()
    speciality = e5.get()
    speciality = speciality.capitalize()
    d_gender = gen_doc.get()

    lst=[] #result is nested tuple. This makes it easier.
    for i in range(0,len(rdid)):
        lst.append(rdid[i][0])
    
    if (did__=="" or name_doc=="" or speciality=="" or d_gender=="" or d_gender=="Gender" or did__.isnumeric()==False):
        tmb.showinfo("Error","Insert every field correctly !!!")

    elif did__.isnumeric():
        if int(did__) not in lst:
            q1="insert into doctor values('{0}','{1}','{2}','{3}');".format(did__,name_doc,speciality,d_gender)
            query_ob = conn_ob.cursor()
            query_ob.execute(q1)
            conn_ob.commit()
            window5.destroy()

            window0 = tk.Tk()
            window0.title("create doctor userpass")
            window0.geometry("1000x600")

            LL = tk.Label(window0, text = "MANAGEMENT", font= ("Arial",40), fg="dark blue").pack()
            l5 = tk.Label(window0, text = "^^^^ DO NOT CLOSE THE CURRENT WINDOW ^^^^", font=('Arial',20), fg='red').pack(pady=10)
            l2 = tk.Label(window0, text = "Create username: ", font = ('Arial', 20), fg = 'blue').pack(pady=20)
            e0 = tk.Entry(window0, width = 25, bg = 'black', fg = 'white')
            e0.pack(pady=20)

            l3 = tk.Label(window0, text = "Create password: ", font = ('Arial', 20), fg = 'blue').pack(pady=20)
            e00 = tk.Entry(window0, width = 25, bg = 'black', fg = 'pink')
            e00.pack(pady=20)
                    
            l4 = tk.Label(window0, text = "Re-enter password: ", font = ('Arial', 20), fg = 'blue').pack(pady=20)
            e000 = tk.Entry(window0, width = 25, bg = 'black', fg = 'pink')
            e000.pack(pady=20)

            b1 = tk.Button(window0, text = "Next", font = ('Arial',20), fg = 'green', command = cdup).pack()

            window0.resizable(False, False)
            window0.mainloop()

            #login_management()
        else:
            tmb.showinfo("Error", "Doctor ID already exists!!!")
   



def reg_doc():
    global e3, e4, e5, gen_doc, window5
    window5 = tk.Tk()
    window5.title("create doctor id")
    window5.geometry("1000x600")
    

    LL = tk.Label(window5, text = "REGISTER DOCTOR", font= ("Arial",40), fg="dark blue").pack()
    
    qqqq="select did from doctor order by did desc limit 1;"
    query_ob.execute(qqqq)
    r9=query_ob.fetchall()

    if r9==[]:
        L1 = tk.Label(window5, text = "**Last did value: 0", font = ("Arial",20), fg = "red").place(x=250, y=100)
    else:
        va = r9[0][0]
        L2 = tk.Label(window5, text = "**Last did value:" + str(va), font = ("Arial",20), fg = "red").place(x=250, y=100) 
    
    L3 = tk.Label(window5, text = "Create doctor's id:", font = ("Arial",20)).place(x=250, y=150)
    e3 = tk.Entry(window5, width = 20, bg = 'black', fg = 'white')
    e3.place(x=550, y=150)
    
    L4 = tk.Label(window5, text = "Enter the name of the doctor:", font = ("Arial",20), fg = 'blue').place(x=250, y=200)
    e4 = tk.Entry(window5, width = 20, bg = 'black', fg = 'white')
    e4.place(x=550, y=200)
    
    L5 = tk.Label(window5, text = "Enter the speciality of the doctor:", font = ("Arial",20), fg = 'blue').place(x=250, y=250)
    e5 = tk.Entry(window5, width = 20, bg = 'black', fg = 'white')
    e5.place(x=550, y=250)

    L6 = tk.Label(window5, text = "Enter the gender of doctor:", font = ("Arial",20), fg = 'blue').place(x=250, y=300)
    gen_doc = ttk.Combobox(window5, width = 20)
    gen_doc['values'] = ('Gender','M','F','O')
    gen_doc.place(x=550, y=300)
    gen_doc.current(0)

    b1 = tk.Button(window5, text = "Next", font = ("Arial", 20), fg = "green", command = exe_reg_doc).pack(side = 'right')
    b2 = tk.Button(window5, text = "Exit", font = ("Arial", 20), fg = "red", command = backtolm_rg).pack(side = 'left')


    window5.resizable(False, False)
    window5.mainloop()
    
       

def next21():
    window2.destroy()
    reg_doc()

#################################

def backtolm_dd():
    window6.destroy()
    login_management()


def del_name():
    global conn_ob, e6
    ds = e6.get()

    query = "select id from login;"
    query_ob = conn_ob.cursor()
    query_ob.execute(query)
    result = query_ob.fetchall()

    lst=[]
    for i in range(0,len(result)):
        lst.append(result[i][0])

    if ds == '':
        tmb.showinfo("Error","Enter doctor's id correctly!")
    elif ds.isnumeric():
        if int(ds) in lst: 
            q="delete from login where id='{0}';".format(ds)
            query_ob = conn_ob.cursor()
            query_ob.execute(q)
            conn_ob.commit()
            tmb.showinfo("Deleted", "Registeration of doctor id "+str(ds)+" deleted!!!")
            window6.destroy()
            login_management()
        elif ds not in lst:
            tmb.showinfo("Error", "ID does not exist!!!")
    else:
        tmb.showinfo("Error","Incorrect format!")



def del_doc():
    global e6, window6
    
    window6 = tk.Tk()

    window6.title("Delete doctor id")
    window6.geometry("1000x600")

    l1 = tk.Label(window6, text = "DELETE DOCTOR id", font= ("Arial",40), fg="dark blue").pack()
    l2 = tk.Label(window6, text="Enter doctor ID: ", font=("Arial",25), fg="red").pack(pady=20)
    e6 = tk.Entry(window6, width = 25, bg="black", fg="white")
    e6.pack(pady=10)

    b1 = tk.Button(window6, text="Next", font=("Arial",20), fg="green", command = del_name).pack(side="right")
    b2 = tk.Button(window6, text="Back", font=("Arial",20), fg="red", command = backtolm_dd).pack(side="left")

    window6.resizable(False, False)
    window6.mainloop()
    
def next22():
    window2.destroy()
    del_doc()
#########################################

def backtolm_vd():
    window7.destroy()
    login_management()

def done_vdr():
    window8.destroy()
    login_management()
    
    
def exe_view_doc_rep():
    global e7, window8
    d_id = e7.get()

    if d_id.isnumeric():
        q1 = "select dname from doctor where did={0}".format(d_id)
        query_ob=conn_ob.cursor()
        query_ob.execute(q1)
        r1 = query_ob.fetchall()

        if r1 == [] :
            tmb.showinfo("Error", "Doctor with ID "+ str(d_id)+" is not registered")
            window7.destroy()
            login_management()
            
        else:
            #window7.destroy()
            q2 = "select pid, disease, iop, status from d_patient natural join doctor where did='{0}';".format(d_id)
            query_ob = conn_ob.cursor()
            query_ob.execute(q2)
            r2 = query_ob.fetchall()

            if r2 == []:
                tmb.showinfo("Null", "No Results found !!!")
                window7.destroy()
                login_management()
                
            else:
                window7.destroy()
                window8 = tk.Tk()

                window8.title("Results")
                window8.geometry("1000x600")

                #create a main frame
                main_frame = tk.Frame(window8)
                main_frame.pack(fill = 'both', expand = 1)

                #create a canvas
                my_canvas = tk.Canvas(main_frame)
                my_canvas.pack(side = 'left', fill = 'both', expand = 1)
                
                #add a scrollbar to canvas
                sb = ttk.Scrollbar(main_frame, orient = 'vertical', command = my_canvas.yview)
                sb.pack(side = 'right', fill = 'y')

                # configure the canvas
                my_canvas.configure(yscrollcommand = sb.set)
                my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion = my_canvas.bbox('all')))

                #create another frame inside the canvas
                second_frame = tk.Frame(my_canvas)

                #add that new frame to a window in the canva
                my_canvas.create_window((0,0), window = second_frame, anchor="nw")
    
                count = 0
                for i in r2:
                    count += 1
                    a = i[0]
                    b = i[1]
                    c = i[2]
                    d = i[3]

                    l1 = tk.Label(second_frame, text = str(count) + ". pid: " + str(a) + ", \tdisease: " + str(b) + ", \tin/out-door: " + str(c) + ", \tstatus: " + str(d) +
                                  '\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~',font = ('Arial',20), fg = 'blue').pack()             
                b1 = tk.Button(window8, text = "Done", font=('Arial',20), fg='green', command = done_vdr).pack(side = 'bottom')
                    
                    
                window8.resizable(False, False)
                window8.mainloop()
    else:
        tmb.showinfo("Error", "Enter doctor ID correctly !!!")
                
def exe_view_doc_rep1():
    window7.destroy()
    exe_view_doc_rep()

def view_doc_rep():
    global window7, e7

    window7 = tk.Tk()

    window7.title("View doctors report")
    window7.geometry("1000x600")

    l1 = tk.Label(window7, text = "VIEW DOCTOR'S REPORT", font= ("Arial",40), fg="dark blue").pack()
    l2 = tk.Label(window7, text="Enter doctor ID to view report : ", font=("Arial",25), fg="red").pack(pady = 20)
    e7 = tk.Entry(window7, width = 25, bg="black", fg="white")
    e7.pack(pady = 20)

    b1 = tk.Button(window7, text="Next", font=("Arial",20), fg="green", command = exe_view_doc_rep).pack(side="right")
    b2 = tk.Button(window7, text="Back", font=("Arial",20), fg="red", command = backtolm_vd).pack(side="left")

    window7.resizable(False, False)
    window7.mainloop()
   
def next23():
    window2.destroy()
    view_doc_rep()

########################################
def rtlm():
    window10.destroy()
    login_management()

def find_pat():
    global e8, CI, conn_ob, window10
    disease_ = e8.get()
    st = CI.get()
    disease = disease_.capitalize()
    
    q1="select pid, pname, address from d_patient natural join patient where (disease='{0}') and (status='{1}');".format(disease,st)
    q2="select count(pid) from d_patient where disease='{0}';".format(disease) 
    
    query_ob = conn_ob.cursor()
    
    query_ob.execute(q1)
    r1=query_ob.fetchall()

    query_ob.execute(q2)
    r2=query_ob.fetchall()

    if disease_ =='' or st=='' or st=='Select choice':
        tmb.showinfo("Error","Enter values correctly.")

    elif r2[0][0]==0 or r1 == []:
        tmb.showinfo("Report","No such patient exist!")

    else:
        window9.destroy()
        window10 = tk.Tk()
        window10.title("Patient's report")
        window10.geometry("1000x600")

        #create a main frame
        main_frame = tk.Frame(window10)
        main_frame.pack(fill = 'both', expand = 1)

        #create a canvas
        my_canvas = tk.Canvas(main_frame)
        my_canvas.pack(side = 'left', fill = 'both', expand = 1)
                
        #add a scrollbar to canvas
        sb = ttk.Scrollbar(main_frame, orient = 'vertical', command = my_canvas.yview)
        sb.pack(side = 'right', fill = 'y')

        # configure the canvas
        my_canvas.configure(yscrollcommand = sb.set)
        my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion = my_canvas.bbox('all')))

        #create another frame inside the canvas
        second_frame = tk.Frame(my_canvas)

        #add that new frame to a window in the canva
        my_canvas.create_window((0,0), window = second_frame, anchor="nw")
 

        count = 0
        for i in r1:
            count += 1
            c=i[0]
            d=i[1]
            e=i[2]
            l1=tk.Label(second_frame, text = str(count) +". pid: "+str(c)+" , name: "+ str(d)+", address: "+ str(e) +
                        '\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~',font = ('Arial',20), fg = 'blue').pack()
    

        b1 = tk.Button(window10, text="Done", font=("Arial",20), fg="green", command = rtlm).pack(side="bottom")


        window10.resizable(False, False)
        window10.mainloop()



def backtolm_vpr():
    window9.destroy()
    login_management()


def view_patient_rep():
    global e8, CI, window9
    
    window9 = tk.Tk()
    window9.title("view patient report")
    window9.geometry("1000x600")

    l1 = tk.Label(window9, text = "VIEW PATIENT REPORT", font= ("Arial",40), fg="dark blue").pack()
    l2 = tk.Label(window9, text="Enter patient's disease: ", font=("Arial",25), fg="blue").pack()
    e8 = tk.Entry(window9, width = 25, bg="black", fg="white")
    e8.pack(pady = 20)

    l3 = tk.Label(window9, text="Enter patient's status (C:cured, I:Infected): ", font=("Arial",25), fg="red").pack()
    CI = ttk.Combobox(window9, width=25)
    CI['values']=('Select choice','C','I')
    CI.pack()
    CI.current(0)
   
    b1 = tk.Button(window9, text = "Next", font = ("Arial",20), fg = "green", command = find_pat).pack(side="right")
    b2 = tk.Button(window9, text = "Back", font = ("Arial",20), fg = "red", command = backtolm_vpr).pack(side="left")

    window9.resizable(False, False)
    window9.mainloop()

    
def next24():
    window2.destroy()
    view_patient_rep()

def logout_1():
    window2.destroy()
    login()
    


def login_management():
    global window2
    window2 = tk.Tk()
    window2.title("login management")
    window2.geometry("1000x600")

    L1 = tk.Label(window2, text = "MANAGEMENT", font= ("Arial",40), fg="dark blue").pack()
    
    L2 = tk.Label(window2, text = "1. Register a new doctor", font = ("Arial",20),fg = 'blue').place(x=300, y=100)
    b1 = tk.Button(window2, text ="1", font=("Arial", 20), fg="green", command = next21).place(x=700, y=100)
    
    L3 = tk.Label(window2, text = "2. Remove a doctor", font =("Arial",20),fg = 'blue').place(x=300, y=150)
    b2 = tk.Button(window2, text ="2", font=("Arial",20), fg="green", command = next22).place(x=700, y=150)
    
    L4 = tk.Label(window2, text = "3. View monthly report of doctors ", font =("Arial",20),fg = 'blue').place(x=300, y=200)
    b3 = tk.Button(window2, text ="3", font=("Arial",20), fg="green", command = next23).place(x=700, y=200)
    
    L5 = tk.Label(window2, text = "4. View disease wise patient registration", font =("Arial",20),fg = 'blue').place(x=300, y=250)
    b4 = tk.Button(window2, text ="4", font=("Arial",20), fg="green", command = next24).place(x=700, y=250)

    b5 = tk.Button(window2, text ="LOGOUT", font=("Arial", 20), fg="red", command = logout_1).place(x=450, y=400)
    
    window2.resizable(False, False)
    window2.mainloop()
    
###################################################
def reg_pat():
    pid___ = e9.get()
    pat_name = e10.get()
    pat_name.capitalize()
    pat_gen = gen_pat.get()
    bgr = blood_gr.get()
    pat_city = e11.get()
    pat_city.capitalize()

    if (pid___=="" or pat_name=="" or pat_gen=="" or pat_gen=="Choose Gender" or bgr=="" or bgr=="Choose Blood Group" or pat_city=="" or pid___.isnumeric()==False):
        tmb.showinfo("Error","Insert every field correctly !!!")
        
    else:
        query="select * from patient where pid='{0}';".format(pid___)
        query_ob = conn_ob.cursor()
        query_ob.execute(query)
        rpid = query_ob.fetchall()

        if rpid == []:
            q1 = "insert into patient values ('{0}','{1}','{2}','{3}','{4}',now());".format(pid___,pat_name,pat_gen,pat_city,bgr)
            query_ob = conn_ob.cursor()
            query_ob.execute(q1)
            conn_ob.commit()

            cq=("create table d_pat_"+str(pid___)+
                "(entry_dates datetime , symptoms varchar(100), disease varchar(50) , diagnosis varchar(100), medicines varchar(100), iop char(1) , "+
                "admit_date datetime, discharge_date datetime , appoinment_date datetime , check(iop in('i','o','I','O')));")
            query_ob = conn_ob.cursor()
            query_ob.execute(cq)
            conn_ob.commit()

            
            tmb.showinfo('created','Patient id '+str(pid___)+' registered successfully.')
            window11.destroy()
            login_receptionist()
        else:
            tmb.showinfo("Error", "Patient ID already exists!!!\nChange patient id to continue.")
            

def backtolr_rp():
    window11.destroy()
    login_receptionist()

def add_new_pat():
    global window11, e9, e10, e11, gen_pat,blood_gr
    window11 = tk.Tk()
    window11.title("reg new pat")
    window11.geometry("1000x600")

    l1 = tk.Label(window11, text="REGISTER A NEW PATIENT",font = ("Arial", 40), fg = "dark blue").pack()

    qp = "select pid from patient order by pid desc limit 1;"
    query_ob = conn_ob.cursor()
    query_ob.execute(qp)
    rr = query_ob.fetchall()

    if rr == []:
        l2 = tk.Label(window11, text = "**Last pid value: 0", font = ("Arial",20), fg = "red").place(x=250, y=100)
    else:
        val = rr[0][0]
        l3 = tk.Label(window11, text = "**Last pid value:" + str(val), font = ("Arial",20), fg = "red").place(x=250, y=100) 

    l4 = tk.Label(window11, text ="Create patient ID : ",font = ("Arial", 20),fg = 'blue').place(x=250,y=150)
    e9 = tk.Entry(window11, width = 25, bg="black", fg="white")
    e9.place(x=500,y=150)

    l5 = tk.Label(window11, text ="Enter patient name : ",font = ("Arial", 20),fg = 'blue').place(x=250,y=200)
    e10 = tk.Entry(window11, width = 25, fg="white", bg="black")
    e10.place(x=500,y=200)

    l6 = tk.Label(window11, text ="Enter patient's gender : ",font = ("Arial", 20),fg = 'blue').place(x=250,y=250)
    gen_pat = ttk.Combobox(window11, width = 25)
    gen_pat['values'] = ('Choose Gender','M','F','O')
    gen_pat.place(x=500, y=250)
    gen_pat.current(0)

    l7 = tk.Label(window11, text ="Enter Blood Group : ",font = ("Arial", 20), fg = 'blue').place(x=250,y=300)
    blood_gr = ttk.Combobox(window11, width = 25)
    blood_gr['values'] = ('Choose Blood Group','A+ve','A-ve','B+ve','B-ve','O+ve','O-ve','AB+ve','AB-ve')
    blood_gr.place(x=500,y=300)
    blood_gr.current(0)

    l8 = tk.Label(window11, text ="Enter patient's city : ",font = ("Arial", 20),fg = 'blue').place(x=250,y=350)
    e11 = tk.Entry(window11, width = 25, fg="white", bg="black")
    e11.place(x=500,y=350)

    b1 = tk.Button(window11, text = "Register", font=("Arial", 20), fg="green", command = reg_pat).place(x=915, y=400)
    b2 = tk.Button(window11, text = "Back", font=("Arial", 20), fg="red", command = backtolr_rp).place(x=0, y=400)

    window11.resizable(False, False)
    window11.mainloop()
    

def next31():
    window3.destroy()
    add_new_pat()
###################################################
def backtolr_ps():
    window12.destroy()
    login_receptionist()

def done_ps():
    window13.destroy()
    login_receptionist()

def run_pat_s():
    name_pat = e12.get()
    pg = gen_pat1.get()

    if (name_pat == '' or pg == '' or pg == 'Choose Gender'):
        tmb.showinfo("Error","Insert every field correctly !!!")
    else:
        q5="select pid from patient where pname like '%{0}%' and gender = '{1}';".format(name_pat,pg)
        query_ob = conn_ob.cursor()
        query_ob.execute(q5)
        res=query_ob.fetchall()
        
        if res==[]:
            tmb.showinfo("s result","No patient found !!!")
        else:
            window12.destroy()
            global window13
            window13 = tk.Tk()
            window13.title("Result")
            window13.geometry("1000x600")

            #create a main frame
            main_frame = tk.Frame(window13)
            main_frame.pack(fill = 'both', expand = 1)

            #create a canvas
            my_canvas = tk.Canvas(main_frame)
            my_canvas.pack(side = 'left', fill = 'both', expand = 1)
                    
            #add a scrollbar to canvas
            sb = ttk.Scrollbar(main_frame, orient = 'vertical', command = my_canvas.yview)
            sb.pack(side = 'right', fill = 'y')

            # configure the canvas
            my_canvas.configure(yscrollcommand = sb.set)
            my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion = my_canvas.bbox('all')))

            #create another frame inside the canvas
            second_frame = tk.Frame(my_canvas)

            #add that new frame to a window in the canva
            my_canvas.create_window((0,0), window = second_frame, anchor="nw")
            
            count = 0
            for j in range(len(res)):
                count += 1
                p = res[j][0]

                l2 = tk.Label(second_frame, text = str(count) + ". Patient's id (PID):   " + str(p) +
                              '\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~',font = ('Arial',20), fg = 'blue').pack()
            b = tk.Button(window13, text = "Done", font=("Arial", 20), fg="green", command = done_ps).place(x=450, y=550)
                
            window13.resizable(False, False)
            window13.mainloop()
        

def pat_s():
    global window12, e12, gen_pat1
    window12 = tk.Tk()
    window12.title("search a patient")
    window12.geometry("1000x600")

    l1 = tk.Label(window12, text="SEARCH A PATIENT",font = ("Arial", 40), fg = "dark blue").pack()

    l2 = tk.Label(window12, text = "Enter patient's name : ", font = ("Arial",20), fg = "blue").pack(pady=30)
    e12 = tk.Entry(window12, width = 25, fg="white", bg="black")
    e12.pack(pady=10)

    l3 = tk.Label(window12, text = "Enter patient's blood group: ", font = ("Arial",20), fg = "blue").pack(pady=20)
    gen_pat1 = ttk.Combobox(window12, width = 25)
    gen_pat1['values'] = ('Choose Gender','M','F','O')
    gen_pat1.pack(pady=10)
    gen_pat1.current(0)

    b1 = tk.Button(window12, text = "Search", font=("Arial", 20), fg="green", command = run_pat_s).place(x=915, y=400)
    b2 = tk.Button(window12, text = "Back", font=("Arial", 20), fg="red", command = backtolr_ps).place(x=0, y=400)

    window12.resizable(False, False)
    window12.mainloop()
    

def next32():
    window3.destroy()
    pat_s()
###############################################
def cfa():
    c_a = e13.get()
    
    if c_a == '':
        tmb.showinfo('error','Enter patient id !!!')
    elif c_a.isnumeric()==False:
        tmb.showinfo('error','Enter patient correctly,\ncharecters like alphabets and special characters are not allowed !!!')
    else:
        q10 = "select * from patient where pid = " + str(c_a) + str(';')
        query_ob.execute(q10)
        r3 = query_ob.fetchall()

        if r3==[]:
            tmb.showinfo('error','Patient not registered !!!')
            window14.destroy()
            login_receptionist()

        else:
            q11 = "select date(appoinment_date) from d_pat_"+str(c_a)+" order by appoinment_date desc limit 1;"
            query_ob.execute(q11)
            r4 = query_ob.fetchall()

            if r4==[]:
                tmb.showinfo('result','No appoinments !!!')
                window14.destroy()
                login_receptionist()
            elif r4[0][0]=="1000-01-01 00:00:00":
                tmb.showinfo('result','No appoinments !!!')
                window14.destroy()
                login_receptionist()
            else:
                tmb.showinfo('result','Pid:  ' + str(c_a) + "\nLast Appoinment date:  " + str(r4[0][0]))
                window14.destroy()
                login_receptionist()
    

def backtolr_ca():
    window14.destroy()
    login_receptionist()

def ca():
    global window14, e13
    window14 = tk.Tk()
    window14.title("check appoinment")
    window14.geometry("1000x600")

    l1 = tk.Label(window14, text = "SEARCH FOR APPOINMENT",font = ("Arial", 40), fg = "dark blue").pack()

    l2 = tk.Label(window14, text = "Enter patient's id (PID no):", font = ('Arial',20), fg = 'blue').pack(pady=40)
    e13 = tk.Entry(window14, width = 25, bg='black', fg='white')
    e13.pack(pady=10)

    l3 = tk.Label(window14, text = "", font = ('Arial',20), fg = 'blue').pack(pady=40)

    b1 = tk.Button(window14, text='Check', font=('Arial',20), fg='green', command = cfa).place(x=915, y=400)
    b2 = tk.Button(window14, text = "Back", font=("Arial", 20), fg="red", command = backtolr_ca).place(x=0, y=400)

    window14.resizable(False, False)
    window14.mainloop()
    
def next33():
    window3.destroy()
    ca()

def logout_2():
    window3.destroy()
    login()

def login_receptionist():
    global window3
    window3 = tk.Tk()
    window3.title("Welcome to Hospital Management Sysytem")
    window3.geometry("1000x600")

    LL = tk.Label(window3, text = "RECEPTIONIST", font = ('Arial', 40), fg = 'dark blue').pack()

    l1 = tk.Label(window3, text="1. Register a new patient ",font = ("Arial", 20),fg = 'blue').place(x=200,y=100)
    b1 = tk.Button(window3, text ="1", font=("Arial", 20), fg="green", command = next31).place(x=700, y=100)

    l2 = tk.Label(window3, text="2. Search for a new patient ",font = ("Arial", 20),fg = 'blue').place(x=200,y=150)              
    b2 = tk.Button(window3, text ="2", font=("Arial", 20), fg="green", command = next32).place(x=700, y=150)

    l3 = tk.Label(window3, text="3. Check for Appointment ",font = ("Arial", 20),fg = 'blue').place(x=200,y=200) 
    b3 = tk.Button(window3, text ="3", font=("Arial", 20), fg="green", command = next33).place(x=700, y=200)

    b4 = tk.Button(window3, text ="LOGOUT", font=("Arial", 20), fg="red", command = logout_2).place(x=450, y=350)
    
    window3.resizable(False, False)
    window3.mainloop()

##########################  
def cont_dp():
    global da, da1, da2
    pid_ = id_pid
    yid = id_did
    symp = e15.get()
    symp.capitalize()
    bimari = e16.get()
    bimari.capitalize()
    dia = e17.get()
    dia.capitalize()
    med = e18.get()
    med.capitalize()
    iop = IO.get()
    iop.capitalize()
    ad = e19
    dd = e20
    apd = e21
    status = IC.get()
    status.capitalize()
    if (symp == '' or bimari == '' or dia == '' or med == '' or iop == 'Select choice' or status == 'Select choice'
        or pid_ == '' or yid == '' or (ad=='1000-01-01 00:00:00' and dd=='1000-01-01 00:00:00' and apd=='1000-01-01 00:00:00')):#or (ad==dd)
        tmb.showinfo('error', "Enter fields correctly !!!")
    elif dd == '1000-01-01 00:00:00':
        qq = ("insert into d_pat_"+str(pid_)+"(entry_dates,symptoms,disease,diagnosis,medicines,iop,admit_date,appoinment_date) values("+
              "CURRENT_TIMESTAMP(),'{0}','{1}','{2}','{3}','{4}','{5}','{6}');".format(symp,bimari,dia,med,iop,ad,apd))
        query_ob.execute(qq)
        conn_ob.commit()

        qqq="insert into d_patient values ('{0}','{1}','{2}','{3}','{4}')".format(pid_,yid,bimari,iop,status)
        query_ob.execute(qqq)
        conn_ob.commit()

        tmb.showinfo('Done',"Diagnose recorded !!!")
            
        window16.destroy()
        login_doctor(yid)
            
    elif ad == '1000-01-01 00:00:00':
        qq = ("insert into d_pat_"+str(pid_)+"(entry_dates,symptoms,disease,diagnosis,medicines,iop,discharge_date,appoinment_date) values"+
              "(CURRENT_TIMESTAMP(),'{0}','{1}','{2}','{3}','{4}','{5}','{6}');".format(symp,bimari,dia,med,iop,dd,apd))
        query_ob.execute(qq)
        conn_ob.commit()

        qqq="insert into d_patient values ('{0}','{1}','{2}','{3}','{4}')".format(pid_,yid,bimari,iop,status)
        query_ob.execute(qqq)
        conn_ob.commit()

        tmb.showinfo('Done',"Diagnose recorded !!!")
            
        window16.destroy()
        login_doctor(yid)
            
    elif ad == '1000-01-01 00:00:00' and apd == '1000-01-01 00:00:00':
        qq = ("insert into d_pat_"+str(pid_)+"(entry_dates,symptoms,disease,diagnosis,medicines,iop,discharge_date) values"+
              "(CURRENT_TIMESTAMP(),'{0}','{1}','{2}','{3}','{4}','{5}');".format(symp,bimari,dia,med,iop,dd))
        query_ob.execute(qq)
        conn_ob.commit()

        tmb.showinfo('Done',"Diagnose recorded !!!")

        qqq="insert into d_patient values ('{0}','{1}','{2}','{3}','{4}')".format(pid_,yid,bimari,iop,status)
        query_ob.execute(qqq)
        conn_ob.commit()
            
        window16.destroy()
        login_doctor(yid)
            
    else:
        tmb.showinfo('error','DATES ERROR')
        

def calendar_view():
    global da, e19
    def print_sel():
        global da, e19
        da = cal.selection_get()
        e19 = da
        ll1.config(text = da)
        top.destroy()

    def nod():
        global da, e19
        da = '1000-01-01 00:00:00'
        e19 = da
        ll1.config(text = 'None')
        top.destroy()

    top = tk.Toplevel(window16)

    cal = Calendar(top,
                   font="Arial 14", selectmode='day',
                   cursor="hand1")
    cal.pack(fill="both", expand=True)
    b1 = ttk.Button(top, text="Ok", command=print_sel).pack(side = 'right')
    b2 = ttk.Button(top, text="None", command=nod).pack(side = 'left')

def calendar_view1():
    global da1
    def print_sel():
        global da1, e20
        da1 = cal.selection_get()
        e20 = da1
        ll2.config(text = da1)
        top.destroy()

    def nod():
        global da1, e20
        da1 = '1000-01-01 00:00:00'
        e20 = da1
        ll2.config(text = 'None')
        top.destroy()

    top = tk.Toplevel(window16)

    cal = Calendar(top,
                   font="Arial 14", selectmode='day',
                   cursor="hand1")
    cal.pack(fill="both", expand=True)
    b1 = ttk.Button(top, text="Ok", command=print_sel).pack(side = 'right')
    b2 = ttk.Button(top, text="None", command=nod).pack(side = 'left')
    

def calendar_view2():
    global da2
    def print_sel():
        global da2, e21
        da2 = cal.selection_get()
        e21 = da2
        ll3.config(text = da2)
        top.destroy()

    def nod():
        global da2, e21
        da2 = '1000-01-01 00:00:00'
        e21 = da2
        ll3.config(text = 'None')
        top.destroy()

    top = tk.Toplevel(window16)

    cal = Calendar(top,
                   font="Arial 14", selectmode='day',
                   cursor="hand1")
    cal.pack(fill="both", expand=True)
    b1 = ttk.Button(top, text="Ok", command=print_sel).pack(side = 'right')
    b2 = ttk.Button(top, text="None", command=nod).pack(side = 'left')


def exe_dp():
    global yid, id_did
    yid = id_did
    window15.destroy()
    global window16, e15, e16, e17, e18, e19, e20, e21, IO, IC, ll1, ll2, ll3
    window16 = tk.Tk()
    window16.title("diagnosis patient")
    window16.geometry("1000x600")

    s = ttk.Style(window16)
    s.theme_use('clam')

    L1 = tk.Label(window16, text = "DOCTOR", font = ("Arial",40), fg="dark blue").pack()

    l2 = tk.Label(window16, text = "1. Enter symptoms of patient: ", font = ("Arial", 20),fg = 'blue').place(x = 170, y=80)
    e15 = tk.Entry(window16, width = 25, bg = 'black', fg = 'white')
    e15.place(x = 630, y=80)
    

    l3 = tk.Label(window16, text = "2. Enter disease of patient: ", font = ("Arial", 20),fg = 'blue').place(x = 170, y=120)
    e16 = tk.Entry(window16, width = 25, bg = 'black', fg = 'white')
    e16.place(x = 630, y=120)

    l4 = tk.Label(window16, text = "3. Enter diagnosis done or suggested: ", font = ("Arial", 20),fg = 'blue').place(x = 170, y=160)
    e17 = tk.Entry(window16, width = 25, bg = 'black', fg = 'white')
    e17.place(x = 630, y=160)

    l5 = tk.Label(window16, text = "4. Enter medicines prescribed: ", font = ("Arial", 20),fg = 'blue').place(x = 170, y=200)
    e18 = tk.Entry(window16, width = 25, bg = 'black', fg = 'white')
    e18.place(x = 630, y=200)

    l6 = tk.Label(window16, text = "5. Enter whether patient is indoor or outdoor [I,O]: ", font = ("Arial", 20),fg = 'blue').place(x = 170, y=240)
    IO = ttk.Combobox(window16, width=25)
    IO['values']=('Select choice','I','O')
    IO.place(x = 630, y=240)
    IO.current(0)

    l7 = tk.Label(window16, text = "6. Enter ADMIT date (YYYY-MM-DD): ", font = ("Arial", 20),fg = 'blue').place(x = 170, y=280)
    b1 = ttk.Button(window16, text='Select date', command=calendar_view).place(x = 630, y=280)
    ll1 = tk.Label(window16, text='', font = ("Arial", 20),fg = 'blue')
    ll1.place(x = 800, y=280)
    
    l8 = tk.Label(window16, text = "7. Enter DISCHARGE date (YYYY-MM-DD): ", font = ("Arial", 20),fg = 'blue').place(x = 170, y=320)
    b2 = ttk.Button(window16, text='Select date', command=calendar_view1).place(x = 630, y=320)
    ll2 = tk.Label(window16, text='', font = ("Arial", 20),fg = 'blue')
    ll2.place(x = 800, y=320)

    l9 = tk.Label(window16, text = "8. Enter next APPOINMENT date (YYYY-MM-DD): ", font = ("Arial", 20),fg = 'blue').place(x = 170, y=360)
    b3 = ttk.Button(window16, text='Select date', command=calendar_view2).place(x = 630, y=360)
    ll3 = tk.Label(window16, text='', font = ("Arial", 20),fg = 'blue')
    ll3.place(x = 800, y=360)

    l10 = tk.Label(window16, text = "9. Cured-'C'/Infected-'I': ", font = ("Arial", 20),fg = 'blue').place(x = 170, y=400)
    IC = ttk.Combobox(window16, width=25)
    IC['values']=('Select choice','C','I')
    IC.place(x = 630, y=400)
    IC.current(0)

    b4 = tk.Button(window16, text = "Continue", font = ('Arial', 20), fg = 'green', command = cont_dp).pack(side = 'bottom')

    
    
    window16.resizable(False, False)
    window16.mainloop()

def backtold():
    window15.destroy()
    login_doctor(id_did)

def OK():
    window15.destroy()
    login_doctor(id_did)

def dp():
    global pid_
    pid_ = e14.get()
    window4.destroy()
    
    global window15, e15
    window15 = tk.Tk()
    window15.title("login doctor")
    window15.geometry("1000x600")

    L1 = tk.Label(window15, text = "DOCTOR", font = ("Arial",40), fg="dark blue").pack()

    q6 = "select * from patient where pid={0};".format(pid_)
    query_ob.execute(q6)
    r = query_ob.fetchall()

    l1 = tk.Label(window15, text = "Patient id (pid):  " + str(r[0][0]) +
                  "\nPatient's name:  " + str(r[0][1]) +
                  "\nPatient's gender:  " + str(r[0][2]) +
                  "\nPatient's blood group:  " + str(r[0][4]), font = ('Arial',20), fg = 'orange').pack()

    q8 = "select * from d_pat_"+str(pid_)+";"
    query_ob.execute(q8)
    r3 = query_ob.fetchall()

    l2 = tk.Label(window15, text = "Patient history: " + str(len(r3)) + "*", font = ('Arial',20), fg = 'brown').pack()

    #create a main frame
    main_frame = tk.Frame(window15)
    main_frame.pack(fill = 'both', expand = 1)

    #create a canvas
    my_canvas = tk.Canvas(main_frame)
    my_canvas.pack(side = 'left', fill = 'both', expand = 1)
    
    #add a scrollbar to canvas
    sb = ttk.Scrollbar(main_frame, orient = 'vertical', command = my_canvas.yview)
    sb.pack(side = 'right', fill = 'y')

    # configure the canvas
    my_canvas.configure(yscrollcommand = sb.set)
    my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion = my_canvas.bbox('all')))

    #create another frame inside the canvas
    second_frame = tk.Frame(my_canvas)

    #add that new frame to a window in the canva
    my_canvas.create_window((0,0), window = second_frame, anchor="nw")
    

    
    for i in range(len(r3)):
        l3 = tk.Label(second_frame, text = "\n^|History: " + str(i+1) +
                      "|^ ,\n|Entry date: " + str(r3[i][0]) +
                      "| ,\n|Symptoms: " + str(r3[i][1]) +
                      "| ,\n|Disease: " + str(r3[i][2]) +
                      "| ,\n|Diagnosis: " + str(r3[i][3]) +
                      "| ,\n|Medicines given: " + str(r3[i][4]) +
                      "| ,\n|Patient admitted or not: " + str(r3[i][5]) +
                      "| ,\n|Admit date (if admited): " + str(r3[i][6]) +
                      "| ,\n|Discharge date: " + str(r3[i][7]) +
                      "| ,\n|Appoinment date: " + str(r3[i][8]) +
                      '| ,\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~',
                      font = ('Arial',20), fg = 'blue').pack()

    b1 = tk.Button(window15, text = 'Continue', font = ('Arial',20), fg = 'green', command = exe_dp).pack(side = 'bottom')
    b2 = tk.Button(window15, text = 'Back', font = ('Arial',20), fg = 'red', command = OK).pack(side = 'bottom')

    window15.resizable(False, False)
    window15.mainloop()
    

def next41():
    global id_pid
    id_pid = e14.get()
    if id_pid == "":
        tmb.showinfo('error',"Enter patient id !!!")
    elif id_pid.isnumeric()==False:
        tmb.showinfo('error',"Enter patient id correctly,\ncharacter like alphabets and special character are not allowed !!!")
    else:
        q6 = "select * from patient where pid={0};".format(id_pid)
        query_ob.execute(q6)
        r = query_ob.fetchall()
        if r == []:
            tmb.showinfo('error','Patient is not registered !!!')
        else:
            dp()
    

def logout_doctor():
    window4.destroy()
    login()

def login_doctor(x):
    global window4, id_did, e14
    window4 = tk.Tk()
    window4.title("Welcome to Hospital Management Sysytem")
    window4.geometry("1000x600")

    id_did = x
    
    L1 = tk.Label(window4, text = "DOCTOR", font= ("Arial",40), fg="dark blue").pack()

    l2 = tk.Label(window4, text = 'Diagnose the patient:', font = ('Arial',20), fg='blue').pack(pady=30)
    l2 = tk.Label(window4, text = "Enter patient's id: ", font = ('Arial',20), fg='blue').pack(pady=10)
    e14 = tk.Entry(window4, width = 25, bg = 'black', fg = 'white')
    e14.pack()


    b1 = tk.Button(window4, text ="Next", font =("Arial",20), fg = 'green', command = next41).pack(side = 'right')
    b2 = tk.Button(window4, text ="LOGOUT", font=("Arial", 20), fg="red", command = logout_doctor).pack(side = 'left')
    
    window4.resizable(False, False)
    window4.mainloop()
   
def checkup():  #username password check
    global e1, e2, conn_ob, query_ob, u
    u = e1.get()
    ps = e2.get()
    q99 = "select * from login"
    query_ob = conn_ob.cursor()
    query_ob.execute(q99)
    r99 = query_ob.fetchall()

    if (u != '' and ps != ''):
        for i in r99:
            if i[0] == u:
                if i[1] == ps:
                    role = i[2]
                    if role == 1:
                        tmb.showinfo("login_management","Welcome "+u)
                        window1.destroy()
                        login_management()
                        break
                    elif role == 2:
                        tmb.showinfo("login_receptionist","Welcome "+u)
                        window1.destroy()
                        login_receptionist()
                        break
                    elif role==3:
                        id_ = i[3]
                        tmb.showinfo("login_doctor","Welcome "+u)
                        window1.destroy()
                        login_doctor(id_)
                        break
        else:
            tmb.showinfo("Error","INCORRECT USERNAME OR PASSWORD !!!")
        
    else:
        tmb.showinfo("Error","Enter both USERNAME and PASSWORD !!!")


def back1():
    window1.destroy()
    w()
    

def login():  #username password enter
   global e1, e2, window1
   window1 = tk.Tk()

   window1.title("Login window")
   window1.geometry("1000x600")

   l1 = tk.Label(window1, text = "WELCOME TO HOSPITAL MANAGEMENT SYSTEM", font = ("Arial", 20), fg = "purple").pack(pady = 20)
   l2 = tk.Label(window1, text = "Username: ", font = ("Arial", 20), fg = "blue").pack(pady = 10)
   e1 = tk.Entry(window1, width = 25, bg = "black", fg = "red")
   e1.pack()
   l3 = tk.Label(window1, text = "Password: ", font = ("Arial", 20), fg = "blue").pack(pady = 10)
   e2 = tk.Entry(window1, width = 25, bg = "black", fg = "white", show = "*")
   e2.pack()
   b1 = tk.Button(window1, text = "Login", font = ("Arial", 20), fg = "green", command = checkup).pack(pady=20)
   b2 = tk.Button(window1, text = "Back", font = ("Arial", 20), fg = "red", command = back1).pack(side = 'left')


   window1.resizable(False, False)
   window1.mainloop()



def con():  #connecting python to mysql
    global E, conn_ob
    p = E.get()
    try:
        conn_ob=mc.connect(host="localhost",database="hospital",user="root",password=p)
        query_ob=conn_ob.cursor()
        if (conn_ob.is_connected()):
            tmb.showinfo("Connected","CONNECTED, click OK to continue.")
            window.destroy()
            login()
            
  
    except Error as e:
        tmb.showinfo("Error occured",e)



#main start

def w():

    global window, E
    window = tk.Tk()

    window.title("Welcome to Hospital Management Sysytem")
    window.geometry("1000x600")

    LL = tk.Label(window, text = "HOSPITAL MANAGEMENT SYSTEM", font = ("Arial", 40), bg = "pink", fg = "blue").pack(fill="x")

    L1 = tk.Label(window, text = "Enter MySql password to initialize.", font = ("Arial", 20), fg = "blue").pack(pady = 170)
    E = tk.Entry(window, width = 25, bg = 'black', fg = 'white', show = '*')
    E.pack(pady = 20)
    B1 = tk.Button(window, text = "Next", font = ("Arial", 20), fg = "green", command = con).pack(side = 'right')
    B2 = tk.Button(window, text = "Exit", font = ("Arial", 20), fg = "red", command = window.destroy).pack(side = 'left')

        
    window.resizable(False, False)
    window.mainloop()

#main start
w()
