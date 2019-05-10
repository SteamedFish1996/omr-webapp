# -*- coding:utf-8 -*-
"""上传文件视图层

处理上传文件的URL，提供视图
"""
__author__ = 'zzy'

from flask import Blueprint, render_template, redirect, request, url_for
from www import app
import os
from werkzeug.utils import secure_filename

upload = Blueprint('upload',__name__)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in app.config['ALLOWED_EXTENSIONS']

@upload.route('/', methods=['POST', 'GET'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        basepath = os.path.dirname(__file__)  # 当前文件所在路径
        upload_path = os.path.join(app.config['UPLOAD_FOLDER'],secure_filename(f.filename))  #注意：没有的文件夹一定要先创建，不然会提示没有该路径
        f.save(upload_path)
        return redirect(url_for('upload.upload_file'))
    return render_template('upload.html')

if __name__ == '__main__':
    app.run(debug=True)