class Person:
    def __init__(self,name,age):
        self._name=name
        self._age=age

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self,name):
        self._name=name

    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self,age):
        if age>=0:
            self._age=age
        else:
            print('나이는 0보다 커야 합니다')

    def greet(self):
        print(f'나의 이름은 {self.name}, 나이는 {self.age}')