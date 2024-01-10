import mysql.connector

mydb = mysql.connector.connect(
	host="localhost",
	user="root",
	password="password",
	database="db_go_dev"
)

mycursor = mydb.cursor()

sql = "Select * FROM tbl_Drivers"

mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
	print(x)
