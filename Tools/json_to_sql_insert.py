import json

with open('dataset.json') as json_file:  
    
	data = json.load(json_file)
    file = open('insertions.sql','w')
    
	for p in data['json_array']:
		#where p is a json object
        
		file.write('INSERT IGNORE INTO table_name VALUES (' + p['attr1'] + ', "' + p['attr2'] + '");\n')
		#p['attr3'].replace('"', '""') #escape "" in strings