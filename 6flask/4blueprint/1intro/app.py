from flask import Flask, request, render_template, redirect, url_for
from user_routes import user_bp
from admin_routes import admin_bp

app = Flask(__name__)

app.register_blueprint(user_bp, url_prefix="/user")
app.register_blueprint(admin_bp, url_prefix="/admin")

@app.route('/')
def home():
    return render_template('index.html')

if __name__=='__main__':
    app.run(debug=True)