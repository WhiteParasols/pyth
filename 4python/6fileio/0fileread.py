file_path='file.txt'
file = open(file_path,'r') #file을 file descriptor라고 부름

content=file.read()

file.close()

#파일을 연다