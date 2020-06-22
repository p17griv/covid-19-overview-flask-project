import json
import mysql.connector
import time
from mysql.connector import errorcode
from dataset_grabber import download_dataset
import create_database
from operator import itemgetter

create_database.create_db()  # Create database

try:
    mydb = mysql.connector.connect(
        host="localhost",
        user="user1",
        passwd="user1",
        database="maindatabase")
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


def start_database():  # Create table and fill it
    mycursor.execute(
        "CREATE TABLE IF NOT EXISTS CountriesPerDay (year VARCHAR(4), month VARCHAR(2), day VARCHAR(2), fulldate DATE, cases INT, deaths INT, country VARCHAR(100), geoId VARCHAR(15), popData2018 BIGINT, continent VARCHAR(50), PRIMARY KEY (fulldate, country))")
    fill_database()


def fill_database():  # Download dataset, parse and fill table
    download_dataset()  # Download the dataset

    with open('dataset.json') as json_file:

        data = json.load(json_file)

        dataset_rows = 0
        rows_inserted = 1
        for p in data['records']:
            dataset_rows += 1  # Count the items/records (json objects) of the dataset

        print('This might take a while the first time...')
        start = time.time()
        for p in data['records']:  # For each item in the dataset

            print(f'\rInserting to database: {rows_inserted} / {dataset_rows} rows', end="", flush=True)

            date = p['dateRep'][6:10] + '-' + p['dateRep'][3:5] + '-' + p['dateRep'][0:2]  # Convert date from dd/mm/yyyy to yyyy-mm-dd
            if p['popData2019']:  # If there are population data for the current country
                sql = f"INSERT IGNORE INTO CountriesPerDay VALUES ('{p['year']}', '{p['month']}', '{p['day']}', '{date}', {p['cases']}, {p['deaths']}, '{p['countriesAndTerritories']}', '{p['geoId']}', {p['popData2019']}, '{p['continentExp']}' )"
            else:  # Insert NULL on 'popData2018'
                sql = f"INSERT IGNORE INTO CountriesPerDay VALUES ('{p['year']}', '{p['month']}', '{p['day']}', '{date}', {p['cases']}, {p['deaths']}, '{p['countriesAndTerritories']}', '{p['geoId']}', NULL, '{p['continentExp']}' )"
            mycursor.execute(sql)

            mydb.commit()

            rows_inserted += 1

        end = time.time() - start
        print('\n\nTime taken: ' + '{:.2f} seconds'.format(end))
        print('\n')


# QUERIES
# Get total cases and deaths per country
def select_all_countries():
    mycursor.execute("SELECT country, SUM(cases), SUM(deaths) FROM CountriesPerDay GROUP BY country")
    result = mycursor.fetchall()
    return result


# Get per day cases and deaths for the 'country' for all available dates
def select_a_country(country):
    sql = "SELECT fulldate, country, cases, deaths FROM CountriesPerDay WHERE country = '" + country + "' ORDER BY fulldate"
    mycursor.execute(sql)
    result = mycursor.fetchall()
    return result


# Get per day cases and deaths for the 'country' between 'date_from' and 'date_to' dates
def select_a_country_between_dates(country, date1, date2):
    sql = "SELECT fulldate, country, cases, deaths FROM CountriesPerDay WHERE country = '" + country + "' AND fulldate BETWEEN '" + date1 + "' AND '" + date2 + "' ORDER BY fulldate"
    mycursor.execute(sql)
    result = mycursor.fetchall()
    return result


# Get total cases and deaths for 'country'
def select_cases_and_deaths_per_country(country):
    sql = "SELECT country, SUM(cases), SUM(deaths) FROM CountriesPerDay WHERE country = '" + country + "'"
    mycursor.execute(sql)
    result = mycursor.fetchall()
    return result


# Get total world cases and deaths
def select_global_cases_and_deaths():
    sql = "SELECT SUM(cases), SUM(deaths) FROM CountriesPerDay"
    mycursor.execute(sql)
    result = mycursor.fetchall()
    result2 = ['{:,}'.format(result[0][0]), '{:,}'.format(result[0][1])]  # add commas to returned numbers

    return result2


# Get total cases and deaths per continent
def select_continent_cases_and_deaths():
    sql = "SELECT continent, SUM(cases), SUM(deaths) FROM CountriesPerDay GROUP BY continent"
    mycursor.execute(sql)
    result = mycursor.fetchall()
    return result


# Get the 'n' countries with most cases
def select_the_n_most_countries_cases(n):
    sql = "SELECT country, SUM(cases) AS sum_cases, SUM(deaths) FROM CountriesPerDay GROUP BY country ORDER BY sum_cases DESC LIMIT " + n
    mycursor.execute(sql)
    result = mycursor.fetchall()
    return result


# Get the 'n' countries with most deaths
def select_the_n_most_countries_deaths(n):
    sql = "SELECT country, SUM(cases), SUM(deaths) AS sum_deaths FROM CountriesPerDay GROUP BY country ORDER BY sum_deaths DESC LIMIT " + n
    mycursor.execute(sql)
    result = mycursor.fetchall()
    return result


# Get the total world population - NOT USED
def get_total_population():  # NOT WORKING PROPERLY - PROBLEM WITH DATA
    sql = "SELECT SUM(popData2018) FROM CountriesPerDay WHERE country IN (SELECT DISTINCT country FROM CountriesPerDay)"
    mycursor.execute(sql)
    result = mycursor.fetchall()
    return result


# Get all country name in data - for the dropdown menu
def get_country_names():
    sql = "SELECT DISTINCT country FROM CountriesPerDay ORDER BY country"
    mycursor.execute(sql)
    result = mycursor.fetchall()
    result_list = []

    for t in result:
        for x in t:
            result_list.append(x)

    return result_list

# Get virus spread percenage per country
def get_spread_percentage():
    sql = "SELECT country, (SUM(cases)*1000)/popData2018 AS spreadPercentage FROM CountriesPerDay WHERE popData2018 IS NOT NULL AND country != 'Cases_on_an_international_conveyance_Japan' GROUP BY country"
    mycursor.execute(sql)
    result = mycursor.fetchall()
    return sorted(result, key=itemgetter(1))

