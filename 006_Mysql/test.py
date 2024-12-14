import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  database="13nov_python"
)

cursor =  mydb.cursor()

# qry = "insert into users values(0,'kb','kb@gmail.com','8596857485')"
qry = "insert into users values(%s,%s,%s,%s)"
val = (0,'paras','paras@gmal.com','5263589696')
cursor.execute(qry,val)
mydb.commit()





