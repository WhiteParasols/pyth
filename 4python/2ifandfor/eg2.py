users=[
    {"name":"Alice","age":25,"location":"Seoul","car":"BMW"},
    {"name":"Bod","age":44,"location":"Tennessee","car":"Volkswagen"},
    {"name":"Charlie","age":65,"location":"York","car":"Mercedes"},
]

def fine_user(name):
    for u in users:
        if u['name']==name:
            return u
        
print(fine_user('Alice'))

def fine_user2(name,age):
    for u in users:
        if u['name']==name and u['age']==age:
            return u