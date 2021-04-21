import csv

with open('employee.csv', 'r') as file_object:
    csv_reader = csv.reader(file_object)
    line_number = 0

    for records in csv_reader:
        if line_number == 0:
            print(f'Rec no {records[0]:10}, {records[1]:20}, {records[2]:10}, {records[3]:20}')
            print('-' * 70)
        else:
            print(records[0])