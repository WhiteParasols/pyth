from typing import Optional
from person import Person
from car import Car

class Driver(Person):
    def __init__(self, name: str, age: int, license_type: str, car: Optional[Car] = None) -> None:
        super().__init__(name, age)
        self._license_type: str = license_type
        self._car: Optional[Car] = car # Car or None
        
    def assign_car(self, car: Car) -> None:
        self._car = car
        print(f"{self.name} 이 {self._car.get_name()} 을 소유하였습니다.")
        
    def drive(self, distance: int) -> None:
        if self._car:
            print(f"{self.name} 은 {self._car.get_name()} 의 운전을 시작합니다.")
            self._car.increment_odometer(distance)
            self._car.read_odometer()
        else:
            print(f"{self.name} 은 소유한 차가 없습니다.")