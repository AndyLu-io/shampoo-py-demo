from sqlalchemy import create_engine, Column, Integer, String, Boolean, Text, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime
# 定义 Base 类
from db.base import Base

class CompanyInfo(Base):
    __tablename__ = 'company_info'

    id = Column(Integer, primary_key=True, autoincrement=True)
    company_id = Column(String(64), nullable=True)
    merchant_id = Column(String(64), nullable=True)
    supplier_id = Column(String(64), nullable=True)
    company_name = Column(String(64), nullable=True)
    company_biz_type = Column(String(32), nullable=True)
    province_name = Column(String(64), nullable=True)
    city_name = Column(String(64), nullable=True)
    feature = Column(Text, nullable=True)
    type = Column(Integer, nullable=True)
    enable = Column(Boolean, nullable=False, default=True)
    biz_category = Column(String(32), nullable=True)
    company_level = Column(String(32), nullable=True)
    business_scope = Column(String(256), nullable=True)
    web_site_url = Column(String(256), nullable=True)
    created_time = Column(DateTime, default=datetime.now)
    updated_time = Column(DateTime, default=datetime.now, onupdate=datetime.now)
