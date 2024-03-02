# 导入
from flask import Flask, render_template,jsonify

# Werkzeug==2.2.2  降级使用这个包这个虚拟环境
# from urllib.parse import quote as url_quote

# 以当前文件夹为根目录，主函数
# 创建实例，应用对象
app = Flask(__name__)

# 路由 + 试图函数
@app.route('/')
def hello_world():  # 一定要有返回值
    return 'Hello World!'

# 路由需要加上后面的斜杠 /
@app.route('/test/')
def test():
    # 返回字符串
    # return 'nihao flask'

    #返回模板渲染
    # return render_template('index.html',name="zhangsan")

    # 返回 json 数据， 前后端分离方式

    return jsonify({'name':'zhangsan','age':1811})


if __name__ == '__main__':
    # 启动服务器 ,加上参数开发模式就会热更新
    # host = 0.0.0.0 同局域网都能通过ip访问本服务 ， port ， debug
    app.run(debug=True)
