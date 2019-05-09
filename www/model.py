from flack_app import db
#创建模型对象
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

def __repr__(self):
    return '<User %r>' % self.username


if __name__ == '__main__':
# 1.创建表
db.create_all()
"""
# 2.增加记录
admin = User(username='admin', email='admin@example.com')
guest = User(username='guest', email='guest@example.com')
db.session.add(admin)
db.session.add(guest)
db.session.commit()
"""
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