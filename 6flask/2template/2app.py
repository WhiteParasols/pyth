from flask import Flask, render_template

app=Flask(__name__)

users=[
    {'name':'Alice','age':25,'mobile':'091-1234-3452'},
    {'name':'Bob','age':30,'mobile':'011-1234-3452'},
    {'name':'Charlie','age':27,'mobile':'031-1234-3452'},
]

@app.route('/')
def home():
    return render_template('index2.html',users=users) #이때 이 파일은 무조건 templates 파일 안에 있다.

if __name__=='__main__':
    app.run(debug=True)