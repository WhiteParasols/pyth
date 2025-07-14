from flask import Flask, render_template, redirect, request
import sqlite3

app = Flask(__name__)

def db_connection():
    conn = sqlite3.connect('users.db')
    conn.row_factory = sqlite3.Row
    return conn


# 테이블 생성함수 작성하시오.
def create_table():
    conn =  db_connection()
    cur = conn.cursor()
    
    cur.execute('''CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, age INTEGER NOT NULL)''')
    
    conn.commit()
    conn.close()

create_table()

@app.route('/', methods=['GET', 'POST'])
def index():
    conn = db_connection()
    
    if request.method == 'POST':
        name = request.form['name']
        age = int(request.form['age'])
        conn.execute('INSERT INTO users (name, age) VALUES (?, ?)', (name, age))
        conn.commit()
        conn.close()
        return redirect('/')
    
    users = conn.execute('SELECT * FROM users').fetchall()
    conn.close()
    return render_template('index.html', users=users)

@app.route('/delete/<int:user_id>')
def delete_user(user_id):
    conn = db_connection()
    conn.execute('DELETE FROM users WHERE id = ?', (user_id,))
    conn.commit()
    conn.close()
    return redirect('/')

@app.route('/update/<int:user_id>', methods=['GET', 'POST'])
def update_user(user_id):
    conn = db_connection()

    if request.method == 'POST':
        name = request.form['name']
        age = int(request.form['age'])
        conn.execute('UPDATE users SET name = ?, age = ? WHERE id = ?', (name, age, user_id))
        conn.commit()
        conn.close()
        return redirect('/')
    
    user = conn.execute('SELECT * FROM users WHERE id = ?', (user_id,)).fetchone()
    conn.close()

    if user is None:
        return "User not found", 404

    return render_template('update_user.html', user=user)

if __name__ == '__main__':
    app.run(debug=True)
