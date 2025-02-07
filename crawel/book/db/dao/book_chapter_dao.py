from crawel.book.db.book_db_base import get_crawel_book_session
from crawel.book.db.model.book_chapter import BookChapter


class BookChapterDAO:

    @staticmethod
    def add_book_chapter(chapter_data):
        """新增章节记录"""
        session = get_crawel_book_session()
        try:
            chapter = BookChapter(**chapter_data)
            session.add(chapter)
            session.commit()
            print(f"新增成功，ID: {chapter.id}")
            return chapter.id
        except Exception as e:
            session.rollback()
            print(f"新增失败: {e}")
            return None
        finally:
            session.close()

    @staticmethod
    def get_chapter_by_source_name_and_chapter(book_source, book_name, chapter_name):
        """根据 book_source, book_name 和 chapter_name 查询章节信息"""
        session = get_crawel_book_session()
        try:
            return session.query(BookChapter).filter(
                BookChapter.book_source == book_source,
                BookChapter.book_name == book_name,
                BookChapter.chapter_name == chapter_name
            ).first()
        except Exception as e:
            print(f"查询失败: {e}")
        finally:
            session.close()

    @staticmethod
    def update_chapter_by_source_name_and_chapter(book_source, book_name, chapter_name, update_data):
        """根据 book_source, book_name 和 chapter_name 更新章节信息"""
        session = get_crawel_book_session()
        try:
            chapter = session.query(BookChapter).filter(
                BookChapter.book_source == book_source,
                BookChapter.book_name == book_name,
                BookChapter.chapter_name == chapter_name
            ).first()
            if chapter:
                for key, value in update_data.items():
                    setattr(chapter, key, value)
                session.commit()
                print(f"更新成功: book_source={book_source}, book_name={book_name}, chapter_name={chapter_name}")
            else:
                print("未找到匹配的章节信息，无法更新。")
        except Exception as e:
            session.rollback()
            print(f"更新失败: {e}")
        finally:
            session.close()

    @staticmethod
    def delete_chapter_by_source_name_and_chapter(book_source, book_name, chapter_name):
        """根据 book_source, book_name 和 chapter_name 删除章节信息"""
        session = get_crawel_book_session()
        try:
            chapter = session.query(BookChapter).filter(
                BookChapter.book_source == book_source,
                BookChapter.book_name == book_name,
                BookChapter.chapter_name == chapter_name
            ).first()
            if chapter:
                session.delete(chapter)
                session.commit()
                print(f"删除成功: book_source={book_source}, book_name={book_name}, chapter_name={chapter_name}")
            else:
                print("未找到匹配的章节信息，无法删除。")
        except Exception as e:
            session.rollback()
            print(f"删除失败: {e}")
        finally:
            session.close()

    @staticmethod
    def list_all_chapters():
        """查询所有章节信息"""
        session = get_crawel_book_session()
        try:
            return session.query(BookChapter).all()
        except Exception as e:
            print(f"查询失败: {e}")
        finally:
            session.close()
