from sqlalchemy.orm import backref
from pybo import db

'''
    1. 하나의 클래스가 하나의 테이블 속성을 의미함.
'''

'''
    # execute flask shell
        >>> flask shell
        >>> from pybo.models import Question, Answer
        >>> from datetime import datetime
        >>> q = Question(subject='what is pybo?', content='I want to know pybo.', create_date=datetime.now())
        >>> from pybo import db
        >>> db.session.add(q)
        >>> db.session.commit()

    # data search by query in flask shell
        >>> Question.query.all()
            [<Question 1>, <Question 2>]
        >>> Question.query.all()
            [<Question 1>, <Question 2>]
        >>> Question.query.filter(Question.id==1).all()
            [<Question 1>]
        >>> Question.query.get(1)
            <Question 1>
        >>> Question.query.filter(Question.subject.like('%플라스크%')).all()
            [<Question 2>]

    # data modifying in flask shell
        >>> q = Question.query.get(2)
        >>> q
            <Question 2>
        >>> q.subject = 'Flask Model Question'
        >>> db.session.commit()

    # data delete in flask shell
        >>> q = Question.query.get(1)
        >>> q         
            <Question 1>
        >>> db.session.delete(q)
        >>> db.session.commit()
        >>> Question.query.all()
            [<Question 2>]
'''

# 질문 모델
class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text(), nullable=False)
    create_date = db.Column(db.DateTime(), nullable=False)

# 답변 모델
class Answer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question_id = db.Column(db.Integer, db.ForeignKey('question.id', ondelete='CASCADE'))

    # backref로 역참조
    # 'all, delete=orphan'으로 연계된 모든 답글(참조하는 모델 내용) 삭제 설정
    question = db.relationship('Question', backref=db.backref('answer_set', cascade='all, delete-orphan'))

    content = db.Column(db.Text(), nullable=False)
    create_date = db.Column(db.DateTime(), nullable=False)