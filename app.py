# -*- coding: <utf-8> -*-

from flask import Flask


# web framework
# web application
# __main__
app = Flask(__name__)
# 设置 secret_key 来使用 flask 自带的 session
# 这个字符串随便你设置什么内容都可  以


"""
在 flask 中，模块化路由的功能由 蓝图（Blueprints）提供
蓝图可以拥有自己的静态资源路径、模板路径（现在还没涉及）
用法如下
"""
# 注册蓝图
# 有一个 url_prefix 可以用来给蓝图中的每个路由加一个前缀
# from routes.board import main as board_routes

# 运行代码
if __name__ == '__main__':
    # debug 模式可以自动加载你对代码的变动, 所以不用重启程序
    # host 参数指定为 '0.0.0.0' 可以让别的机器访问你的代码
    config = dict(
        debug=True,
        host='0.0.0.0',
        port=8000,
    )
    app.run(**config)
    # log('running in 2000')
# 1. 明文储存
# 2. 注册用户 但是 不保留用户
# 3. 我这边登陆以后 那边 也要登陆看看
# 功能如下
# 1. 登陆页面
#      登陆进去有两个功能 1. 成绩查询 2. 课表查询
