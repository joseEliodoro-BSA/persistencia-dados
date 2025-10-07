from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "mysql://root:root@localhost:3306/db_escola"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine) # conexão entre o banco é o código

Base = declarative_base()