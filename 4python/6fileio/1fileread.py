file_path='test.txt'

#파일을 읽을때 모드
#r=read, w=write(세로쓰기), a=append(이어서쓰기)
with open(file_path,'r', encoding='utf-8') as file:
    contents=file.read()

print("파일 내용: ",contents)