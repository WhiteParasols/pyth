from person import Person

class Driver(Person):
    def __init__(self, name, age,license_type,car=None):
        super().__init__(name, age)
        self._license_type=license_type
        self._car=car
    
    def assign_car(self,car):
        self._car=car
        print(f'{self.name}이 {self._car.get_name()} 소유')

    def drive(self,distance):
        if self._car:
            print(f'{self.name}은 {self._car.get_name()}의 운전을 시작합니다')
            self._car.increment_odometer(distance)
            self._car.read_odometer()
        else:
            print(f"{self.name} 은 소유한 차가 없습니다.")