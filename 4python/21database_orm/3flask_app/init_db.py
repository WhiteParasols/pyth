from app import app
from models import db, User

with app.app_context(): #위 flask앱이 초기화가 되면
    db.drop_all() #모든 테이블 삭제
    db.create_all() #새로 초기화

    db.session.add(User(name="Alice", age=30))
    db.session.add(User(name="Bob", age=25))
    db.session.add(User(name="Charlie", age=20))
    db.session.commit()

    for u in User.query.all():
        print(u.id, u.name, u.age)