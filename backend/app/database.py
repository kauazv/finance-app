from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
import os

DB_URL = os.getenv("DATABASE_URL", "postgresql://finance_user:finance_pass@postgres:5432/finance_db")
engine = create_engine(DB_URL)
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)
Base = delcarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()