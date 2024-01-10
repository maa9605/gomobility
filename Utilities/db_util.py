import mysql.connector

def get_geo_dataset(rSql):

	try:
		mydb = mysql.connector.connect(
		host="localhost",
		user="root",
		password="password",
		database="db_go_dev"
		)

		mycursor = mydb.cursor()
			
		mycursor.execute(rSql)
		
		myresult = mycursor.fetchall()
		
		return myresult
	
	except mysql.connector.Error as error:
		print("Fail {}",error)
	
	finally:
		if mydb.is_connected():
			mycursor.close()
			mydb.close()

def get_dataset(rSql, Vals):

	try:
		mydb = mysql.connector.connect(
		host="localhost",
		user="root",
		password="password",
		database="db_go_dev"
		)

		mycursor = mydb.cursor()
			
		mycursor.execute(rSql, (Vals,))
		
		myresult = mycursor.fetchall()
		
		return myresult
	
	except mysql.connector.Error as error:
		print("Fail {}",error)
	
	finally:
		if mydb.is_connected():
			mycursor.close()
			mydb.close()

def insert_record(rSql, Vals):

	try:
		mydb = mysql.connector.connect(
		host="localhost",
		user="root",
		password="password",
		database="db_go_dev"
		)

		mycursor = mydb.cursor()
		
		mycursor.execute(rSql, Vals)
			
		mydb.commit()	
			
		return mycursor.lastrowid
		
	except mysql.connector.Error as error:
		print("Fail {}",error)
	
	finally:
		if mydb.is_connected():
			mycursor.close()
			mydb.close()
	
def update_record(rSql, Vals):

	try:
		mydb = mysql.connector.connect(
		host="localhost",
		user="root",
		password="password",
		database="db_go_dev"
		)

		mycursor = mydb.cursor()
		
		mycursor.execute(rSql, Vals)
			
		mydb.commit()
	
	except mysql.connector.Error as error:
		print("Fail {}",error)
	
	finally:
		if mydb.is_connected():
			mycursor.close()
			mydb.close()
				

	
