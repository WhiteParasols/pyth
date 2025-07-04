try:
    result =1/0
    print(result)

except ZeroDivisionError:
    print('오류가 났음')

#글자를 숫자로 바꾸기
#python은 함수 설명을 안에다
def convert_to_int(num_str):
    '''글자를 숫자로 변환 <-- docstring 

    Args: 
        num_str(string):

    Returns:
        result:변환된 숫자값, 변환에 실해하면 none
    '''
    try:
        return int(num_str)
    except:
        print('입력값',num_str)
        result = None
    
    return result

def double_number(num):
    return num*2

user_input="A"
result=convert_to_int(user_input)
if result:
    result=double_number(result)
result=double_number(convert_to_int(user_input))
print(f'입력한 숫자: {user_input} 두배값 {result}')