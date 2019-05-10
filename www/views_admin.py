from flask import Blueprint,render_template, request

admin = Blueprint('admin',__name__)

@admin.route('/index')
def index():
    return render_template('admin/index.html')

@admin.route('/add')
def add():
    return 'admin_add'

@admin.route('/show')
def show():
    return 'admin_show'