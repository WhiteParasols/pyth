from animal import Animal

class Cat(Animal):
    # def __init__(self, name):
    #     super.__init__(name)
        
    def speak(self) -> None:
        print(f"{self._name} 는 Meow~ 라고 합니다")
    
    def move(self) -> None:
        if self._energy > 0:
            self._energy -= 5
            print(f"{self._name} 은 걷고 있습니다. 잔여 에너지: {self._energy}")
        else:
            print(f"{self._name} 은 에너지가 다 소진되어 움직일수 없습니다.")