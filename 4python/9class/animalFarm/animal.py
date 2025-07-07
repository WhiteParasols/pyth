class Animal:
    def __init__(self, name: str):
        self._name: str = name
        self._energy: int = 100


    def feed(self, food: str) -> None:
        self._energy += 50
        print(f"{self._name} 은 {food} 를 먹었습니다. 잔여 에너지: {self._energy}")