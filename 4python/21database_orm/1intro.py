#pip install sqlalchemy
from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.orm import declarative_base, sessionmaker

engine = create_engine('sqlite:///example.db') #상대경로로 설정하면 기본 디렉토리는 instance라는 폴더에
# engine = create_engine('sqlite:///tmp/example.db') #절대경로 /tmp/example.db
# engine = create_engine('sqlite:///./example.db') #절대경로 ./example.db(현재디렉터리)

#베이스 클래스를 만들어서 객체랑 db와 연결
Base =  declarative_base()

class User(Base):
    __tablename__ = 'users' #옵션) db table 명을 지정해 주고 싶을 때
    id= Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)

#db에게 테이블 생성하라고 시킴
Base.metadata.create_all(engine)

#세션을 통해서 실제 db와 CRUD를 함
Session = sessionmaker(bind=engine)
session = Session()

#insert into users(name, age) values('Alice',30)
new_user = User(name="Alice", age=30)
session.add(new_user)
session.commit()

#select * FROM users
users= session.query(User).all()
print(users)
for user in users:
    print(user.id, user.name, user.age)