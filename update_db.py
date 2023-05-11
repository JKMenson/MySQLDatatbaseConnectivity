import  mysql.connector
mydb = mysql.connector.connect(host = "localhost", user = "root", passwd = "", database = "harshdb")

mycursor = mydb.cursor()

sql = "Update employee SET sal = 70000 WHERE name = 'ankita'"
mycursor.execute(sql)
mydb.commit()