# -*- coding: utf-8 -*-

'''项目启动入口

'''
__author__ = 'zzy'


from www import app
app.debug = True    #交互式调试器 WARNING: Do not use the development server in a production environment.
app.run(host='0.0.0.0')