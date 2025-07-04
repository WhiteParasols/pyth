try:
    with open('hello.txt','r') as file:
        contents=file.read()

    print('file content: ',contents)
except FileNotFoundError:
    print('파일 존재X')
except IOError:
    print('알수없음..')
except:
    print('알수없음..')