class Person:
    def __init__(self,name,age):
        self.name=name #속성(attribute) - 개별 데이터를 저장하는 공간
        self.age=age  

    def __str__(self): # 이 객체를 사람들이 보기 좋게 표현하는 함수
        return f"Person={self.name}, age={self.age}"      
    
    def __eq__(self, other): #나와(이 객체)와 다른 객체 비교할때의 조건
        return self.name==other.name and self.age==other.age


    def greet(self): #메소드(method) - 객체 함수
        print(f'hello {self.name}')

    def ride_car(self):
        print('자동차')

person1=Person('김',30)
person2=Person('이',26)
person3=Person('박',46)

person1.greet()
person1.ride_car()

person2.greet()
person2.ride_car()

print(person1)

print(person1==person2)