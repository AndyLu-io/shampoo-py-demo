from db import CompanyInfo
from db.base import get_session


class CompanyInfoDAO:

    @staticmethod
    def add_company(company_data):
        session = get_session()
        """新增公司记录"""
        try:
            company = CompanyInfo(**company_data)
            session.add(company)
            session.commit()
            print(f"新增成功，ID: {company.id}")
        except Exception as e:
            session.rollback()
            print(f"新增失败: {e}")
        finally:
            session.close()

    @staticmethod
    def get_company_by_id(company_id):
        session = get_session()
        """根据 ID 查询公司"""
        try:
            return session.query(CompanyInfo).filter(CompanyInfo.company_id == company_id).first()
        except Exception as e:
            print(f"查询失败: {e}")
        finally:
            session.close()

    @staticmethod
    def update_company(company_id, update_data):
        session = get_session()
        """更新公司记录"""
        try:
            company = session.query(CompanyInfo).filter(CompanyInfo.company_id == company_id).first()
            if company:
                for key, value in update_data.items():
                    setattr(company, key, value)
                session.commit()
                print(f"更新成功: {company_id}")
            else:
                print("未找到公司信息，无法更新。")
        except Exception as e:
            session.rollback()
            print(f"更新失败: {e}")
        finally:
            session.close()

    @staticmethod
    def delete_company(company_id):
        session = get_session()
        """删除公司记录"""
        try:
            company = session.query(CompanyInfo).filter(CompanyInfo.company_id == company_id).first()
            if company:
                session.delete(company)
                session.commit()
                print(f"删除成功: {company_id}")
            else:
                print("未找到公司信息，无法删除。")
        except Exception as e:
            session.rollback()
            print(f"删除失败: {e}")

    @staticmethod
    def list_all_companies():
        session = get_session()
        """查询所有公司"""
        try:
            return session.query(CompanyInfo).all()
        except Exception as e:
            print(f"查询失败: {e}")
