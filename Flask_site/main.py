from flask import Flask, render_template, request
import json_to_database

app = Flask(__name__)
json_to_database.start_database()
country_names = json_to_database.get_country_names()
global_cases_deaths = json_to_database.select_global_cases_and_deaths()
continent_cases_deaths = json_to_database.select_continent_cases_and_deaths()


@app.route('/')
@app.route('/home')
def home():
	result = json_to_database.select_all_countries()

	return render_template(
		'home.html',
		rlt = result,
		cntr_nms = country_names,
		gl_cs_dths = global_cases_deaths,
		cnt_cs_dths = continent_cases_deaths
	)


@app.route('/about')
def about():
	return render_template('about.html')


@app.route('/result', methods=['POST'])
def result():
	if request.form['date1'] and request.form['date2']:
		result = json_to_database.select_a_country_between_dates(request.form['country'], request.form['date1'], request.form['date2'],)
	else:
		result = json_to_database.select_a_country(request.form['country'])

	result2 = json_to_database.select_cases_and_deaths_per_country(request.form['country'])


	return render_template(
		'home.html',
		rlt = result,
		rlt2 = result2,
		cntr_nms = country_names,
		gl_cs_dths = global_cases_deaths,
		cnt_cs_dths = continent_cases_deaths
	)


@app.route('/result2', methods=['POST'])
def result2():
	result3 = json_to_database.select_the_n_most_countries_cases(request.form['topN'])

	return render_template(
		'home.html',
		rlt3 = result3,
		cntr_nms = country_names,
		gl_cs_dths = global_cases_deaths,
		cnt_cs_dths = continent_cases_deaths
	)

if(__name__ == '__main__'):
	app.run(debug=True)
