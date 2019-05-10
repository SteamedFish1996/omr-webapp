# -*- coding: utf-8 -*-

'''
Configuration
'''
__author__ = 'zzy'

#MySQL 配置文件
SECRET_KEY = 'hard to guess'#一个字符串，密码。也可以是其他如加密过的

#在此登录的是root用户，要填上密码如password，MySQL默认端口是3306。并填上创建的数据库名如youcaihua
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:password@127.0.0.1:3306/omr'

#设置下方这行code后，在每次请求结束后会自动提交数据库中的变动
SQLALCHEMY_COMMIT_ON_TEARDOWN = True
SQLALCHEMY_TRACK_MODIFICATIONS = True