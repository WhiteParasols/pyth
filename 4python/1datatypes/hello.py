print("hello");

str='Hello, World!'
str2=' hi, Hello, world welcome!  '

print(str.lower())
print(str.upper())
print(str.capitalize())
print(str2.title()) #문장의 단어 단어마다 대문자로
print(str2.strip()) #앞뒤 불필요한 공백 제거
print(str2.lstrip()) #왼쪽 불필요한 공백 제거
print(str2.rstrip()) #오른쪽 불필요한 공백 제거
print(str.split())#문장을 단어 단위로 짜른다
print(str2.split())#문장을 단어 단위로 짜른다

words=str2.split()
print(words[0])
print(words[2])
print(words[0].upper())
print("-".join(words))

print(str.startswith("hello"))
