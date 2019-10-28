from flask import Blueprint,render_template,request,jsonify,make_response,redirect,session
from util.myutil import islogin
from flask_login import login_user,logout_user,UserMixin,login_required
# from util.flask_login_user import User
from database.db import session
from database.tables import Admin,Teachers,Students

# 创建登录用户
class User(UserMixin):
    pass

indexs = Blueprint("indexs",__name__,url_prefix="/",template_folder="templates/index",static_folder="static/indexs")

# # flask-http验证
# from flask_httpauth import HTTPBasicAuth



@indexs.route('/')
@login_required  #
# @islogin
def index():
    return render_template("index/index.html")



@indexs.route('/login',methods=["GET","POST"])
def login():
    if request.method == "GET":
        return render_template('index/login.html')
    elif request.method == "POST":
        username = request.form['username']
        password = request.form['password']
        type = request.form['type']
        if type == '0':
            #教师
            pass
        elif type == '1':
            #学生
            pass
        elif type == '2':
            # 管理员
            user1 = session.query(Admin).filter(Admin.username == username).one()
            if user1:
                if user1.password == password:
                    user = User()
                    user.id = username
                    login_user(user)
                    return jsonify({'code': 200, 'status': 'yes', 'msg': '管理员登录成功'})
                else:
                    return jsonify({'code': 200, 'status': 'no', 'msg': '密码错误'})
        # 比对数据库
        return jsonify({'code':200,'status':'no','msg':'用户不存在'})

@indexs.route('/loginout')
def loginout():
    # print(session.get("username"))
    # session.pop('username')
    logout_user()
    return redirect("/login")