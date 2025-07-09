import sys
from generators.user_generator import UserGenerator

class DisplayData(UserGenerator):
    def print_console(self, count):
        data = self.generate_user(count)
        for name, birthdate, gender, address in data:
            print(f"Name: {name}\nBirthdate: {birthdate}\nGender: {gender}\nAddress: {address}\n")

    def print_csv(self, count):
        data = self.generate_user(count)
        # data 를 가지고 csv에 저장한다
        print(f"CSV 파일에 저장 완료")

# 최종 실행
print(sys.argv)  # 입력 인자
# sys.argv[0] # 여기는 실행 파일명 자신
# sys.argv[1] # 첫번째 인자

if len(sys.argv) > 1: 
    num_data = int(sys.argv[1])
else:
    num_data = int(input("원하는 데이터 갯수를 입력하시오: "))

output_format = 'console'
if len(sys.argv) > 2:
    output_format = sys.argv[2]

my_data = DisplayData()
if output_format == 'console':
    my_data.print_console(num_data)
elif output_format == 'csv':
    my_data.print_csv(num_data)
else:
    print("지원되지 않는 출력 형태입니다.")