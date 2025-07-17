from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

engine = create_engine('sqlite:///users.db')

Base = declarative_base()

# 테이블 설계 - 객체 설계
# 사용자 '모델' 정의

class User(Base):
    __tablename__='users'
    id = Column(Integer, primary_key=True)
    name= Column(String)
    age=Column(Integer)

Base.metadata.create_all(engine) 

# CRUD 함수 만들기--------------------
def create_user(session, name: str, age: int) -> User:
    new_user = User(name=name,age=age)
    session.add(new_user)
    session.commit()

    return new_user

def get_users(session) -> list[User]:
    #아무 인자 안 받아서 사용자 리스트 리턴하기
    users = session.query(User).all()

def get_user_by_id(session, user_id: int) -> User | None:
    #사용자 ID를 받아서 사용자 반환(사용자 없을 수 도)
    # user = session.query(User).filter(id==user_id).first()
    # return user

    return session.get(User,user_id) #SQLAlchemy 2.x버전부터 가능

def update_user_age(session, user_id: int, new_age: int) ->  bool:
    #사용자 아이디와 나이를 받아서 나이 업데이트 하기
    # 그냥 객체에 값만 설정하면 자동으로 쓰임(session.commit()할때)
    u = session.query(User).filter(User.id==user_id).first()
    session.add(u)
    session.commit()

def delete_user_by_id(session, user_id:int) -> bool:
    #사용자 삭제하고 성공하면 True
    user = session.get(User, user_id)
    if not user:
        return False
    
    session.delete(user)
    session.commit()
    return True

def delete_user_by_name(session, name:str) -> bool:
    #사용자 삭제하고 성공하면 True
    users = session.query(User).filter_by(name=name).all()
    if not users: 
        return 0
    for u in users:
        session.delete(u)
    session.commit()
    return len(users)

# CRUD 함수 만들기--------------------

if __name__ == "__main__":
    Session = sessionmaker(bine=engine, expire_on_commit=False)
    with Session() as session:
        # 1)사용자 생성
        alice = create_user(session, 'Alice', 30)
        bob = create_user(session, 'Bob', 25)
        print(f"추가된 사용자 ID:{alice.id},{bob.id}")

        # 2)사용자 조회
        user1=get_user_by_id(session, alice.id)
        print(f"조회한 사용자 정보:{user1.name, user1.age}")
        
        user2=get_user_by_id(session, bob.id)
        print(f"조회한 사용자 정보:{user2.name, user2.age}")

        # 3)정보 수정
        update_alice = update_user_age(session, alice.id, 29)
        print(f"업데이트 성공여부 확인:", update_alice)

        # 4)사용자 모두 조회
        users=get_users(session)
        for u in users:
            print(f'id: {u.id}, name: {u.name}, age:{u.age}')

        # 5)사용자 삭제
        delete_alice=delete_user_by_id(session, alice.id)
        print(f"Alice 삭제 성공여부 확인:", delete_alice)

        del_user_count = delete_user_by_id(session, 'Bob')
        print(f'Bob이라는 사용자 삭제 개수: ', del_user_count)

        # 6)최종 사용자 목록
        users=get_users(session)
        for u in users:
            print(f'id: {u.id}, name: {u.name}, age:{u.age}')