#WAP a program that reads data from a CSV file and prints it to the console
#Let's do this in 3 ways

#Method 1
import csv
with open('Cruz.csv', mode ='r') as file:    
       csvFile = csv.DictReader(file)
       for lines in csvFile:
            print(lines)

#Method 2
#import csv
with open('Cruz.csv', mode ='r')as file:
  csvFile = csv.reader(file)
  for lines in csvFile:
        print(lines)

#Method 3
import pandas
csvFile = pandas.read_csv('Cruz.csv')
print(csvFile)
