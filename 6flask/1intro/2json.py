from flask import Flask, jsonify

app = Flask(__name__)

users=[
    {'name':'Alice','age':25,'mobile':'091-1234-3452'},
    {'name':'Bob','age':30,'mobile':'011-1234-3452'},
    {'name':'Charlie','age':27,'mobile':'031-1234-3452'},
]

@app.route('/')
def index():
    return jsonify(users)

@app.route('/user/<name>')
def get_name(name):
    #if 구문 통해 입력받은 name이 실제로 위에 users에 존재하는지 찾아서 user에 할당
    for user in users:
        if(user['name'].upper()==name.upper()):
            return jsonify(user)
        else:
            return jsonify({'error':'User not found'}),404

@app.route('/user/<int:age>')
def get_age(age):
    for user in users:
        if(user['age']==age):
            return jsonify(user)
        else:
            return jsonify({'error':'User not found'}),404
        
    

if __name__=='__main__':
    app.run()