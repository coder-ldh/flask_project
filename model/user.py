from app import db

class SX_User(db.Model):
    __tablename__ = 'sx_user'
    id = db.Column(db.Integer, primary_key=True)
    login_name = db.Column(db.String(255),unique=False)
    mobile = db.Column(db.String(255), unique=True)
    email = db.Column(db.String(255),unique=False)

    #重写该方法，方便输出user信息
    def __repr__(self):
        user = ''
        user += 'login_name: %s\n' % (self.login_name)
        user += 'mobile: %s\n' % (self.mobile)
        user += 'email: %s\n' % (self.email)
        return user

def create_user(login_name, mobile, email):
    user = SX_User( login_name=login_name, mobile=mobile, email=email)
    db.session.add(user)
    try:
        db.session.commit()
    except BaseException:
        return 0
    else:
        return user.id

def select_list():
    users = db.session.query(SX_User).all()
    try:
        db.session.commit()
    except BaseException:
        return 0
    else:
        return users