#csv 파일

import csv
file_path ='test.csv'

data=[
    ['name','age','city'],
    ['john',25,'seoul'],
    ['jane',30,'busan'],
    ['bob',35,'jeju'],
]

print(data)
for i in range(len(data)):
    print(data[i])

with open(file_path,'w',newline='') as file:
    csv_writer=csv.writer(file)
    csv_writer.writerows(data)
    csv_writer.writerow(['Alice',40,'suwon'])

