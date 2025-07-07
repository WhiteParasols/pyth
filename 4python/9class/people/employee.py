from person import Person
class Employee(Person):
    def __init__(self, name, age,company):
        super().__init__(name, age)
        self._company=company
    
    def greet(self): #person의 greet대신 나만의 greet로 over-ride
        print(f'{self._company}에서 일하는 {self.name}')

    def work(self):
        print(f'직원 {self.name}은/는 {self._company}에서 일합니다.')