from person import Person
from student import Student
from employee import Employee

Alice=Person('Alice',23)
Bob=Person('Bob',22)
tom=Student('tom',20,'123456')
charlie=Employee('charlie', 30, 'samsung')

Alice.greet()
Bob.name='BOB'
Bob.greet()

tom.greet()
tom.study()

charlie.greet()
charlie.work()