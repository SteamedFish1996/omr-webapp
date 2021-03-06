# -*- coding:utf-8 -*-
"""模型层

固化数据，为数据库的创建和操作提供模板
"""
__author__ = 'zzy'

from www import db


class User(db.Model):
    """用户表

    映射数据库中的user表

    Attributes:
        __tablename__：数据库中的表名
        id：
        email：
        password：
    """
    __tablename__ = 'users' #数据库中的表名
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(320), unique=True)
    password = db.Column(db.String(32), nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username


class Admin(db.Model):
    __tablename__ = 'admins'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(320), unique=True)
    password = db.Column(db.String(32), nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username


if __name__ == '__main__':
# 1.在数据库中根据上面的模型创建表
    db.create_all()
"""
# 2.增加记录
admin = User(username='admin', email='admin@example.com')
guest = User(username='guest', email='guest@example.com')
db.session.add(admin)
db.session.add(guest)
db.session.commit()

#3.查询记录,注意查询返回对象，如果查询不到返回None
User.query.all() #查询所有
User.query.filter_by(username='admin').first()#条件查询
User.query.order_by(User.username).all()#排序查询
User.query.limit(1).all()#查询1条
User.query.get(id = 1)#精确查询

# 4.删除
user = User.query.get(id = 1)
db.session.delete(user)
db.session.commit()

"""