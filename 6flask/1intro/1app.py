from flask import Flask

app = Flask(__name__)

@app.route('/') #사용자가 /에 접속하면 이 아래 함수 접속
def home():
    return "<h1>hello flask</h1>"

@app.route('/user/<username>') 
def user(username): #위의 flask 데코레이터에서 정한 변수명을 <변수명>으로 함수 인자로 전달
    print(username)
    return f"<h1>hello {username}</h1>" #서버 사이드 렌더링

@app.route('/user/<int:age>') 
def greet_age(age): #위의 flask 데코레이터에서 정한 변수명을 <변수명>으로 함수 인자로 전달
    return f"<h1>hello {age}살 아무개님</h1>" #서버 사이드 렌더링

@app.route('/user/<float:weight>') 
def greet_weight(weight): #위의 flask 데코레이터에서 정한 변수명을 <변수명>으로 함수 인자로 전달
    if weight>60:
        message = '큰'
    elif weight<40:
        message = '작은'
    else:
        message=""
    
    return f"<h1>hello {weight}kg 살 {message}아무개님</h1>" #서버 사이드 렌더링

@app.route('/user/<name>/<int:age>/<float:weight>')
def greet_user(name,age,weight):
    return f"<h1>안녕하세요</h1><h2>사용자정보:</h2><ul><li>이름: {name}</li><li>나이: {age}</li><li>몸무게: {weight}</li></ul>" 

@app.route('/product') 
def product():
    return "<h1>hello product</h1>"

if __name__=='__main__':
    print('여기가 메인함수')
    app.run(debug=True) #절대로 이대로 커밋하면 안됨!! 꼭 false로 두고 commit