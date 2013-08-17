# add_pk_to_csv.py
#
# Inserts a primary key field in given CSV file, in prep for conversion
# of the CSV file to a JSON fixture
#
# Execute this script manually BEFORE executing csv2json.py
#
# To run script...
# python add_pk_to_csv.py

import csv

# define order of fields in output file
fieldnames = ['pk', 'vsn', 'trim_id','vehicle_year', 'make', 'vehicle_model', 'trim_name']

with open('car_data.csv', 'rb') as csvinput:
    with open('testdata.csv', 'wb') as csvoutput:
        csvwriter = csv.DictWriter(csvoutput, fieldnames, delimiter=',')
        csvwriter.writeheader()
        pkcount = 0
        for row in csv.DictReader(csvinput):
            pkcount +=1
            row['pk'] = '%s' % pkcount  # add 'pk' entry to row data
            csvwriter.writerow(row)