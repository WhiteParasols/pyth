import random 

names=['john','jane','michael','emily','william','olivia']
cities=['New York','Los Angeles','Chicago','Houston','Philadelphia']

def generate_name():
    return random.choice(names)

def generate_birthdate():
    year=random.randint(1990,2010)
    month=random.randint(1,12)
    day=random.randint(1,28)
    return f'{year}--{month:02d}--{day:02d}'

def generate_gender():
    return random.choice(['male','female'])

def generate_address():
    city=random.choice(cities)
    street_num=random.randint(1,100)
    return f'{street_num} {city}'

users=[]
for _ in range(100):
    name = generate_name()
    bday = generate_birthdate()
    gender = generate_gender()
    address = generate_address()
    
    users.append((name, bday, gender, address))
    
for u in users:
    print(u)