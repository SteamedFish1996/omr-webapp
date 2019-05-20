# -*- coding:utf-8 -*-
"""上传文件视图层

处理上传文件的URL，提供视图
"""

__author__ = 'zzy'

from flask import Blueprint, render_template, redirect, request, url_for, jsonify, Response, make_response,  send_from_directory

from www import app
from cv2 import cv2
import os
from werkzeug.utils import secure_filename
from flask import jsonify

upload = Blueprint('upload',__name__)


def allowed_file(filename):
    return '.' in filename and  filename.rsplit('.', 1)[1] in app.config['ALLOWED_EXTENSIONS']


@upload.route('/', methods=['POST', 'GET'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        if not (f and allowed_file(f.filename)):
             return jsonify({"status": 1001, "msg": "Please check the type of uploaded image, only pdf and png are allowed"})
        upload_path = os.path.join(app.config['UPLOAD_FOLDER'],secure_filename(f.filename))  #注意：没有的文件夹一定要先创建，不然会提示没有该路径
        f.save(upload_path)
        basepath = os.path.dirname(__file__)  # 当前文件所在路径
        img = cv2.imread(upload_path)
        cv2.imwrite(os.path.join(basepath, 'static/images', 'test.jpg'), img)
        return jsonify({"status": 200, "msg": "upload success","newpng":"IMSLP00747.png","mp3":"","xml":""})
    elif request.method=='GET':
        basepath = os.path.dirname(__file__) 
        directory = os.path.join(basepath, 'static/result')
        filename = 'results.zip'
        response = make_response(send_from_directory(directory, filename, as_attachment=True))
        response.headers["Content-Disposition"] = "attachment; filename={}".format(filename.encode().decode('latin-1'))
        return response 
 
@upload.route('/results', methods=['POST', 'GET'])
def results():
    from omr.shell import Shell
    python27_dir = 'python'
    testfile_dir = '--vesion'
    cmd = python27_dir + ' ' + testfile_dir
    print(cmd)
    shell = Shell()
    returncode, sout, serr, pid = shell.run_cmd(cmd)
    results = shell.cmd_result_list(sout)
    for l in results:
        print(l)
    
    return "success"

if __name__ == '__main__':
    app.run(debug=True)