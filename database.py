from flask_sqlalchemy import SQLAlchemy
import os

def init_db(app):
    app.config["SQLALCHEMY_DATABASE_URI"] = f"postgresql+psycopg2://postgres:{os.getenv('DB_PASSWORD')}@54.252.236.254:5432/library_api"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db = SQLAlchemy(app)
    return db


# import psycopg2
# import os

# connection = psycopg2.connect(
#     database="library_api",
#     user="postgres",
#     password=os.getenv("DB_PASSWORD"),
#     host="54.252.236.254",
#     port="5432"
# )

# cursor = connection.cursor()

# cursor.execute("create table if not exists books (id serial PRIMARY KEY, title varchar);")
# connection.commit()