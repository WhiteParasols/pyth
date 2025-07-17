# pip install flask-sqlalchemy

from flask import Flask, render_template, request, redirect
from models import db, User

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///example.db'
db.init_app(app)


#테이블 생성(초기화)
# with app.app_context():
#     db.create_all()

#     new_user = User(name='Alice', age=30)
#     db.session.add(new_user)
#     db.session.commit()

#     users = User.query.all()
#     for u in users:
#         print(u.id, u.name, u.age)

@app.route('/')
def index():
    users=User.query.all()
    return render_template('index.html',users=users)

@app.route('/add',methods=["POST"])
def add_user():
    name = request.form.get('name')
    age = int(request.form.get('age'))

    #필요한 error check
    new_user = User(name=name, age=age)
    db.session.add(new_user)
    db.session.commit()
    return redirect('/')

@app.route('/delete/<int:id>')
def delete_user(id):
    user = db.session.get(User, id)
    if user:
        db.session.delete(user)
        db.session.commit()
    else:
        print('사용자 없음', id)

    return redirect('/')

@app.route('/edit', methods=['POST'])
def edit(id):
    user = db.session.get(User, id)
    


if __name__ == '__main__':
    app.run(debug=True)