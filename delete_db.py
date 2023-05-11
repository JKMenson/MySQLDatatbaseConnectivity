import  mysql.connector
mydb = mysql.connector.connect(host = "localhost", user = "root", passwd = "", database = "harshdb")

mycursor = mydb.cursor()

sql = "Delete from employee WHERE name = 'harshit'"
mycursor.execute(sql)
mydb.commit()