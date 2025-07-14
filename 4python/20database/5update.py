import sqlite3

#db 연결
conn=sqlite3.connect('example.db')

#커서 객체 생성
cur=conn.cursor()

cur.execute('UPDATE users SET age=10 WHERE name="Alice"')
cur.execute('UPDATE users SET age=? WHERE id=?',(50, 1))

#커밋하여 변경사항 저장
conn.commit()

#db연결 종료
conn.close()