import  mysql.connector
mydb = mysql.connector.connect(host = "localhost", user = "root", passwd = "", database = "harshdb")

mycursor = mydb.cursor()

sqlform = "Insert into employee(name,sal) values (%s,%s)"
employees = [("harshit", 20000), ("amit", 30000), ("ankita", 40000), ]
mycursor.executemany(sqlform, employees)
mydb.commit()