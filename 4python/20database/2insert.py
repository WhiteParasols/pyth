import sqlite3

#db 연결
conn=sqlite3.connect('example.db')

#커서 객체 생성
cur=conn.cursor()

#데이터 삽입
cur.execute('''
    INSERT INTO users (name, age) VALUES ('Alice', 30)
''')
cur.execute('''
    INSERT INTO users (name, age) VALUES ('Bob', 25)
''')

# ? = placeholder
# sql injection 막는 패턴
cur.execute('''
    INSERT INTO users (name, age) VALUES (?, ?)
''',('charlie',40))

#커밋하여 변경사항 저장
conn.commit()

#db연결 종료
conn.close()