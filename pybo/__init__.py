from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

import config  

# 전역변수로 객체를 설정함. 그래야 다른 모듈에서도 불러올 수 있음.
db = SQLAlchemy()
migrate = Migrate()


def create_app():
    app = Flask(__name__)
    app.config.from_object(config)


# ORM 객체 초기화 안에서 진행. 
    db.init_app(app)
    migrate.init_app(app, db)
#   
    from . import models # 모델 가져오기

    from .views import main_views, question_views, answer_views
    app.register_blueprint(main_views.bp)
    app.register_blueprint(question_views.bp)
    app.register_blueprint(answer_views.bp)

# 필터
    from .filter import format_datetime
    app.jinja_env.filters['datetime'] = format_datetime
    
    return app