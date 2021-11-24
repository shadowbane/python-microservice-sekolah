import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

load_dotenv()

db_host = os.getenv('DB_HOST', 'localhost')
db_port = os.getenv('DB_PORT', 3306)
db_username = os.getenv('DB_USERNAME', 'root')
db_password = os.getenv('DB_PASSWORD', 'password')
db_database = os.getenv('DB_DATABASE', 'microservice_sekolah')

SQLALCHEMY_DATABASE_URL = "mysql+mysqlconnector://" \
                          + db_username \
                          + ":" \
                          + db_username \
                          + "@" \
                          + db_host \
                          + ":" \
                          + db_port \
                          + "/" \
                          + db_database

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = None
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()
