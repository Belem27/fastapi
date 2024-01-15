from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .config import settings
# import psycopg2
# import time


SQLALCHEMY_DATABASE_URL = f"postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# ***RAW SQL***
# while True:
#     try:
#         connect = psycopg2.connect(host='localhost', database='fastapi', user='postgres', password='$p@rk', cursor_factory=RealDictCursor)
#         cursor = connect.cursor()
#         print("Connection to database was successful!")
#         break
#     except Exception as error:
#         print("Failed to connect to database")
#         print("Error: ", error)
#         time.sleep(2)
        
# cursor.execute(""" SELECT * FROM posts """)
# posts = cursor.fetchall()

# cursor.execute(""" INSERT INTO posts (title, content, published) VALUES (%s, %s, %s) RETURNING *""",
#                (post.title, post.content, post.published))
# new_post = cursor.fetchone()
# connect.commit()

# cursor.execute(""" INSERT INTO posts (title, content):
# cursor.execute(""" SELECT * FROM posts WHERE id = %s""", (str(id)))
# post = cursor.fetchone()

# cursor.execute(""" DELETE FROM posts WHERE id = %s RETURNING *""", (str(id)))
# deleted_post = cursor.fetchone()
# connect.commit()
        
# cursor.execute(""" UPDATE posts SET title = %s, content = %s, published = %s WHERE id = %s RETURNING *""", (post.title, post.content, post.published, str(id)))
# updated_post = cursor.fetchone()
# connect.commit()