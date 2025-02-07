from crawel.book.db.book_db_base import get_crawel_book_session
from crawel.book.db.model.book_info import BookInfo


class BookInfoDAO:

    @staticmethod
    def add_book_info(book_info_data):
        """新增书籍信息记录"""
        session = get_crawel_book_session()
        try:
            book_info = BookInfo(**book_info_data)
            session.add(book_info)
            session.commit()
            print(f"新增成功，ID: {book_info.id}")
            return book_info.id
        except Exception as e:
            session.rollback()
            print(f"新增失败: {e}")
            return None
        finally:
            session.close()

    @staticmethod
    def get_book_info_by_source_and_name(book_source, book_name):
        """根据 book_source 和 book_name 查询书籍信息"""
        session = get_crawel_book_session()
        try:
            return session.query(BookInfo).filter(
                BookInfo.book_source == book_source,
                BookInfo.book_name == book_name
            ).first()
        except Exception as e:
            print(f"查询失败: {e}")
        finally:
            session.close()

    @staticmethod
    def update_book_info_by_source_and_name(book_source, book_name, update_data):
        """根据 book_source 和 book_name 更新书籍信息"""
        session = get_crawel_book_session()
        try:
            book_infos = session.query(BookInfo).filter(
                BookInfo.book_source == book_source,
                BookInfo.book_name == book_name
            ).all()
            if book_infos:
                for book_info in book_infos:
                    for key, value in update_data.items():
                        setattr(book_info, key, value)
                session.commit()
                print(f"更新成功: book_source={book_source}, book_name={book_name}")
            else:
                print("未找到匹配的书籍信息，无法更新。")
        except Exception as e:
            session.rollback()
            print(f"更新失败: {e}")
        finally:
            session.close()

    @staticmethod
    def delete_book_info_by_source_and_name(book_source, book_name):
        """根据 book_source 和 book_name 删除书籍信息"""
        session = get_crawel_book_session()
        try:
            book_infos = session.query(BookInfo).filter(
                BookInfo.book_source == book_source,
                BookInfo.book_name == book_name
            ).all()
            if book_infos:
                for book_info in book_infos:
                    session.delete(book_info)
                session.commit()
                print(f"删除成功: book_source={book_source}, book_name={book_name}")
            else:
                print("未找到匹配的书籍信息，无法删除。")
        except Exception as e:
            session.rollback()
            print(f"删除失败: {e}")
        finally:
            session.close()

    @staticmethod
    def list_all_book_infos():
        """查询所有书籍信息"""
        session = get_crawel_book_session()
        try:
            return session.query(BookInfo).filter(
                BookInfo.finish_flag == 0
            ).all()
        except Exception as e:
            print(f"查询失败: {e}")
        finally:
            session.close()

    @staticmethod
    def get_by_book_url(book_url):
        session = get_crawel_book_session()
        try:
            return session.query(BookInfo).filter(BookInfo.book_url == book_url).first()
        except Exception as e:
            print(f"查询失败: {e}")
        finally:
            session.close()
