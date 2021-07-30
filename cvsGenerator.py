import csv

# open the file in the write mode
file = open('myCsv.csv', 'w')

# create the csv writer
writer = csv.writer(file)

# write a row to the csv file
writer.writerow('hello')

# close the file
file.close()