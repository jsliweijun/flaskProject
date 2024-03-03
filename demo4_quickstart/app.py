from flask import Flask

app = Flask(__name__) #  WSGI 应用

# WSGI（Web Server Gateway Interface）是一种规范. web服务器 与 Pythony web 应用 之间的接口规范。
#  请求 -》 web 服务器 -》（environ ，start_response ） Python web 应用

@app.route('/')
def hello_world():
    return 'Hello World!'

#  当前app.py 就能启动 flask 应用了， 没有执行的 app.run()