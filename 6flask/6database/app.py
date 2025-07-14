from flask import Flask, render_template, redirect, request

app = Flask(__name__)

# db안쓸때
users=[] #예, [{'id':1 , 'name':'홍길동', 'age':30}]
next_id = 1 # id 자동 증가

@app.route('/',methods=['GET','POST'])
def index():
    global next_id
    if request.method == 'POST':
        #POST 요청 처리하기
        name = request.form['name']
        age = int(request.form['age'])

        #사용자 추가
        users.append({'id':next_id, 'name':name,'age':age})
        next_id += 1 #자동 증가

        return redirect('/') #추가 끝났으면 그 페이지 다시 불러오기
    
    return render_template('index.html',users=users)

@app.route('/delete/<int:user_id>')
def delete_user(user_id):
    global users
    users = [user for user in users if user['id'] != user_id]
    return redirect('/')

@app.route('/update/<int:user_id>', methods=['GET', 'POST'])
def update_user(user_id):
    user = next((u for u in users if u['id'] == user_id), None)
    if not user:
        return "User not found", 404

    if request.method == 'POST':
        user['name'] = request.form['name']
        user['age'] = int(request.form['age'])
        return redirect('/')

    return render_template('update_user.html', user=user)


if __name__ == '__main__':
    app.run(debug=True)