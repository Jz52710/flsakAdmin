from flask import Blueprint,render_template,request,jsonify
from database.db import session
from database.tables import Classes
from datetime import datetime
classes = Blueprint("classess",__name__,url_prefix="/classess")

@classes.route("/")
def index():
    return render_template("classess/classess.html")

@classes.route("/classess",methods=['GET'])
def classesuri():
    if request.method == "GET":
        cid = request.args.get('id', None)
        if cid:
            pass
        else:
            data = session.query(Classes).all()
            print(data)
            return jsonify({'code': 200, 'msg': 'ok'})

# 添加
@classes.route("/add",methods=['POST'])
def add():
    username = request.form['username']
    if username:
        try:
            now = datetime.now()
            now = now.strftime("%Y-%m-%d %H:%M:%S")
            cls = Classes(username=username,utime=now,ctime=now)
            session.add(cls)
            session.commit()
        except BaseException as e:
            print("数据库异常",e)
            return jsonify({'code': 200, 'status': 'no', 'msg': '数据库异常请稍后重试'})

        return jsonify({'code':200,'status':'yes','msg':'添加成功'})
    else:
        return jsonify({'code':200,'status':'no','msg':'参数不正确'})

# 删除
@classes.route('/del',methods=['delete'])
def dels():
    c = session.query(Classes).filter(Classes.id).first()
    try:
        session.delete(c)
        session.commit()
    except:
        return jsonify({'code':200,'status':'no','msg':'数据库异常，请重试'})
    return jsonify({'code':200,'status':'yes','msg':'提交成功'})


