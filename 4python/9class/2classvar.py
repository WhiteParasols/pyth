class Person:
    # 클래스 변수 (공통, 공용, 영역에 해당함)
    # count =0 
    # _count: protected / __count:private
    _count =0

    def __init__(self,name,age):
        self.name=name #속성(attribute) - 개별 데이터를 저장하는 공간
        self.age=age  
        Person._count += 1 # 클래스 변수에 접근해서 1을 증가

    def greet(self): #메소드(method) - 객체 함수
        print(f'hello {self.name}')

    def ride_car(self):
        print('자동차')

    # getter, setter 내부 변수에 저장해서 값을 읽어올때는 getter를 사용하고 get_name()
    # 내부 변수에 세팅 할 때는 set_name()

    @classmethod #데코레이터 - 나의 함수에 기능을 더해주는 것.
    def get_count(cls): #클래스 자체에 접근하기 위해 cls라는 클래스 자신을 칭하는 변수를 받아옴
        return cls._count
    # def set_count(cls,count):
    #     cls.count =count;

person1=Person('김철수',30) # 객체를 찍어내는 과정 = 실체화 = instantiation
print(f'만들어진 사람수:{person1.get_count()}')

person2=Person('이',26)
print(f'만들어진 사람수:{person1.get_count()}')
print(f'만들어진 사람수:{person2.get_count()}')

# person2.get_count() = 5 이렇게 못함
# print(f'만들어진 사람수:{person1.__count}')
# print(f'만들어진 사람수:{person2.__count}')

person3 = Person('아무개',35)
print(f'만들어진 사람수:{person1.get_count()}')

# person1={
#     'name':"김철수",
#     'age':30,
#     '__class__': Person,
#     '__dict__': {'name':'김철수, 'age':30}
# }
# print(person1.name)
# print(person1.age)
# print(person1.__class__)
# print(person1.__dict__)