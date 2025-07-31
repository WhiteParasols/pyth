def named1(**kwargs):
    print(kwargs)
def named2(name ,age):
    print(name, age)

details = {'name':'bob','age':25}

named1(**details)
named1(name='bob', age=25)
named2(**details)
named2(name='bob', age=25)