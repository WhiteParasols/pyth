import sqlite3

DATABASE = 'user-sample.db'

def get_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    #미션 1)여기 DB로부터 가져온 내용을 dict로 하고 싶으면?
    return conn

def get_stores():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM stores")
    stores = cursor.fetchall()
    conn.close()
    
    stores = [dict(r) for r in stores]

    #미션 1-2)튜플형의 데이터를 dict형으로 변환(conn.row_factory = sqlite3.Row 안 했을 때)
    # stores=[dict(r) for r in stores]
    # stores_dict = [{'id':s[0], 'name':s[1],}]
    return stores
 
def get_stores_by_name(name):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM stores WHERE Name LIKE ?", ('%' + name + '%', ))
    stores = cursor.fetchall()
    conn.close()
    
    stores = [dict(r) for r in stores]
    
    return stores