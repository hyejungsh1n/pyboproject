from flask import Blueprint, url_for
from werkzeug.utils import redirect

bp = Blueprint('main', __name__, url_prefix='/')


@bp.route('/hello')
def hello_pybo():
    return 'Hello, Pybo!'

@bp.route('/')
def index():
    return redirect(url_for('question._list'))

# question._list  : question은 등록된 블루프린트이름
# _list는 블루프린트에 등록된 함수명
# 즉 저렇게 쓰면 _list함수로 가는 건데 거기에 라우트가  '/list'로 설정 되어
# 저 함수는 5050/question/list/에서 호출 됨.




