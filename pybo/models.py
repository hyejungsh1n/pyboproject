from pybo import db

class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text(), nullable=False)
    create_date = db.Column(db.DateTime(), nullable=False)
    

class Answer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question_id = db.Column(db.Integer, db.ForeignKey('question.id', ondelete='CASCADE'))
    question = db.relationship('Question', backref=db.backref('answer_set'))
    content = db.Column(db.Text(), nullable=False)
    create_date = db.Column(db.DateTime(), nullable=False)

# question_id    
# ondelete에 지정한 값은 삭제 연동 설정.
# 즉, 답변 모델의 question_id 속성은 질문 모델 id와 연결되며, ondelete='CASCADE(종속)'에 의해
# 데이터베이스에 쿼리를 이용하여 질문을 삭제하면 해당 질문에 달린 답변도 삭제.


# question
# 답변모델에서 질문 모델을 참조하기 위해서 사용. 질문모델을 사용하려면 db.relationship 사용
# 답변모델에서 질문모델의 제목을 참조하려면 answer.question.subject 
# backref는 역참조. 질문에서 답변 찾기..(아직 잘 모름)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    
    