from flask import Flask, render_template, request, redirect, url_for
from flask import session

app = Flask(__name__)
app.secret_key = 'sesac'

users = [
    {'name': 'MyName', 'id': 'user', 'pw': 'password'}
]

items = [
    {'id': 'prod-001', 'name': '사과', 'price': 3000},
    {'id': 'prod-002', 'name': '딸기', 'price': 2000},
    {'id': 'prod-003', 'name': '오렌지', 'price': 2500},
    {'id': 'prod-004', 'name': '바나나', 'price': 1000},
]

@app.route('/')
def home():
    user = session.get('user')
    return render_template('index.html', user=user)

@app.route('/user')
def user():
    user = session.get('user')
    if user:
        return render_template('user.html', user=user)
    else:
        return redirect(url_for('login'))  # 어디로 보낼지, 뭐라고 출력할지, 내맘임..

@app.route('/login', methods=["GET"])
def login():
    return render_template('login.html')

@app.route('/login', methods=["POST"])
def login_submit():
    input_id = request.form.get('id')
    input_pw = request.form.get('password')
    
    user = next((u for u in users if u['id'] == input_id and u['pw'] == input_pw), None)
    if user: # 성공
        session['user'] = user  # 사용자 정보를 모두다 저장함.
        return redirect(url_for("user"))
    else: # 실패
        return render_template('login.html', error="ID 또는 비밀번호가 올바르지 않습니다.")

@app.route('/logout')
def logout():
    session.pop('user', None)  # user가 없으면 KeyError 가 날 수 있음.. 그래서 없을때 None 반환..
    return redirect(url_for('home'))

@app.route('/product')
def product():
    user = session.get('user')
    return render_template('product.html', user=user, items=items)

@app.route('/add-to-cart/<item_id>')
def add_to_cart(item_id):
    if 'cart' not in session:
        session['cart'] = []

    session['cart'].append(item_id)
    session.modified = True  # Required to update session
    return redirect(url_for('product'))

@app.route('/cart')
def view_cart():
    cart = session.get('cart', {})
    cart_items = []

    for item in items:
        if item['id'] in cart:
            item_copy = item.copy()
            item_copy['quantity'] = cart[item['id']]
            item_copy['total_price'] = item_copy['price'] * item_copy['quantity']
            cart_items.append(item_copy)

    return render_template('cart.html', cart_items=cart_items)



if __name__ == "__main__":
    app.run(debug=True)