from flask import Flask
from myblueprints.studentblue import student
from myblueprints.teacherblue import teacher
from myblueprints.indexblue import indexs,User
from myblueprints.classblue import classes
import os
from flask_login import LoginManager,UserMixin
from flask_restful import Api
from myuris.classesuri import Classes,ClassesList,ClassesPage

secret_key = os.urandom(16)

def createApp():
    # 实例化应用
    app = Flask(__name__)
    # 设置密钥
    app.secret_key = secret_key
    # 加载蓝图
    app.register_blueprint(indexs)
    app.register_blueprint(student)
    app.register_blueprint(teacher)
    app.register_blueprint(classes)
    # 绑定 flask_login 插件
    login_manager = LoginManager(app)
    # login_manager配置信息
    login_manager.login_view = "/login"


    # 检测 会话 是否存在用户  是否登录
    @login_manager.user_loader
    def userLoader(username):
        # username  User.id
        if username:
            user= User()
            user.id = username
            return user

    #restfulapi
    api = Api(app)
    #注册接口 注册uri
    api.add_resource(Classes,'/api/classess/<int:id>',endpoint='classes')
    api.add_resource(ClassesList,'/api/classess/',endpoint='classelist')
    api.add_resource(ClassesPage, '/api/classess/<int:page>/<int:limit>/', endpoint="classespage")

    return app