from cat import Cat
from dog import Dog
from farm import Farm

if __name__ == "__main__":
    dog = Dog("Buddy")
    cat = Cat("Kitty")
    
    farm = Farm("Sesac")
    farm.add_animal(dog)
    farm.add_animal(cat)
    
    dog.speak()
    cat.speak()
    
    dog.move()
    cat.move()
    
    # 반복문을 통해서 10번 움직인다.
    # Pythonic (파이썬 스러운~)
    for _ in range(10):   # 0~9 까지 10번 반복
        dog.move()

    for _ in range(10):
        cat.move()
        
    # animals = [dog, cat]
    # for _ in range(10):
    #     for animal in animals:
    #         animal.move()
    
    farm.feed_all()