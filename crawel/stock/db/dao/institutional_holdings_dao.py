from crawel.stock.db.model.institutional_holdings import InstitutionalHolding
from crawel.stock.db.stock_db_base import get_stock_session


class InstitutionalHoldingsDAO:

    @staticmethod
    def add_institutional_holding(holding_data):
        """新增持股记录"""
        session = get_stock_session()
        try:
            holding = InstitutionalHolding(**holding_data)
            session.add(holding)
            session.commit()
            print(f"新增成功，ID: {holding.id}")
            return holding.id
        except Exception as e:
            session.rollback()
            print(f"新增失败: {e}")
            return None
        finally:
            session.close()

    @staticmethod
    def get_holding_by_id(holding_id):
        """根据 ID 查询持股记录"""
        session = get_stock_session()
        try:
            return session.query(InstitutionalHolding).filter(InstitutionalHolding.id == holding_id).first()
        except Exception as e:
            print(f"查询失败: {e}")
        finally:
            session.close()

    @staticmethod
    def get_holding_by_security_code_and_org_type(security_code, org_type, report_date):
        """根据证券代码和机构类型查询持股记录"""
        session = get_stock_session()
        try:
            return session.query(InstitutionalHolding).filter(InstitutionalHolding.security_code == security_code,
                                                              InstitutionalHolding.org_type == org_type,
                                                              InstitutionalHolding.report_date == report_date).first()
        except Exception as e:
            print(f"查询失败: {e}")
        finally:
            session.close()

    def list_holding_by_security_code_and_org_type(self,security_code, org_type):
        """根据证券代码和机构类型查询持股记录"""
        session = get_stock_session()
        try:
            return session.query(InstitutionalHolding).filter(InstitutionalHolding.security_code == security_code,
                                                              InstitutionalHolding.org_type == org_type).all()
        except Exception as e:
            print(f"查询失败: {e}")
        finally:
            session.close()

    @staticmethod
    def get_holding_by_secu_code(secu_code):
        """根据证券代码查询持股记录"""
        session = get_stock_session()
        try:
            return session.query(InstitutionalHolding).filter(InstitutionalHolding.secu_code == secu_code).all()
        except Exception as e:
            print(f"查询失败: {e}")
        finally:
            session.close()

    @staticmethod
    def update_holding(holding_id, update_data):
        """更新持股记录"""
        session = get_stock_session()
        try:
            holding = session.query(InstitutionalHolding).filter(InstitutionalHolding.id == holding_id).first()
            if holding:
                for key, value in update_data.items():
                    setattr(holding, key, value)
                session.commit()
                print(f"更新成功，ID: {holding_id}")
            else:
                print("未找到持股记录，无法更新。")
        except Exception as e:
            session.rollback()
            print(f"更新失败: {e}")
        finally:
            session.close()

    @staticmethod
    def delete_holding(holding_id):
        """删除持股记录"""
        session = get_stock_session()
        try:
            holding = session.query(InstitutionalHolding).filter(InstitutionalHolding.id == holding_id).first()
            if holding:
                session.delete(holding)
                session.commit()
                print(f"删除成功，ID: {holding_id}")
            else:
                print("未找到持股记录，无法删除。")
        except Exception as e:
            session.rollback()
            print(f"删除失败: {e}")
        finally:
            session.close()

    @staticmethod
    def list_all_holdings():
        """查询所有持股记录"""
        session = get_stock_session()
        try:
            return session.query(InstitutionalHolding).all()
        except Exception as e:
            print(f"查询失败: {e}")
        finally:
            session.close()

    @staticmethod
    def get_holdings_by_org_type(org_type):
        """根据机构类型查询持股记录"""
        session = get_stock_session()
        try:
            return session.query(InstitutionalHolding).filter(InstitutionalHolding.org_type == org_type).all()
        except Exception as e:
            print(f"查询失败: {e}")
        finally:
            session.close()
