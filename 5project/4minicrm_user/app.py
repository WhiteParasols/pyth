from flask import Flask, render_template, request
import database as db

app = Flask(__name__)

@app.route('/')
def index():
    page = request.args.get('page', default=1, type=int)
    items_per_page = 10 # 10개, 20개, 50개, ...
    
    # 전체 유저수 가져오기
    user_count = db.get_user_count()
    total_pages = user_count // items_per_page   # 사용자 수가 나눠서 딱 떨어지지 않으면?? 사용자가 1004명이었음
    
    # users = db.get_users()  # 전체 유저 다가져오기
    users = db.get_users_per_page(page, items_per_page)  # 페이지 수만큼 유저 가져오기
    
    return render_template('index.html', users=users, total_pages=total_pages)

if __name__ == "__main__":
    app.run(debug=True)