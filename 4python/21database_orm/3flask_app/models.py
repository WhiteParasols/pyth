from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

#사용자 모델 정의 
class User(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String)
    age = db.Column(db.Integer)

    #객체를 print로 출력할때의 포멧 정의하는 함수
    def __repr__(self):
        return f'출력<User {self.id} {self.name} {self.age}>'
    def __str__(self):
        return f'문자열변환<User {self.id} {self.name} {self.age}>'