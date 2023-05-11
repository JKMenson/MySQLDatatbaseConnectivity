import  mysql.connector
mydb = mysql.connector.connect(host = "localhost", user = "root", passwd = "", database = "harshdb")

mycursor = mydb.cursor()

# mycursor.execute("Create table employee(name varchar(255), sal int (20))")
mycursor.execute("Show tables")
for table in mycursor:
    print(table)