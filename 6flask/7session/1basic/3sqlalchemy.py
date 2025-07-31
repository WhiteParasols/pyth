#pip install flask-sqlalchemy

from flask import Flask, session
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = 'my-secret-key' #세션 암호화를 위한 키(내가 관리하고, 내가 암호화 복호화 하고 -> 외부 노출하면 안됨)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sessions.db'
db = SQLAlchemy(app)

app.config['SESSION_TYPE'] = 'sqlalchemy'
app.config['SESSION_SQLALCHEMY'] = db

Session(app)

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
