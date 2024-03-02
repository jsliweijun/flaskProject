from flask import Flask
from .views import blue


def create_app():
    app = Flask(__name__)

    # 注册蓝图 ， 使用蓝图管理路由
    app.register_blueprint(blueprint=blue)

    return app
