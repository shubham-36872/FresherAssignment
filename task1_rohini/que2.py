from csv import reader
import logging

logging.basicConfig(filename='que2.log', filemode='w', format='%(asctime)s - %(message)s')
type_service = input("Enter service name(VM/SMS): ")
type_service = type_service.lower()
while True:
	if(type_service == 'vm'):
		type_service = 'VM_SUBPROFILE'
		break
	elif(type_service == 'sms'):
		type_service =  'SMS_SUBPROFILE'
		break
	else:
		print("Invalid input")
		logging.warning('Invalid Input')
		type_service = input("Enter service name(VM/SMS): ").lower()

with open('sample_data.csv', 'r') as read_obj:
	csv_reader = reader(read_obj)
	for row in csv_reader:
		if(row[2] == type_service):
			print(row[0] + ' '+ row[1] + ' ' + row[2] + ' '+ row[3] + ' '+ row[4])
		
	


