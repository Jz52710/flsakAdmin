from database.db import Base,session
from sqlalchemy import Column,Integer,String,TIMESTAMP,ForeignKey
from sqlalchemy.orm import relationship
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer,SignatureExpired,BadSignature
import os


# 生成secre_key
secret_key = os.urandom(16)

class Admin(Base):
    __tablename__="admin"
    id = Column(Integer,primary_key=True)
    username = Column(String)
    password = Column(String)
    ctime = Column(TIMESTAMP)
    utime = Column(TIMESTAMP)

    #生成token
    def generate_auth_token(self,expiration=600):#有效期6分钟
        s = Serializer(secret_key,expires_in=expiration)
        return s.dumps({'id': self.id, 'type': 2})
    #检验token
    @staticmethod
    def verify_auth_token(token):
        s = Serializer(secret_key)
        try:
            data =s.loads(token)
        except SignatureExpired:
            return None  # valid token, but expired
        except BadSignature:
            return None  # invalid token
        user = Admin.query.get(data['id'])
        return user



class Classes(Base):
    __tablename__ = "classes"
    id = Column(Integer,primary_key=True)
    username = Column(String)
    ctime = Column(TIMESTAMP)
    utime = Column(TIMESTAMP)
    teacher = relationship("Teachers")
    student = relationship("Students")


class Teachers(Base):
    __tablename__ = "teachers"
    id = Column(Integer,primary_key=True)
    username = Column(String)
    password = Column(String)
    num = Column(Integer)
    age = Column(Integer)
    sex = Column(Integer)
    cid = Column(Integer,ForeignKey("classes.id"))
    ctime = Column(TIMESTAMP)
    utime = Column(TIMESTAMP)

    # 生成token
    def generate_auth_token(self, expiration=600):  # expiration = 600  有效期 6分钟
        s = Serializer(secret_key, expires_in=expiration)
        print(s)
        return s.dumps({'id': self.id, 'type': 2})

    # 检验token
    @staticmethod
    def verify_auth_token(token):
        s = Serializer(secret_key)
        try:
            data = s.loads(token)
        except SignatureExpired:
            return None  # valid token, but expired
        except BadSignature:
            return None  # invalid token
        user = Teachers.query.get(data['id'])
        return user

class Students(Base):
    __tablename__ = "students"
    id = Column(Integer, primary_key=True)
    username = Column(String)
    password = Column(String)
    num = Column(Integer)
    age = Column(Integer)
    sex = Column(Integer)
    cid = Column(Integer, ForeignKey("classes.id"))
    ctime = Column(TIMESTAMP)
    utime = Column(TIMESTAMP)

    # 生成token
    def generate_auth_token(self, expiration=600):  # 有效期6分钟
        s = Serializer(secret_key, expires_in=expiration)
        return s.dump({'id': self.id, 'type': 1})

    # 检验token
    @staticmethod
    def verify_auth_token(token):
        s = Serializer(secret_key)
        try:
            data = s.loads(token)
        except SignatureExpired:
            return None  # valid token, but expired
        except BadSignature:
            return None  # invalid token
        user = Students.query.get(data['id'])
        return user

def verify_auth_token(token):
    s = Serializer(secret_key)
    try:
        data = s.loads(token)
        #{ id:1,type1}
        return True
    except SignatureExpired:
        return False  # valid token, but expired
    except BadSignature:
        return False  # invalid token

