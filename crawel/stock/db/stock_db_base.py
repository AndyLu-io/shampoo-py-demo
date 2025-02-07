from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# 定义全局的 Base
Base = declarative_base()

# 配置数据库连接
DATABASE_URL = "mysql+pymysql://root:asdf1234@127.0.0.1:3306/stock"
engine = create_engine(DATABASE_URL, echo=True)  # echo=True 可调试时打印 SQL 语句
Session = sessionmaker(bind=engine)

# 提供全局会话
def get_stock_session():
    return Session()
