# -*- coding:utf-8 -*-

"""视图层

1、注册所有视图层蓝图
参数url_prefix='/xxx'的意思是设置request.url中的url前缀，
即当request.url是以/admin或者/user的情况下才会通过注册的蓝图的视图方法处理请求并返回
2、处理未登录用户的URL，提供视图
"""
__author__ = 'zzy'


from www import app
from www.views_admin import admin
from www.views_user import user
from www.views_upload import upload

from flask import redirect, url_for, render_template ,request

#app注册蓝图
app.register_blueprint(admin, url_prefix='/admin')
app.register_blueprint(user, url_prefix='/user')
app.register_blueprint(upload, url_prefix='/upload')

@app.route('/')
def index():
    return redirect(url_for('upload.upload_file'))

@app.route('/hello')
def hello():
    return 'Hello World'

@app.route('/omr')
def omr():
    return "omr"


@app.route('/signin', methods=['GET'])
def signin_form():
    return '''<form action="/signin" method="post">
              <p><input name="username"></p>
              <p><input name="password" type="password"></p>
              <p><button type="submit">Sign In</button></p>
              </form>'''

@app.route('/signin', methods=['POST'])
def signin():
    # 需要从request对象读取表单内容：
    if request.form['username']=='admin' and request.form['password']=='password':
        return '<h3>Hello, admin!</h3>'
    return '<h3>Bad username or password.</h3>'

