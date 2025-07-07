class Car:
    def __init__(self,make,model):
        self._make=make
        self.model=model
        self._odometer=0 #주행거리

    def get_name(self):
        long_name=f'{self._make}{self._model}'
        return long_name.title()

    def read_odometer(self):
        print(f'이 차의 주행거리는 {self._odometer}km')

    def update_odometer(self, mileage):
        if self._odometer<mileage:
            self._odometer=mileage
        else:
            print('주행거리는 속일수 없습니다!!')

    def increment_odometer(self,distance):
        self._odometer+=distance
        