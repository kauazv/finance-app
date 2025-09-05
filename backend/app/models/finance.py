from sqlalchemy import Colummn, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base
from datetime import datetime

class User(Base):
    _tablename_ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, nullable=False)
    password_hash = Column(String, unique=True, nullable=False)
    transactions = relationship("Transaction", back_populates="user")

class Category(Base):
    _tablename_ = "categories"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullabel=False)
    transactions = relationship("Transaction", back_populates="category")

class Transaction(Base):
    _tablename_ = "transactions"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    category_id = Column(Integer, ForeignKey ("categories.id"))
    amount = Column(Float)
    type = Column(String)
    description  = Column(String)
    date = Column(DateTime, default=datetime.utcnow)
    user = relationship("User", back_populates="transactions")
    category = relationship("Category", back_populates="transactions")