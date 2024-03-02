
# 启动引用， 他要执行 App 下的代码

from App import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)