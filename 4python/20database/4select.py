import sqlite3

#db 연결
conn=sqlite3.connect('example.db')

#커서 객체 생성
cur=conn.cursor()

#데이터 조회
cur.execute('select * from users')

#결과 가져오기 - 모든 행 다 가져오기 fetchall()
rows=cur.fetchall()
for row in rows:
    print(row)

cur.execute('select * from users')

print('-'*10)
rows=cur.fetchone()
print(rows)

cur.execute('select * from users')
rows=cur.fetchone()[0]
print(rows)


#커밋하여 변경사항 저장
conn.commit()

#db연결 종료
conn.close()