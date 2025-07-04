#pip install bs4

import requests
from bs4 import BeautifulSoup

response=requests.get('http://makemyproject.net')
print(response)
print(response.status_code)
print(response.text)

#여기 위에는 그냥 문자열
#여기 아래는 문자 파싱해서 DOM의 형태로 자료구조 갖춤

#html 파싱
soup=BeautifulSoup(response.text,"html.parser")
print(soup)
head=soup.find('head')
print("헤드 Dom:", head)

body=soup.find('body')
print("바디 Dom:", body)

bodytext=body.text.strip()
print("바디 내용만:", bodytext)

