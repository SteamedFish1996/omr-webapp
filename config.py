# -*- coding: utf-8 -*-

'''配置文件

flack框架的配置文件，所有的参数在www的init.py中写入app
eg：调用app[SECRET_KEY] 返回字符串'hard to guess'
'''
__author__ = 'zzy'

# MySQL 配置文件
SECRET_KEY = 'hard to guess'    # 一个字符串，密码。也可以是其他如加密过的
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:password@127.0.0.1:3306/omr'    # 在此登录的是root用户，密码password，MySQL端口是3306。数据库名omr
#SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:root@59.77.7.58:3306/omr'    # 在此登录的是root用户，密码password，MySQL端口是3306。数据库名omr
# 设置下方这行code后，在每次请求结束后会自动提交数据库中的变动
SQLALCHEMY_COMMIT_ON_TEARDOWN = True
SQLALCHEMY_TRACK_MODIFICATIONS = True

# 文件上传路径
UPLOAD_FOLDER = './data/uploads'
#ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])
ALLOWED_EXTENSIONS = set(['pdf', 'png'])