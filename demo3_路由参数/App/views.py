# 写路由和试图函数
from flask import Blueprint

# 蓝图
blue = Blueprint('user', __name__)


@blue.route('/')
def index():
    return 'index'


# 参数类型
# string
#  <class 'str'>
# @blue.route('/string/<string:name>/')
# 简写 不用指定类型 @blue.route('/string/<:name>/')
@blue.route('/string/<string:name>/')
def hello_name(name):
    print(type(name))
    return name


# int ，接收 整型，但是返回时必须字符串
@blue.route('/int/<int:age>/')
def hello_age(age):
    print(type(age))  # <class 'int'>
    return str(age)
