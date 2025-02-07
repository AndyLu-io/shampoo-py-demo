from sqlalchemy import create_engine, Column, Integer, String, DateTime, func
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

# 定义 Base 类
Base = declarative_base()

class BookTop(Base):
    __tablename__ = 'book_top'

    id = Column(Integer, primary_key=True, autoincrement=True)
    book_source = Column(String(64), nullable=True)
    book_site = Column(String(256), nullable=True)
    rank_list_name = Column(String(128), nullable=True)
    rank_list_url = Column(String(256), nullable=True)
    book_name = Column(String(64), nullable=True)
    book_author = Column(String(64), nullable=True)
    book_url = Column(String(512), nullable=True)
    created_time = Column(DateTime, nullable=False, default=func.now())
    updated_time = Column(DateTime, nullable=False, default=func.now(), onupdate=func.now())

    def __repr__(self):
        return (f"<BookTop(id={self.id}, book_source='{self.book_source}', book_site='{self.book_site}', "
                f"rank_list_name='{self.rank_list_name}', rank_list_url='{self.rank_list_url}', "
                f"book_name='{self.book_name}', book_author='{self.book_author}', book_url='{self.book_url}', "
                f"created_time='{self.created_time}', updated_time='{self.updated_time}')>")
