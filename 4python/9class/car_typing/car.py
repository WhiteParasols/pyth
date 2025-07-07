class Car:
    def __init__(self, make: str, model: str) -> None:
        self._make: str = make
        self._model: str = model
        self._odometer: int = 0  # 주행거리
    
    def get_name(self) -> str:
        long_name = f"{self._make} {self._model}"
        return long_name.title()   # 문자열에서 각 단어의 첫번째 글자를 대문자화
    
    def read_odometer(self) -> None:
        print(f"이 차의 주행거리는 현재 {self._odometer} km 입니다.")
        
    def update_odometer(self, mileage: int) -> None:
        if self._odometer < mileage:
            self._odometer = mileage
        else:
            print("주행거리를 속일수 없습니다!!")
    
    def increment_odometer(self, distance):
        self._odometer += distance
        