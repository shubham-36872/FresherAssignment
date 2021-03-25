import csv
import logging

logging.basicConfig(filename='que3.log', filemode='w', format='%(asctime)s - %(message)s')

#Reading data from output_data.csv  file
f = open('output_data.csv')
csv_f = csv.reader(f)   
data = []

for row in csv_f: 
	data.append(row)
f.close()
length = len(data)

#Function to convert data in xml format
def convert_row(row):
	return """
   <auditSubscribers>
      <MSISDN>%s</MSISDN>
      <OperationType>%s</OperationType>
      <ServiceIndication>%s</ServiceIndication>
   </auditSubscribers>
""" %(row[0], row[1], row[2])

	
#Program to take input from user
while True:
	n = int(input("Enter batch limiting size: \n"))
	if(n > length):
		print("Input size is greater than data present in CSV file")
		logging.warning('Input size is greater than data present in CSV file')
	else:
		#Writting data to xml file
		with open('output.xml', 'w') as f:
			f.write("<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n")
			f.write("<Audit xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xsi:noNamespaceSchemaLocation=\"schema.xsd\">")
			f.write('\n'.join([convert_row(row) for row in data[:n]]))
			f.write("</Audit>")
		break

