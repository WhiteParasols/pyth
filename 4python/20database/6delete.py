import sqlite3

#db 연결
conn=sqlite3.connect('example.db')

#커서 객체 생성
cur=conn.cursor()

cur.execute('DELETE FROM users WHERE name="Alice"')

cur.execute('DELETE FROM users WHERE name=?',('Bob', )) #인자를 ('Bob') 이렇게만 표현하면 이것이 튜플인지 단일 인자인지 모름

#커밋하여 변경사항 저장
conn.commit()

#db연결 종료
conn.close()