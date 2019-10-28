from flask_restful import Resource,fields,marshal,reqparse
from flask import jsonify
from database.db import session
from database.tables import Classes as cla
from datetime import datetime
import math




#获取班级列表信息
classes_fields={
    'id':fields.Integer,
    'username':fields.String,
    'ctime':fields.Raw,
    'utime':fields.Raw,
}

#时间处理函数
def EditTime(item):
    item['ctime'] = item['ctime'].strftime("%Y-%m-%d %H:%M:%S")
    item['utime'] = item['utime'].strftime("%Y-%m-%d %H:%M:%S")
    return item

# 班级分页
class ClassesPage(Resource):
    def get(self,page,limit):
        start = (page - 1) * limit
        data = session.query(cla).limit(limit).offset(start)
        arr = [EditTime(marshal(item, classes_fields)) for item in data]
        num = session.query(cla).count()
        pageNum = math.ceil(num / limit)
        return {'code': 200, 'data': arr, 'pagenum': pageNum}


#获取班级列表
class ClassesList(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument("username", type=str, required=True, help="username参数不正确")
        super().__init__()

    def get(self):
        data = session.query(cla).all()
        print(data)
        #序列号
        arr = [EditTime(marshal(item,classes_fields)) for item in data]
        return {'msg':'ok','data':arr},200

    # 添加
    def post(self):
        args = self.reqparse.parse_args()
        username = args.username
        now = datetime.now()
        now = now.strftime("%Y-%m-%d %H:%M:%S")
        c = cla(username=username, ctime=now, utime=now)
        session.add(c)
        session.commit()
        return {'msg': 'ok', 'data': {'username': username, 'ctime': now, 'utime': now}}

# 获取班级单个信息
class Classes(Resource):
    def get(self,id):
        print(id)
        print('班级请求')
        return jsonify({'code':200,'msg':'ok'})
