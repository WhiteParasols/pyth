import random

class NameGenerator:
    # def __init__(self):
        # self.names = ['John', 'Jane', 'Michael', 'Emily', 'William', 'Olivia']
        # 기존 하드코딩 되어 있던걸, 파일을 통해서 읽는 방식으로 변경해보기
    def __init__(self, file_path):
        self.names = self.load_data_from_file(file_path)

    def load_data_from_file(self, file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            data = file.read().splitlines() # 한줄에 이름이 하나가 있는 경우
        return data

    def generate_name(self):
        return random.choice(self.names)