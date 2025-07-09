import random

class AddressGenerator:
    # def __init__(self):
        # self.cities = ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Philadelphia']
        
    def __init__(self, file_path):
        self.cities = self.load_data_from_file(file_path)

    def load_data_from_file(self, file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            data = file.read().splitlines() # 한줄에 이름이 하나가 있는 경우
        return data
        
    def generate_address(self):
        city = random.choice(self.cities)
        street_num = random.randint(1, 100)
        return f"{street_num} {city}"