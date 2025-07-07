class Person:
    def __init__(self,name:str,age:int)->None:
        self._name:str=name
        self._age:int=age

    @property
    def name(self)->str:
        return self._name
    
    @name.setter
    def name(self,name:str):
        self._name=name

    @property
    def age(self)->int:
        return self._age
    
    @age.setter
    def age(self,age:int) -> None:
        if age>=0:
            self._age=age
        else:
            print('나이는 0보다 커야 합니다')

    def greet(self):
        print(f'나의 이름은 {self.name}, 나이는 {self.age}')