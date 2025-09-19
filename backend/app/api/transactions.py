from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.models.finance import Transaction, Category
from app.schemas.finance import TransactionCreate, TransactionResponse
from app.database import get_db
from app.auth import get_current_user
from datetime import datetime

router = APIRouter()

def add_transaction(data: TransactionCreate, db: Session = Depends(get_db), user_id=Depends(get_current_user)):
    trx = Transaction(**data.dict(), user_id=user_id, date=datetime.utcnow())
    db.add(trx)
    db.commit()
    db.refresh(trx)
    return trx

@router.get("/", response_model=list[TransactionResponse])
def list_transactions(db: Session = Depends(get_db), user_id=Depends(get_current_user_)):
    trxs = db.query(Transaction).filter(Transaction.user_id==user_id).order_by(Transaction.date.desc()).all()
    return trxs