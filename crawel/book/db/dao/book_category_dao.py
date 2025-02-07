from crawel.book.db.book_db_base import get_crawel_book_session
from crawel.book.db.model.book_category import BookCategory

class BookCategoryDAO:

    @staticmethod
    def add_book_category(category_data):
        """新增分类记录"""
        session = get_crawel_book_session()
        try:
            category = BookCategory(**category_data)
            session.add(category)
            session.commit()
            print(f"新增成功，ID: {category.id}")
            return category.id
        except Exception as e:
            session.rollback()
            print(f"新增失败: {e}")
            return None
        finally:
            session.close()

    @staticmethod
    def get_category_by_name(category_name):
        """根据 ID 查询分类"""
        session = get_crawel_book_session()
        try:
            return session.query(BookCategory).filter(BookCategory.category_name == category_name).first()
        except Exception as e:
            print(f"查询失败: {e}")
        finally:
            session.close()

    @staticmethod
    def update_category(category_name, update_data):
        """更新分类记录"""
        session = get_crawel_book_session()
        try:
            category = session.query(BookCategory).filter(BookCategory.category_name == category_name).first()
            if category:
                for key, value in update_data.items():
                    setattr(category, key, value)
                session.commit()
                print(f"更新成功: {category_name}")
            else:
                print("未找到分类信息，无法更新。")
        except Exception as e:
            session.rollback()
            print(f"更新失败: {e}")
        finally:
            session.close()

    @staticmethod
    def delete_category(category_name):
        """删除分类记录"""
        session = get_crawel_book_session()
        try:
            category = session.query(BookCategory).filter(BookCategory.category_name == category_name).first()
            if category:
                session.delete(category)
                session.commit()
                print(f"删除成功: {category_name}")
            else:
                print("未找到分类信息，无法删除。")
        except Exception as e:
            session.rollback()
            print(f"删除失败: {e}")
        finally:
            session.close()

    @staticmethod
    def list_all_categories():
        """查询所有分类"""
        session = get_crawel_book_session()
        try:
            return session.query(BookCategory).all()
        except Exception as e:
            print(f"查询失败: {e}")
        finally:
            session.close()

    @staticmethod
    def get_category_by_book_source(book_source):
        """根据 ID 查询分类"""
        session = get_crawel_book_session()
        try:
            return session.query(BookCategory).filter(BookCategory.book_source == book_source).all()
        except Exception as e:
            print(f"查询失败: {e}")
        finally:
            session.close()