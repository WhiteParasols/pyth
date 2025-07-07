from flask import Flask, render_template, request

app=Flask(__name__)

users=[
    {'name':'Alice','age':25,'mobile':'091-1234-3452'},
    {'name':'Bob','age':30,'mobile':'011-1234-3452'},
    {'name':'Charlie','age':27,'mobile':'031-1234-3452'},
    {'name':'Doe','age':30,'mobile':'031-1234-3452'},
]
#
@app.route('/') #Get 파라미터 요청이 함께 온다
def home():
    name = request.args.get('name')  # Name search
    age = request.args.get('age')    # Age search
    
    filtered_users = users

    if name:
        filtered_users = [user for user in filtered_users if user['name'].upper() == name.upper()]
    
    if age:
        try:
            filtered_users = [user for user in filtered_users if user['age'] == int(age)]
        except:
            filtered_users = [] 

    return render_template('index4.html', users=filtered_users)

if __name__=='__main__':
    app.run(debug=True)