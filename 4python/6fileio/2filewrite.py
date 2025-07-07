file_path='test.txt'

#파일을 읽을때 모드
#r=read, w=write(세로쓰기), a=append(이어서쓰기)
with open(file_path,'w', encoding='utf-8') as file:
    file.write('hello\n') # \n 뉴라인 - 줄바꿈
    file.write('안녕ㅎ')

