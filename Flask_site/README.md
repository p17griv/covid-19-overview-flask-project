### Database Schema
![Database Schema](https://github.com/IonianIronist/internetTech/blob/master/Flask_site/db_scema2.png)

### Steps:

1. Install python dependencies
	- pip3 install Flask
	- pip3 install mysql-connector
	- pip3 install requests

2. Create a user account in your mysql server with:
	- username: user1
	- password: user1
	- host name (local): localhost
	- all data & structure rights
	
Or change the 'host', 'user' and 'passwd' arguments in 
'create_database.py' and 'json_to_database.py' files to match your 
server credentials.

3. Start your mysql server.

4. Run the 'main.py' with
	- python3 main.py //It takes a while the first time...
	
	Possible fix --> wrap multiple inserts in 1 transactions

5. Open site with your browser using the following address:
	
	http://127.0.0.1:5000/