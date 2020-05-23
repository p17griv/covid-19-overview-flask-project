import json
import mysql.connector
from mysql.connector import errorcode
from dataset_grabber import download_dataset
import create_database

create_database.create_db()

try:
	mydb = mysql.connector.connect(
		host = "localhost",
		user = "user1",
		passwd = "user1",
		database = "maindatabase")
except mysql.connector.Error as err:
	if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
		print("Something is wrong with your user name or password")
	elif err.errno == errorcode.ER_BAD_DB_ERROR:
		print("Database does not exist")
	else:
		print(err)

if mydb.is_connected():
	print('Connection to database established!')
	mycursor = mydb.cursor()

def start_database():
	mycursor.execute("CREATE TABLE IF NOT EXISTS CountriesPerDay (year VARCHAR(4), month VARCHAR(2), day VARCHAR(2), fulldate DATE, cases INT, deaths INT, country VARCHAR(100), geoId VARCHAR(15), popData2018 BIGINT, continent VARCHAR(50), PRIMARY KEY (fulldate, country))")
	fill_database()

def fill_database():
	download_dataset() #download the dataset

	with open('dataset.json') as json_file:

		data = json.load(json_file)

		total_rows = 0
		rows_cnt = 1
		for p in data['records']:
			total_rows += 1

		print('This might take a while the first time...')
		for p in data['records']:
			#where p is a json object

			print(f'\rInserting to database: {rows_cnt} / {total_rows} rows', end="", flush=True)

			date = p['dateRep'][6:10] + '-' + p['dateRep'][3:5] + '-' + p['dateRep'][0:2] #convert date from dd/mm/yyyy to yyyy-mm-dd
			if p['popData2018']:
				sql = f"INSERT IGNORE INTO CountriesPerDay VALUES ('{p['year']}', '{p['month']}', '{p['day']}', '{date}', {p['cases']}, {p['deaths']}, '{p['countriesAndTerritories']}', '{p['geoId']}', {p['popData2018']}, '{p['continentExp']}' )"
			else:
				sql = f"INSERT IGNORE INTO CountriesPerDay VALUES ('{p['year']}', '{p['month']}', '{p['day']}', '{date}', {p['cases']}, {p['deaths']}, '{p['countriesAndTerritories']}', '{p['geoId']}', NULL, '{p['continentExp']}' )"
			mycursor.execute(sql)

			mydb.commit()

			rows_cnt +=1

		print('\n')

def select_all_countries():
	mycursor.execute("SELECT country, SUM(cases), SUM(deaths) FROM CountriesPerDay GROUP BY country")
	result = mycursor.fetchall()
	return result

def select_a_country(country):
	sql = "SELECT fulldate, country, cases, deaths FROM CountriesPerDay WHERE country = '" + country + "' ORDER BY fulldate"
	mycursor.execute(sql)
	result = mycursor.fetchall()
	return result

def select_a_country_between_dates(country, date1, date2):
	sql = "SELECT fulldate, country, cases, deaths FROM CountriesPerDay WHERE country = '" + country + "' AND fulldate BETWEEN '" + date1 + "' AND '" + date2 + "' ORDER BY fulldate"
	mycursor.execute(sql)
	result = mycursor.fetchall()
	return result

def select_cases_and_deaths_per_country(country):
	sql = "SELECT country, SUM(cases), SUM(deaths) FROM CountriesPerDay WHERE country = '" + country + "'"
	mycursor.execute(sql)
	result = mycursor.fetchall()
	return result

def select_global_cases_and_deaths():
	sql = "SELECT SUM(cases), SUM(deaths) FROM CountriesPerDay"
	mycursor.execute(sql)
	result = mycursor.fetchall()
	return result

def select_continent_cases_and_deaths():
	sql = "SELECT continent, SUM(cases), SUM(deaths) FROM CountriesPerDay GROUP BY continent"
	mycursor.execute(sql)
	result = mycursor.fetchall()
	return result

def select_the_n_most_countries_cases(n):
	sql = "SELECT country, SUM(cases) AS sum_cases, SUM(deaths) FROM CountriesPerDay GROUP BY country ORDER BY sum_cases DESC LIMIT " + n
	mycursor.execute(sql)
	result = mycursor.fetchall()
	return result

def get_total_population(): # NOT WORKING PROPERLY
	sql = "SELECT SUM(popData2018) FROM CountriesPerDay WHERE country IN (SELECT DISTINCT country FROM CountriesPerDay)"
	mycursor.execute(sql)
	result = mycursor.fetchall()
	return result

def get_country_names():
	sql = "SELECT DISTINCT country FROM CountriesPerDay ORDER BY country"
	mycursor.execute(sql)
	result = mycursor.fetchall()
	result_list = []

	for t in result:
		for x in t:
			result_list.append(x.replace('_',' '))

	return result_list
