from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy import create_engine


DATABASE_URL = "mysql+mysqlconnector://root:root@127.0.0.1/productdb"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()