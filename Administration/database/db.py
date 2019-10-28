from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


engine = create_engine("mysql+pymysql://root:jz52710@127.0.0.1:3306/stbale?charset=utf8")

Session = sessionmaker(bind=engine)
session = Session()

#创建数据库基类
Base = declarative_base()
