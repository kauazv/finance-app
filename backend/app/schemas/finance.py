from pydantic import BaseModel
from datetime import datetime

class TransactionBase(BaseModel):
    amount: float
    type: str
    description: str
    category_id: int

class TransactionCreate(TransactionBase):
    pass

class TransactionResponse(TransactionBase):
    id: int
    date: datetime

    class Config:
        orm_mode = True

class CategoryResponse(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True