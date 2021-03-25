from csv import reader

service = raw_input("Enter Service: ")
service = service.upper()


if service == 'VM':
    service = 'VM_SUBPROFILE'
elif service == 'SMS':
    service = 'SMS_SUBPROFILE'
else:
    print ("Invalid Input")
    service = raw_input("Enter Service: ")
    service = service.upper()
with open('sample_csv.csv', 'r') as read_obj:
    csv_reader = reader(read_obj)
    for row in csv_reader:
        if row[3] == service:
            print(row[0] + ' ' + row[2] + ' ' + row[3] + ' ' + row[4])