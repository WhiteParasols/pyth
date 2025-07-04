#pip install requests 외부(pypi.org) 라이브러리 설치
#pip uninstall requests
#가상환경에 설치됨

import requests

response=requests.get("http://makemyproject.net")
print(response)
print(response.status_code)
print(response.text)