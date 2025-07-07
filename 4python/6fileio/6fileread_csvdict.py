#csv 파일

import csv
file_path ='test.csv'

data=[]

with open(file_path,'r') as file:
    csv_reader=csv.DictReader(file)
    for row in csv_reader:
        print(row)
        data.append(row)

print(data)