from sqlalchemy import create_engine, Column, Integer, String, Text, DateTime, func
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

# 定义 Base 类
Base = declarative_base()

class BookChapter(Base):
    __tablename__ = 'book_chapter'

    id = Column(Integer, primary_key=True, autoincrement=True)
    book_source = Column(String(64), nullable=True)
    book_site = Column(String(256), nullable=True)
    book_name = Column(String(128), nullable=True)
    book_author = Column(String(256), nullable=True)
    book_desc = Column(Text, nullable=True)
    chapter_name = Column(String(256), nullable=True)
    chapter_url = Column(String(256), nullable=True)
    content = Column(Text, nullable=True)
    chapter_index = Column(Integer, nullable=True)
    created_time = Column(DateTime, nullable=False, default=func.now())
    updated_time = Column(DateTime, nullable=False, default=func.now(), onupdate=func.now())

    def __repr__(self):
        return (f"<BookChapter(id={self.id}, book_source='{self.book_source}', book_site='{self.book_site}', "
                f"book_name='{self.book_name}', book_author='{self.book_author}', book_desc='{self.book_desc}', "
                f"chapter_name='{self.chapter_name}', chapter_url='{self.chapter_url}', content='{self.content}', "
                f"created_time='{self.created_time}', updated_time='{self.updated_time}')>")
