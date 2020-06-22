from flask import Flask, render_template, request
import json_to_database

app = Flask(__name__)
json_to_database.start_database()  # Create table - fetch dataset - parse data and insert to table
country_names = json_to_database.get_country_names()  # Get all country name in data - for the dropdown menu
global_cases_deaths = json_to_database.select_global_cases_and_deaths()  # Get total world cases and deaths


@app.route('/')
@app.route('/home')  # Gets called when home page is requested
def home():
    result = json_to_database.select_all_countries()  # Get total cases and deaths per country

    return render_template(
        'home.html',
        rlt=result,
        cntr_nms=country_names,
        gl_cs_dths=global_cases_deaths
    )


@app.route('/result', methods=['POST'])  # Called when form is submitted
def result():
    country = request.form['country']  # Get the selected country from the form
    date_from = request.form['date1']  # Get the given 'from date' from the form
    date_to = request.form['date2']  # Get the given 'to date' from the form

    if date_from > date_to:  # If user gives a from date that's after to date
        # swap dates
        temp = date_from
        date_from = date_to
        date_to = temp

    if date_from and date_to:  # If both (from and to) dates were given from the user
        # Get per day cases and deaths for the 'country' between 'date_from' and 'date_to' dates
        result = json_to_database.select_a_country_between_dates(country, date_from, date_to, )
    else:  # User selected only a country
        # Get per day cases and deaths for the 'country' for all available dates
        result = json_to_database.select_a_country(country)

    result2 = json_to_database.select_cases_and_deaths_per_country(country)  # Get total cases and deaths for 'country'

    return render_template(
        'home.html',
        rlt4=result,
        rlt2=result2,
        cntr_nms=country_names,
        gl_cs_dths=global_cases_deaths,
        d_from=date_from,
        d_to=date_to,
    )


@app.route('/result2', methods=['POST'])  # Called when form is submitted
def result2():
    n = request.form['topNCases']  # Get the selected number of countries from the form
    result3 = json_to_database.select_the_n_most_countries_cases(n)  # Get the 'n' countries with most cases

    return render_template(
        'home.html',
        rlt3=result3,
        cntr_nms=country_names,
        gl_cs_dths=global_cases_deaths,
        number=n
    )


@app.route('/result3', methods=['POST'])  # Called when form is submitted
def result3():
    n = request.form['topNDeaths']  # Get the selected number of countries from the form
    result3 = json_to_database.select_the_n_most_countries_deaths(n)  # Get the 'n' countries with most deaths

    return render_template(
        'home.html',
        rlt3=result3,
        cntr_nms=country_names,
        gl_cs_dths=global_cases_deaths,
        number=n
    )


@app.route('/result4')  # Called when form is submitted
def result4():
    # Get total cases and deaths per continent
    continent_cases_deaths = json_to_database.select_continent_cases_and_deaths()

    return render_template(
        'home.html',
        cntr_nms=country_names,
        gl_cs_dths=global_cases_deaths,
        cnt_cs_dths=continent_cases_deaths
    )


@app.route('/result5', methods=['POST']) # Called when form is submitted
def result5():
    # Get the spread percentage per country
    spread_percentages = json_to_database.get_spread_percentage()

    return render_template(
        'home.html',
        cntr_nms=country_names,
        gl_cs_dths=global_cases_deaths,
        rlt5=spread_percentages
    )


@app.route('/result6', methods=['POST'])  # Called when form is submitted
def result6():
    country1 = request.form['country1']  # Get the first selected country from the form
    country2 = request.form['country2']  # Get the second selected country from the form
    date_from = request.form['date1']  # Get the given 'from date' from the form
    date_to = request.form['date2']  # Get the given 'to date' from the form

    if date_from > date_to:  # If user gives a from date that's after to date
        # swap dates
        temp = date_from
        date_from = date_to
        date_to = temp

    if date_from and date_to:  # If both (from and to) dates were given from the user
        # Get per day cases and deaths for the 'country1' and 'country2' between 'date_from' and 'date_to' dates
        result = json_to_database.select_a_country_between_dates(country1, date_from, date_to, )
        result1 = json_to_database.select_a_country_between_dates(country2, date_from, date_to, )
    else:  # User selected only the two countries
        # Get per day cases and deaths for the 'country1' and 'country2' for all available dates
        result = json_to_database.select_a_country(country1)
        result1 = json_to_database.select_a_country(country2)

    # Concatenate the 2 lists of tuples to one list of tuples
    result_list = []
    for t in result:  # for each tuple in 'result' list
        for t1 in result1:  # for each tuple in 'result1' list
            if t[0] == t1[0]:  # if fist items of tuples 't' and 't1' are equal - if dates are equal
                result_list.append(t + t1)  # add to 'result_list' list the concatenation of the two tuples

    result2 = json_to_database.select_cases_and_deaths_per_country(country1)  # Get total cases and deaths for 'country1'
    result3 = json_to_database.select_cases_and_deaths_per_country(country2)  # Get total cases and deaths for 'country2'

    return render_template(
        'home.html',
        rlt_con=result_list,
        rlt2=result2,
        rlt3=result3,
        cntr_nms=country_names,
        gl_cs_dths=global_cases_deaths,
        d_from=date_from,
        d_to=date_to,
    )


if __name__ == '__main__':
    app.run()
# app.run(debug=True)  # run in debug mode to auto-restart server on code changes
