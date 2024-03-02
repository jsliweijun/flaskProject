# 写路由和试图函数
from flask import Blueprint

# 蓝图
blue = Blueprint('user', __name__)


@blue.route('/')
def index():
    return 'index'
