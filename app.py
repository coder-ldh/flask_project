from flask import Flask

from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)

app.config['JSON_AS_ASCII']=False  #指定json编码格式 如果为False 就不使用ascii编码，
app.config['JSONIFY_MIMETYPE'] ="application/json;charset=utf-8" #指定浏览器渲染的文件类型，和解码格式；

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost:3306/sx'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)

from model.user import select_list

@app.route('/users/<name>')
def hello_world(name):
    return 'Hello %s!' % name

@app.route('/users')
def users():
    users = select_list()
    t= {}
    t['data'] = users
    print(t)
    return '%s' % t

if __name__ == '__main__':
    app.run(debug=True)