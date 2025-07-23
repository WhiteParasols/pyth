import sqlite3

DATABASE = 'user-sample.db'

def get_connection():
    conn = sqlite3.connect(DATABASE)
    # 미션1-1. 여기 DB로부터 가져온 내용을 dict로 하고 싶으면??
    conn.row_factory = sqlite3.Row
    return conn

# ---- 유저(user) -----
def get_user_count():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM users")
    user_count = cursor.fetchone()[0]
    conn.close()
    return user_count
    
def get_users():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    conn.close()
    users = [dict(r) for r in users]
    return users

def get_users_per_page(page, count):
    offset_pos = (page - 1) * count
    print(f"페이지:{page}, 오프셋:{offset_pos}")
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users LIMIT ? OFFSET ?", (count, offset_pos))
    users = cursor.fetchall()
    conn.close()
    users = [dict(r) for r in users]
    return users
    
# ---- 상점(store) -----
def get_stores():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM stores")
    stores = cursor.fetchall()
    conn.close()
    stores = [dict(r) for r in stores]
    return stores

def get_stores_by_name(name):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM stores WHERE Name LIKE ?", ('%' + name + '%', ))
    stores = cursor.fetchall()
    conn.close()
    stores = [dict(r) for r in stores]
    return stores