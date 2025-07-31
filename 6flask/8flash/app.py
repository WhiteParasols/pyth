from flask import Flask, render_template, request, redirect, url_for, session, flash

app = Flask(__name__)
app.secret_key = 'abcd'

users = [
    {'name': 'MyName', 'id': 'user', 'pw': 'password'}
]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'POST':
        user = request.form.get('id')
        password = request.form.get('password')

        user = next((u for u in users if u['id'] == user and u['pw'] == password), None)
        if user:
            session['user'] = user
            flash('로그인 성공')
            return redirect(url_for('user'))
        
        flash('id/pw가 일치하지 않습니다')
        return redirect(url_for('home'))
    
    else:
        if 'user' in session:
            flash('이미 로그인 된 사용자 입니다')
            return redirect(url_for('user'))
        
        return redirect(url_for('home'))

@app.route('/user')
def user():
    if 'user' in session:
        user = session['user']
        return render_template(user.html, name=user['name'])
    
    flash('비정상적인 접근입니다')
    return redirect(url_for('home'))

@app.route('/logout')
def logout():
    if 'user' in session:
        session.pop('user',None)
        flash('정상적으로 로그아웃 되었습니다')
    else:
        flash('이미 로그아웃 되었습니다.')
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)