from crawel.book.db.book_db_base import get_crawel_book_session
from crawel.book.db.model.book_top import BookTop


class BookTopDAO:

    @staticmethod
    def add_book_top(book_top_data):
        """新增排行榜记录"""
        session = get_crawel_book_session()
        try:
            book_top = BookTop(**book_top_data)
            session.add(book_top)
            session.commit()
            print(f"新增成功，ID: {book_top.id}")
            return book_top.id
        except Exception as e:
            session.rollback()
            print(f"新增失败: {e}")
            return None
        finally:
            session.close()

    @staticmethod
    def get_book_top_by_rank_and_book_name(book_source, rank_list_name, book_name):
        """根据 rank_list_name 查询排行榜记录"""
        session = get_crawel_book_session()
        try:
            return session.query(BookTop).filter(
                BookTop.book_source == book_source,
                BookTop.rank_list_name == rank_list_name,
                BookTop.book_name == book_name
            ).first()
        except Exception as e:
            print(f"查询失败: {e}")
        finally:
            session.close()

    @staticmethod
    def get_book_top_by_source_and_rank_list_name(book_source, rank_list_name):
        """根据 book_source 和 rank_list_name 进行联合查询"""
        session = get_crawel_book_session()
        try:
            return session.query(BookTop).filter(
                BookTop.book_source == book_source,
                BookTop.rank_list_name == rank_list_name
            ).all()
        except Exception as e:
            print(f"联合查询失败: {e}")
        finally:
            session.close()

    @staticmethod
    def update_book_top(rank_list_name, update_data):
        """更新排行榜记录"""
        session = get_crawel_book_session()
        try:
            book_tops = session.query(BookTop).filter(BookTop.rank_list_name == rank_list_name).all()
            if book_tops:
                for book_top in book_tops:
                    for key, value in update_data.items():
                        setattr(book_top, key, value)
                session.commit()
                print(f"更新成功: {rank_list_name}")
            else:
                print("未找到排行榜记录，无法更新。")
        except Exception as e:
            session.rollback()
            print(f"更新失败: {e}")
        finally:
            session.close()

    @staticmethod
    def delete_book_top(rank_list_name):
        """删除排行榜记录"""
        session = get_crawel_book_session()
        try:
            book_tops = session.query(BookTop).filter(BookTop.rank_list_name == rank_list_name).all()
            if book_tops:
                for book_top in book_tops:
                    session.delete(book_top)
                session.commit()
                print(f"删除成功: {rank_list_name}")
            else:
                print("未找到排行榜记录，无法删除。")
        except Exception as e:
            session.rollback()
            print(f"删除失败: {e}")
        finally:
            session.close()

    @staticmethod
    def list_all_book_tops():
        """查询所有排行榜记录"""
        session = get_crawel_book_session()
        try:
            return session.query(BookTop).all()
        except Exception as e:
            print(f"查询失败: {e}")
        finally:
            session.close()
