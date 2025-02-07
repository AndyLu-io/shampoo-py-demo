from sqlalchemy import create_engine, Column, Integer, String, DateTime, func
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

# 定义 Base 类
Base = declarative_base()

class BookCategory(Base):
    __tablename__ = 'book_category'

    id = Column(Integer, primary_key=True, autoincrement=True)
    book_source = Column(String(64), nullable=True)
    book_site = Column(String(256), nullable=True)
    category_name = Column(String(128), nullable=True)
    category_url = Column(String(256), nullable=True)
    created_time = Column(DateTime, nullable=False, default=func.now())
    updated_time = Column(DateTime, nullable=False, default=func.now(), onupdate=func.now())

    def __repr__(self):
        return (f"<BookCategory(id={self.id}, book_source='{self.book_source}', "
                f"book_site='{self.book_site}', category_name='{self.category_name}', "
                f"category_url='{self.category_url}', created_time='{self.created_time}', "
                f"updated_time='{self.updated_time}')>")
