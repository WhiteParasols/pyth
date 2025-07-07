from animal import Animal

class Panda(Animal):
    sound = "Pang~"
    
    # def speak(self) -> None:
    #     print(f"{self._name} 는 Pang~Pang~ 이라고 합니다")
        
    def move(self) -> None:
        if self._energy > 0:
            self._energy -= 20
            print(f"{self._name} 은 걷고 있습니다. 잔여 에너지: {self._energy}")
        else:
            print(f"{self._name} 은 에너지가 다 소진되어 움직일수 없습니다.")