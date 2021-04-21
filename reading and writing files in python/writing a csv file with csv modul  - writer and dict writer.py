import csv

employees = [
    ['E001', 'John Rambo', '7000.0', 'Sales'],
    ['E002', 'Tina Munim', '6575.0', 'Production'],
    ['E003', 'James Smith', '9875.2', 'Design']

]

with open('emp1.csv', 'w', newline='') as file_object: # with newline = '' we will print our result without new line with its own
    csv_writer = csv.writer(file_object, delimiter=',', quotechar='"',quoting=csv.QUOTE_MINIMAL)
    for i in employees:
        csv_writer.writerow(i) # this method will automatically adding new line after each list