import mysql.connector

def create_db():
	try:
		mydb = mysql.connector.connect(
		  host="localhost",
		  user="user1",
		  passwd="user1"
		)
	except mysql.connector.Error as err:
		if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
			print("Something is wrong with your user name or password")
		else:
			print(err)

	mycursor = mydb.cursor()

	mycursor.execute("CREATE DATABASE IF NOT EXISTS maindatabase")
	
if __name__ == '__main__':
    create_db()
