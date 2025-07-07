def function_a1():
    print("module_a 의 function_a1 호출")
    function_a2()
        
def function_a2():
    print("module_a 의 function_a2 호출")
    function_a3()
    
def function_a3():
    print("module_a 의 function_a3 호출")
    test_1234()

def test_1234():
    print("module_a 의 text_1234 호출")
    deep_call_1()

def deep_call_1():
    print("module_a 의 deep_call_1 호출")
    raise RuntimeError("의도적으로 발생한 나의 예외")

def call_test():
    print("나(modulea_a) 실행됨")

# call_test()

if __name__ == '__main__':   # 파이썬이 나를 직접 호출했을때 실행되는 것 = 메인 함수
    call_test()