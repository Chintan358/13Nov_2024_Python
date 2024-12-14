import sqlite3

conn =  sqlite3.connect("data.db")

#  conn.execute("create table student(id int primary key,name varchar(20),email varchar(20))")
# conn.execute("create table products(id int primary key, pname varchar(20),price int)")
# data =  conn.execute("select name from sqlite_master where type='table'")
# for i in data:
#     print(i)

# qry = "insert into student values(2,'Paras','paras@gmail.com')"
# conn.execute(qry)
# conn.commit()

# data =  conn.execute("select * from student")
# for i in data:
#     for k in i:
#         print(k,end=" ")
#     print()



