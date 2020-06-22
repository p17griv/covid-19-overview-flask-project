# Covid-19 Overview

#### Description

'Covid-19 Overview' is a Python Flask student project for "Internet Technologies" course of department of Informatics - Ionian University, made by [Pashalis Grivas](https://github.com/p17griv) and [Nemanja Jevtić](https://github.com/IonianIronist). The main goal of this project is to demonstrate the usage of Flask web framework by building a simple application/website with an interesting topic - Covid-19 virus.

The app fetches "
[COVID-19 cases worldwide](https://data.europa.eu/euodp/en/data/dataset/covid-19-coronavirus-data/resource/ce379c1d-066a-4de8-a195-1d5e8338142a)
" (JSON) dataset with Covid-19 data from [EU Open Data Portal](https://data.europa.eu/euodp/en/home).

----------------------------

#### User is able to:
- watch global total cases and deaths (until current day)
- track total cases and deaths by continent (until current day)
- be informed about total cases and deaths of all countries (until current day)
- track cases and deaths for a specific country between two dates
- compare cases and deaths of two countries between two dates
- see the top N countries with the most cases/deaths for a specific N (until current day)
- watch the virus spread percentage per country (until current day).

###### All options are either visualized with tables or charts or both. 

----------------------

### How to run - Instructions

1. Run ``` git clone (url of the repository) ``` into a directory in order to download the project.
2. Install python dependencies (Install Python 3 if you haven't)
    - ```pip3 install Flask``` (just pip on Windows)
    - ```pip3 install mysql-connector```
    - ```pip3 install requests```
3. Create a user account in your mysql server with: (use xampp with phpadmin or install mysql on your system)
    - username: user1
    - password: user1
    - host name (local): localhost
    - all data & structure rights

    Or change the ```host```, ```user``` and ```passwd``` arguments in 
'create_database.py' and 'json_to_database.py' files to match your 
server credentials.

    ###### Follow the insturctions below of how to create a new user (linux)

4. Start your mysql server. (if you already haven't)
5. Run the 'main.py' with:
    - ```python3 main.py``` command (it takes a while the first time...)
6. Open site with your browser using the following address:
    - http://127.0.0.1:5000/

##### Notes:
- Html date input is not supported in Safari or Internet Explorer 11 (or earlier).
- FIX ERROR (if raised):
    - ```"SELECT list is not in GROUP BY clause and contains nonaggregated column … incompatible with sql_mode=only_full_group_by"```
    
    by running: ```SET GLOBAL sql_mode=(SELECT REPLACE(@@sql_mode,'ONLY_FULL_GROUP_BY',''));``` command on your mysql server.
    
------------------
##### How to create a new user on mysql server - Linux
1. Connect to mysql as root:
    - ```sudo mysql -h localhost -u root```
2. Create user running:
    - mysql> ```CREATE USER 'user1'@'localhost' IDENTIFIED BY 'user1';```
3. If ERROR 1819 (HY000) run:
    - mysql> ```SET GLOBAL validate_password_policy=LOW;```
    
    and run again step 2.
    
    Remember to reset this value after you're done.
4. Give privileges to the user:
    - mysql> ```GRANT ALL PRIVILEGES ON * . * TO 'user1'@'localhost';```
5. Run:
    - mysql> ```FLUSH PRIVILAGES;```
    
    to reload privileges.
6. Log out:
    - mysql> ```quit```
7. Connect as the new user (test):
    - ```mysql -u user1 -p user1```
    
----------------------
#### Database schema

![Image of the database schema](https://github.com/IonianIronist/internetTech/blob/master/db_scema.png)
