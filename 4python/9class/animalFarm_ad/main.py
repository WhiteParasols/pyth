from cat import Cat
from dog import Dog
from panda import Panda
from farm import Farm

if __name__ == "__main__":
    dog = Dog("Buddy")
    cat = Cat("Kitty")
    panda = Panda("Fuba")
    
    farm = Farm("Sesac")
    farm.add_animal(dog)
    farm.add_animal(cat)
    farm.add_animal(panda)
    
    dog.speak()
    cat.speak()
    panda.speak() 
    
    dog.move()
    cat.move()
    
    # 반복문을 통해서 10번 움직인다.
    # Pythonic (파이썬 스러운~)
    # for _ in range(10):   # 0~9 까지 10번 반복
    #     dog.move()

    # for _ in range(10):
    #     cat.move()
        
    farm.move_all(5)
    farm.speak_all()
    farm.move_all(5)
    farm.speak_all()
    
    farm.feed_all("독사과")
    print('--- GAME OVER ---')