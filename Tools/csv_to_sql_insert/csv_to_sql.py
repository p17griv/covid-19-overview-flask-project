import csv

try:
	csv_file = open("covid_19_data.csv")
	try:
		sql_file = open('insertions.sql','w')
		
		csv_reader = csv.reader(csv_file, delimiter=",")
		lcnt = 0
		for row in csv_reader:
			if lcnt == 0:
				print(f"Column names are {row}\n")
			else:
				sql_file.write('INSERT IGNORE INTO table_name VALUES (' + row[0] + ', "' + row[1] + '", "' + row[2] + '", "' + row[3] + '", "' + row[4] + '", ' + row[5] + ', ' + row[6] + ', ' + row[7] + ');\n')
				#p['attr3'].replace('"', '""') #escape " in strings
			lcnt += 1
		print(f"Processed {lcnt} lines.")
	finally:
		sql_file.close()
finally:
	csv_file.close()    
