from tkinter import *
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  database="13nov_python"
)

cursor =  mydb.cursor()

def addData(name,email,phone):
    qry = "insert into users values(%s,%s,%s,%s)"
    value=(0,name,email,phone)
    cursor.execute(qry,value)
    mydb.commit()
    print("Data inserted")

root = Tk()
root.geometry("500x500")

uname = Label(root,text="Username")
email =Label(root,text="Email")
phone = Label(root, text="Phone")

t1 = Entry(root)
t2 = Entry(root)
t3 = Entry(root)

submit = Button(root,text="Submit",command=lambda:addData(t1.get(),t2.get(),t3.get()))

# uname.pack(side=TOP)
# email.pack(side=LEFT)
# phone.pack(side=RIGHT)

# uname.grid(row=0,column=0)
# email.grid(row=1, column=0)
# phone.grid(row=2,column=0)
# t1.grid(row=0,column=1)
# t2.grid(row=1,column=1)
# t3.grid(row=2,column=1)

uname.place(x=100,y=100)
email.place(x=100,y=150)
phone.place(x=100,y=200)

t1.place(x=200,y=100)
t2.place(x=200,y=150)
t3.place(x=200,y=200)

submit.place(x=200,y=250)

root.mainloop()