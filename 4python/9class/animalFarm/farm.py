from typing import List
from animal import Animal

class Farm:
    def __init__(self, name):
        self._animals: List[Animal] = []  # 동물들 리스트를 담는곳
        self._name: str = name
        
    def add_animal(self, animal: Animal) -> None:
        self._animals.append(animal)

    def feed_all(self) -> None:
        print("동물들에게 밥주는중")
        for animal in self._animals:
            animal.feed("독사과")