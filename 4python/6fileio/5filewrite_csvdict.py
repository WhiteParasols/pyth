#csv 파일

import csv
file_path ='test.csv'

data=[
    {'name':'john','age':25,'city':'seoul'},
    {'name':'jane','age':30,'city':'busan'},
    {'name':'bob','age':35,'city':'jeju'},
]

print(data)
for person in data:
    print(person)
    for key,value in person.items():
        #print(f'key: {key}, value: {value}')
        print(f'사람의 이름은 {person['name']} 나이는 {person['age']}')

with open(file_path,'w',newline='') as file:
    headers=['name','age','city'] #headers=data[0].keys()
    csv_writer=csv.DictWriter(file, fieldnames=headers)
    csv_writer.writeheader()
    csv_writer.writerows(data)

