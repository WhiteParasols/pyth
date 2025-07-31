#pip install flask-session

from flask import Flask, session
from flask_session import Session
import os

app = Flask(__name__)
app.secret_key = 'abcd1234' #아무거나 무방

app.config['SESSION_TYPE'] = 'filesystem' #그 이외에 filesystem / redis / mongodb 등등

app.config['SESSION_FILE_DIR'] = os.path.join(os.getcwd(),'my_sessions')
app.config['SESSION_PERMANENT'] = False #False면 브라우저가 닫히면 삭제
app.config['SESSION_USE_SIGNER'] = True #세션 쿠키에 서명 사용 여부

Session(app) #세션기능 추가

@app.route('/set-session/<username>')
def set_session(username):
    session['username'] = username
    return '세션 저장'

@app.route('/get-session')
def get_session():
    if 'username' in session:
        return f"세션정보: {session['username']}"
    else:
        return f"저장된 정보 없음"
    
@app.route('/clear-session')
def del_session():
    session.pop('username',None) #세션에서 값 삭제
    return f'세션 정보 삭제'
    
if __name__=='__main__':
    app.run(debug=True)

