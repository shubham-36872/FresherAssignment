from csv import reader
import csv
li1 = ['mobile number']
li2 = list()
with open('sample_data.csv', 'r') as read_obj:
	csv_reader = reader(read_obj)
	for row in csv_reader:
		if(row[0] not in li1):
			print(row[0] + ' ' + row[1] + ' ' + row[2])
			li1.append(row[0])
			li2.append(row)
			

#writing output to csv file		
with open('output_data.csv', 'w', newline="") as file:
	writer = csv.writer(file, quoting = csv.QUOTE_ALL, delimiter = ',')
	writer.writerows(li2)
	


