from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def index():
    return render_template('form.html')

@app.route('/submit',methods=['POST'])
def submit():
    # name = request.args.get('name') #Get 파라미터(argument)
    name = request.form.get('name') #post로 form이 전달된 것 안에서 name이 키 인것을 주시오
    age = request.form.get('age') 

    print(request.form)
    return f'{name}! {age}살'

if __name__ == '__main__':
    app.run(debug=True)