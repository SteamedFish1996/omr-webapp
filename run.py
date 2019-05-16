# -*- coding: utf-8 -*-

'''项目启动入口

'''
__author__ = 'zzy'

from flask_cors import CORS
from www import app


import os
from omr.shell import Shell
basepath = os.path.dirname(__file__)  # 当前文件所在路径
vue_dir = basepath+'/www/templates/vueweb'
cmd1 = "cd "+vue_dir
cmd2 = 'npm run build'
cmd3 = 'npm run dev'
cmd = cmd1 + ' && ' + cmd2 + ' && ' + cmd3
print('run this command in shell to start vue quickly:')
print(cmd)
print()

CORS(app, supports_credentials=True)
app.debug = True    #交互式调试器 WARNING: Do not use the development server in a production environment.
app.run(host='0.0.0.0')

