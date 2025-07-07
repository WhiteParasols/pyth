from flask import Flask, render_template

app=Flask(__name__)

@app.route('/')
def home():
    users = ['Alice','Bob','Charlie','David','Eve']
    return render_template('index.html',names=users) #이때 이 파일은 무조건 templates 파일 안에 있다.

if __name__=='__main__':
    app.run(debug=True)