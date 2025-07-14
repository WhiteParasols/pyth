import sqlite3

#db 연결
conn=sqlite3.connect('example.db')

#커서 객체 생성
cur=conn.cursor()

#커서를 중심으로 db에 입출력을 한다.
cur.execute('''CREATE TABLE IF NOT EXISTS users (id integer primary key autoincrement, name text not null, age integer not null)''')

#커밋하여 변경사항 저장
conn.commit()

#db연결 종료
conn.close()