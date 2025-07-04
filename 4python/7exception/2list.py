numbers=[1,2,3,4,5]

first_value=None
last_value=None

try:
    first_value=numbers[0]
    last_value=numbers[5]
except IndexError:
    print('숫자 잘못 참조')


