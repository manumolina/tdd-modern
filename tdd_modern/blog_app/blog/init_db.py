# init_db.py
if __name__ == '__main__':
    from tdd_modern.blog_app.blog.models import Article
    Article.create_table()
