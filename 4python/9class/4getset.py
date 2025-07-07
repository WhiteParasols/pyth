class Person:
    # 초중급 에서도 필수
    def __init__(self, name, age):
        self.__name = name  # 속성 (Attribute) - __ 밑줄 두개는 private 속성이라서, 클래서 밖에서 접근 불가
        self.__age = age   # 속성 (Attribute)
    
    @property      # 이 함수는 getter 입니다.
    def name(self):
        return self.__name
    
    @name.setter   # 이 함수는 setter 입니다.
    def name(self, name):
        self.__name = name
        
    @property
    def age(self):
        return self.__age
    
    @age.setter
    def age(self, age):
        if age >= 0:
            self.__age = age
        else:
            print("나이는 0보다 커야 합니다.")
    
    def greet(self):   # 메소드 (Method - 객체 함수)
        print(f"안녕하세요, 저는 {self.__name} 입니다.")

    def ride_car(self):  # 메소드 (Method - 객체 함수)
        print(f"자동차를 탑니다")

person1 = Person("김철수", 30)
person2 = Person("홍길동", 25)

print(person1.name)  # setter/getter 를 파이썬 신버전에서 decorator로 지정을 했으면, 함수가 아닌 변수처럼 쉽게 접근할수 있음

print(person1.age)

person1.name = "박철수"
person1.age = 35

print(person1.age)

person1.age = -10
