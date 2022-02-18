from datetime import datetime

from flask import Blueprint, url_for, request, render_template
from werkzeug.utils import redirect

from pybo import db
from ..forms import AnswerForm
from pybo.models import Question, Answer

bp = Blueprint('answer', __name__, url_prefix='/answer')

# question_detil.html에서 method를 post로 지정했으니 여기 또한 그래야 함. 아니면 오류 남
@bp.route('/create/<int:question_id>', methods=('POST', ))
def create(question_id):
    form = AnswerForm()
    question = Question.query.get_or_404(question_id)
    if form.validate_on_submit():
        content = request.form['content'] #post폼 방식으로 전송된 항목 중 name속성이 content
        answer = Answer(content=content, create_date=datetime.now())
        question.answer_set.append(answer) # question.answer_set 질문에 달린 답변들 
        db.session.commit()
        return redirect(url_for('question.detail', question_id=question_id))
    return render_template('question/question_detail.html', question=question, form=form)

# request객체는 플라스크에서 생성 과정 없이 사용할 수 있는 기본 객체.
# 플라스크는 브라우저의 요청부터 응답까지의 처리 구간에서 request 객체를 사용하
# 해주고 이것을 이용해 브라우저에서 요청한 정보를 확인할 수 있음. 

