import tkinter as tk

from tkinter import ttk,messagebox

from tkinter import*

import mysql.connector
def GetValue(event):
    e1.delete(0,END)
    e2.delete(0,END)
    e3.delete(0,END)
    e4.delete(0,END)
    row_id=listBox.selection()[0]
    select=listBox.set(row_id)
    e1.insert(0,select['id'])
    e2.insert(0,select['name'])
    e3.insert(0,select['course'])
    e4.insert(0,select['fees'])


    
def  Add():
    studid=e1.get()
    studname=e2.get()
    coursename=e3.get()
    fee=e4.get()

    mysqldb=mysql.connector.connect(host="localhost",user="root",password="anu@2028",database="project")
    mycursor=mysqldb.cursor()
    try:
        sql="INSERT INTO student_fees(id,name,course,fees) values(%s,%s,%s,%s)"
        val=(studid,studname,coursename,fee)
        mycursor.execute(sql,val)
        mysqldb.commit()

        lastid= mycursor.lastrowid
        messagebox.showinfo("information","Data insert sucessfully")
        e1.delete(0,END)
        e2.delete(0,END)
        e3.delete(0,END)
        e4.delete(0,END)
    except Exception as e:
        print(e)
        mysqldb.rollback()
        mysqldb.close()

def update():
    studid=e1.get()
    studname=e2.get()
    coursename=e3.get()
    fee=e4.get()

    mysqldb=mysql.connector.connect(host="localhost",user="root",password="anu@2028",database="project")
    mycursor=mysqldb.cursor()
    try:
        sql="update student_fees set name=%s,course=%s,fees=%s where id=%s"
        val=(studname,coursename,fee,studid)
        mycursor.execute(sql,val)
        mysqldb.commit()

        lastid= mycursor.lastrowid
        messagebox.showinfo("information","Data Update sucessfully")
        e1.delete(0,END)
        e2.delete(0,END)
        e3.delete(0,END)
        e4.delete(0,END)
    except Exception as e:
        print(e)
        mysqldb.rollback()
        mysqldb.close()


def delete():
    studid=e1.get()
   

    mysqldb=mysql.connector.connect(host="localhost",user="root",password="anu@2028",database="project")
    mycursor=mysqldb.cursor()
    try:
        sql="delete from student_fees where id=%s"
        val=(studid,)
        mycursor.execute(sql,val)
        mysqldb.commit()

        lastid= mycursor.lastrowid
        messagebox.showinfo("information","Record Deleted sucessfully")
        e1.delete(0,END)
        e2.delete(0,END)
        e3.delete(0,END)
        e4.delete(0,END)
    except Exception as e:
        print(e)
        mysqldb.rollback()
        mysqldb.close()

def show():
     mysqldb=mysql.connector.connect(host="localhost",user="root",password="anu@2028",database="project")
     mycursor=mysqldb.cursor()
     mycursor.execute("SELECT id,name,course,fees from student_fees")
     records=mycursor.fetchall()

     for i,(id,stuname,course,fee) in enumerate(records,start=1):
         listBox.insert("","end",value=(id,stuname,course,fee))
         mysqldb.close()


root=Tk()

root.geometry("800x500")
root.title("STUDENT FEES DETAILS")
root.wm_iconbitmap("C:\\Users\\Admin\\Downloads\\notepad.ico")

global e1
global e2
global e3
global e4

tk.Label(root,text="Student Fees Information",bg="white",fg="blue",font=("Helvetic","17","italic")).place(x=300,y=5)

tk.Label(root,text="StudentID").place(x=10,y=10)

Label(root,text="studentName").place(x=10,y=40)

Label(root,text="StudentCOURSE").place(x=10,y=70)
Label(root,text="StudentFEES").place(x=10,y=100)

e1=Entry(root)

e1.place(x=140,y=10)


e2=Entry(root)

e2.place(x=140,y=40)

e3=Entry(root)

e3.place(x=140,y=70)


e4=Entry(root)

e4.place(x=140,y=100)


Button(root,text="Add",command=Add,height=2,width=10,activebackground="red",activeforeground="blue",bd=3,bg="blue").place(x=30,y=130)
Button(root,text="Update",command=update,height=2,width=10,activebackground="red",activeforeground="blue",bd=3,bg="blue").place(x=140,y=130)
Button(root,text="delete",command=delete,height=2,width=10,activebackground="red",activeforeground="blue",bd=3,bg="blue").place(x=250,y=130)


cols=('id','name','course','fees')

listBox=ttk.Treeview(root,columns=cols,show='headings')


for col in cols:
    listBox.heading(col,text=col)
    
    listBox.grid(row=1,column=0,columnspan=2)

    listBox.place(x=10,y=200)
show()

listBox.bind('<Double-Button-1>',GetValue)

root.mainloop()



