from zipfile import ZipFile

neededFilesList = ('time_series_covid_19_confirmed.csv',
					'time_series_covid_19_deaths.csv',
					'time_series_covid_19_recovered.csv',
					'covid_19_data.csv')

with ZipFile('datasets.zip', 'r') as zipObj:
	# Get a list of all archived file names from the zip
	listOfFileNames = zipObj.namelist()

	# Iterate over the file names
	for fileName in listOfFileNames:
		if fileName in neededFilesList:
			# Extract files from zip
			zipObj.extract(fileName)