
from sqlalchemy import create_engine, Column, Integer, String, BigInteger, DateTime, func
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from sqlalchemy.types import DECIMAL

# 定义 Base 类
Base = declarative_base()

class InstitutionalHolding(Base):
    __tablename__ = 'institutional_holdings'

    # 主键，自增
    id = Column(Integer, primary_key=True, autoincrement=True)
    # 证券内码，唯一标识股票
    security_inner_code = Column(String(50), nullable=False, comment='证券内码，唯一标识股票')
    # 证券简称（股票名称的简称）
    security_name_abbr = Column(String(255), nullable=False, comment='证券简称（股票名称的简称）')
    # 报告日期，表示报告发布时间
    report_date = Column(DateTime, nullable=False, default=datetime.utcnow, comment='报告日期，表示报告发布时间')
    # 机构类型代码（例如：QFII、券商等）
    org_type = Column(String(10), nullable=False, comment='机构类型代码（例如：QFII、券商等）')
    # 持股数量，表示该机构持有的股票数
    hould_num = Column(BigInteger, nullable=False, comment='持股数量，表示该机构持有的股票数')
    # 总股本，表示公司总股本
    total_shares = Column(BigInteger, nullable=False, comment='总股本，表示公司总股本')
    # 持股市值，表示该机构持有股票的市值
    hold_value = Column(DECIMAL(20, 2), nullable=False, comment='持股市值，表示该机构持有股票的市值')
    # 流通股比例，表示该机构持有的流通股比例（百分比）
    freeshares_ratio = Column(DECIMAL(10, 8), nullable=False, comment='流通股比例，表示该机构持有的流通股比例（百分比）')
    # 持股变化，表示机构增持或减持的状态
    holdcha = Column(String(10), nullable=False, comment='持股变化，表示机构增持或减持的状态')
    # 持股变化数量，增持或减持的股票数
    holdcha_num = Column(BigInteger, nullable=False, comment='持股变化数量，增持或减持的股票数')
    # 持股变化比例，表示持股变化的百分比
    holdcha_ratio = Column(DECIMAL(10, 2), nullable=False, comment='持股变化比例，表示持股变化的百分比')
    # 证券代码，股票的唯一代码（例如：001300.SZ）
    secu_code = Column(String(20), nullable=True, comment='证券代码，股票的唯一代码（例如：001300.SZ）')
    # 总股本占比，表示该机构持股占公司总股本的比例
    totalshares_ratio = Column(DECIMAL(10, 8), nullable=False, comment='总股本占比，表示该机构持股占公司总股本的比例')
    # 机构类型名称，表示机构的完整名称（例如：QFII、基金等）
    org_type_name = Column(String(50), nullable=False, comment='机构类型名称，表示机构的完整名称（例如：QFII、基金等）')
    # 持股变化率，表示持股的增减幅度（百分比）
    qchange_rate = Column(DECIMAL(10, 2), nullable=False, comment='持股变化率，表示持股的增减幅度（百分比）')
    # 流通市值，表示公司流通股票的总市值
    free_market_cap = Column(DECIMAL(20, 2), nullable=False, comment='流通市值，表示公司流通股票的总市值')
    # 流通股本，表示公司流通股的总数
    free_shares = Column(BigInteger, nullable=False, comment='流通股本，表示公司流通股的总数')
    # 证券类型代码，表示股票所属的证券类型（如：A股、B股等）
    security_type_code = Column(String(20), nullable=False, comment='证券类型代码，表示股票所属的证券类型（如：A股、B股等）')
    # 持股变化金额，表示持股变化的金额（增持或减持的市值）
    holdcha_value = Column(DECIMAL(20, 2), nullable=False, comment='持股变化金额，表示持股变化的金额（增持或减持的市值）')
    # 证券代码（简化格式），用于快速标识股票
    security_code = Column(String(20), nullable=False, comment='证券代码（简化格式），用于快速标识股票')
    # 流通股比例变化，表示流通股比例的变化幅度
    freeshares_ratio_change = Column(DECIMAL(5, 2), nullable=False, comment='流通股比例变化，表示流通股比例的变化幅度')
    # 类型编号，表示不同类别的编号（如QFII、基金等）
    type_num = Column(Integer, nullable=False, comment='类型编号，表示不同类别的编号（如QFII、基金等）')

    # 创建时间
    created_time = Column(DateTime, nullable=False, default=func.now(), comment='记录创建时间')
    # 更新时间，每次更新时自动更新
    updated_time = Column(DateTime, nullable=False, default=func.now(), onupdate=func.now(), comment='记录最后更新时间')

    def __repr__(self):
        return (f"<InstitutionalHolding(id={self.id}, security_inner_code='{self.security_inner_code}', "
                f"security_name_abbr='{self.security_name_abbr}', report_date='{self.report_date}', "
                f"org_type='{self.org_type}', hould_num={self.hould_num}, total_shares={self.total_shares}, "
                f"hold_value={self.hold_value}, freeshares_ratio={self.freeshares_ratio}, "
                f"holdcha='{self.holdcha}', holdcha_num={self.holdcha_num}, holdcha_ratio={self.holdcha_ratio}, "
                f"secu_code='{self.secu_code}', totalshares_ratio={self.totalshares_ratio}, "
                f"org_type_name='{self.org_type_name}', qchange_rate={self.qchange_rate}, "
                f"free_market_cap={self.free_market_cap}, free_shares={self.free_shares}, "
                f"security_type_code='{self.security_type_code}', holdcha_value={self.holdcha_value}, "
                f"security_code='{self.security_code}', freeshares_ratio_change={self.freeshares_ratio_change}, "
                f"type_num={self.type_num}, created_time='{self.created_time}', updated_time='{self.updated_time}')>")

