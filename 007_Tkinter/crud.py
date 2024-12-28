from tkinter import *
import mysql.connector
from tkinter import ttk
from tkinter import messagebox

root = Tk()
root.geometry("800x500")
root.title("Student usersistration")


def conn():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        port=3306,
        database="13nov_python"
    )

def getdata(self):
    rowid =  table.selection()[0]
    rdata =   table.set(rowid)
    e1.delete(0,END)
    e2.delete(0,END)
    e3.delete(0,END)
    e4.delete(0,END)
    e1.insert(0,rdata['Id'])
    e2.insert(0,rdata['Name'])
    e3.insert(0,rdata['Email'])
    e4.insert(0,rdata['Phone'])
    
def add():
    id = e1.get()
    name = e2.get()
    email = e3.get()
    phone = e4.get()
    con = conn()
    cursor = con.cursor()
    qry = "insert into users(id,uname,email,phone)values(%s,%s,%s,%s)"
    val = (id,name,email,phone)
    cursor.execute(qry,val)
    con.commit()
    e1.delete(0,END)
    e2.delete(0,END)
    e3.delete(0,END)
    e4.delete(0,END)
    e1.focus_set()
    messagebox.showinfo("Success","User Inserted successsfully")
    for i in table.get_children():
        table.delete(i)
    show()

def update():
    id = e1.get()
    name = e2.get()
    email = e3.get()
    phone = e4.get()
    con = conn()
    cursor = con.cursor()
    qry = "update users set uname=%s,email=%s,phone=%s where id=%s"
    val = (name,email,phone,id)
    cursor.execute(qry,val)
    con.commit()
    e1.delete(0,END)
    e2.delete(0,END)
    e3.delete(0,END)
    e4.delete(0,END)
    e1.focus_set()
    messagebox.showinfo("Success","User Updated successsfully")
    for i in table.get_children():
        table.delete(i)
    show()


def show():


    con = conn()
    cursor = con.cursor()
    cursor.execute("select * from users")
    data = cursor.fetchall()

    for i,(id,name,email,phone) in enumerate(data,start=1):
        table.insert("",END,values=(id,name,email,phone))
        cid=id

    e1.insert(0,cid+1)

def delete():
    id = e1.get()
    con = conn()
    cursor = con.cursor()
    cursor.execute("delete from users where id="+id+"")
    con.commit()
    messagebox.showinfo("Success","User Deleted successsfully")
    for i in table.get_children():
        table.delete(i)
    show()

l1 = Label(root,text="Id").place(x=10, y=10);
l2 = Label(root,text="Name").place(x=10,y=40)
l3 = Label(root,text="Email").place(x=10, y=70);
l4 = Label(root,text="Phone").place(x=10,y=100)




e1 = Entry(root)
e1.place(x=100,y=10)
e2 = Entry(root)
e2.place(x=100,y=40)
e3 = Entry(root)
e3.place(x=100,y=70)
e4= Entry(root)
e4.place(x=100,y=100)

b1 = Button(root,text="Add",command=add, height=2,width=7).place(x = 10, y=130)
b2 = Button(root,text="Update",command=update,  height=2,width=7).place(x = 90, y=130)
b3 = Button(root,text="Delete",command=delete, height=2,width=7).place(x = 170, y=130)

cols = ("Id","Name","Email","Phone")
table = ttk.Treeview(root,columns=cols,show="headings")

for col in cols:
    table.heading(col,text=col)
    # table.grid(row=0,column=1)
    table.place(x=10,y=200)

show()
table.bind('<Double-Button-1>',getdata)
root.mainloop()