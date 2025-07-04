def square_root(number):
    if(number<0):
        return None
    return number **0.5

def square_root2(number):
    if(number<0):
        raise ValueError('음수의 제곱근은 계산 불가')
    return number **0.5

print(square_root(25))
print(square_root2(-1))

try:
    print(square_root2(-25))
except ValueError as e:
    print(e)