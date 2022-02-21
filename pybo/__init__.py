from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData

import config  

naming_convention = {
    "ix": 'ix_%(column_0_label)s',
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(column_0_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s"
}

# 전역변수로 객체를 설정함. 그래야 다른 모듈에서도 불러올 수 있음.
db = SQLAlchemy(metadata=MetaData(naming_convention=naming_convention))
migrate = Migrate()


def create_app():
    app = Flask(__name__)
    app.config.from_object(config)


# ORM 객체 초기화 안에서 진행. 
    # db.init_app(app)
    # if app.config['SQLALCHEMY_DATABASE_URI'].startswith("sqlite"):
    #     migrate.init_app(app, db, render_as_batch=True)
    # else:
    #     migrate.init_app(app, db)
    
    db.init_app(app)
    if app.config['SQLALCHEMY_DATABASE_URI'].startswith("sqlite"):
        migrate.init_app(app, db, render_as_batch=True)
    else:
        migrate.init_app(app, db)
        
#   
    from . import models # 모델 가져오기

    from .views import main_views, question_views, answer_views, auth_views, comment_views
    app.register_blueprint(main_views.bp)
    app.register_blueprint(question_views.bp)
    app.register_blueprint(answer_views.bp)
    app.register_blueprint(auth_views.bp)
    app.register_blueprint(comment_views.bp)

# 필터
    from .filter import format_datetime
    app.jinja_env.filters['datetime'] = format_datetime
    
    return app