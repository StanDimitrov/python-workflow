import csv

with open('employee.csv', 'r') as file_object:
    csv_dict_reader = csv.DictReader(file_object)
    print(csv_dict_reader.fieldnames) # using .fieldnames we take in list containing all the field names
#----------------------------------------------------------------------------------------------------------
# if we don't have any filednames in our file we can pass the heading information in the dict reader with (fieldnames=[...])

    for record in csv_dict_reader:
        print(record['name of employee'], record['basic salary'])