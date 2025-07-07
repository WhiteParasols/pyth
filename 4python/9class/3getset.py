class Person:
    # 초중급 에서도 필수
    def __init__(self, name, age):
        self.__name = name  # 속성 (Attribute) - __ 밑줄 두개는 private 속성이라서, 클래서 밖에서 접근 불가
        self.__age = age   # 속성 (Attribute)
    
    def get_name(self):
        return self.__name
    
    def set_name(self, name):
        self.__name = name
        
    def get_age(self):
        return self.__age
    
    def set_age(self, age):
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

print(person1.get_name())
person1.set_name("박철수")
print(person1.get_name())
print(f"나이는 {person1.get_age()} 입니다")
person1.set_age(-10)
print(f"나이는 {person1.get_age()} 입니다")

