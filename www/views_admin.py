# -*- coding:utf-8 -*-
"""管理员视图层

处理来自管理员的URL，提供视图
"""
__author__ = 'zzy'

from flask import Blueprint, render_template, redirect, request, url_for
from www.models import Admin
from www import db

admin = Blueprint('admin',__name__)

@admin.route('/')
def index():
    return redirect(url_for('user.show'))
    #return 'admin_index.html'

@admin.route('/add/',methods=['POST','GET'])
def add():
    if request.method == 'POST':
        p_admin = request.form.get('username',None)
        p_email = request.form.get('email',None)
        p_password = request.form.get('password',None)

        if not p_admin or not p_email or not p_password:
            return 'input error'

        newobj = Admin(username=p_admin, email=p_email, password=p_password)
        db.session.add(newobj)
        db.session.commit()
    admins = Admin.query.all()
    return render_template('admin_add.html',admins=admins)

@admin.route('/show')
def show():
    return 'admin_show'