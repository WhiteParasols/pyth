from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)

users = [
    {'name': 'aaa', 'id': 'aaa', 'pw': 'aaa'},
    {'name': 'bbb', 'id': 'bbb', 'pw': 'bbb'},
    {'name': 'ccc', 'id': 'ccc', 'pw': 'ccc'},
]

@app.route("/")
def home():
    return render_template("index2.html")

@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        id = request.form['id']
        pw = request.form['password']

        user = None
        for u in users:
            if (u['id'] == id) & (u['pw'] == pw):
                user = u
                break
        if user:
            error= None
        else:
            error='incorrect id or password'
        return render_template('index2.html', user=user, error=error)
        
    return render_template("login.html")

@app.route("/user")
@app.route("/user/<user>")
def user(user=None): #초기값 할당
        return render_template("user.html", user=user)

@app.route("/product")
def product():
        return render_template("product.html")

if __name__ == "__main__":
    app.run(debug=True, port=5000)