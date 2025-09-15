from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.finance import Transaction, Category
from app.ml.spending_analysis import analyze_spending
from app.auth import get_current_user

router = APIRouter()

@router.get("/recommendations")
def get_recommendations(db: Session = Depends(get_db), user_id=Depends(get_current_user)):
    trxs = db.query(Transaction).filter(Transaction.user_id==user_id).all()
    cat_lookup = {c.id: c.name for c in db.query(Category).all()}
    trx_list = [{"amount": t.amount, "type": t.type, "category": cat_lookup.get(t.category_id, "Outro"), "date": t.date} for t in trxs]
    analytics = analyze_spending(trx_list)
    recs = []
    for alert in analytics["alets"]:
        recs.append({
            "type": "warning",
            "message": f"Gasto incomum: R$ {alert['amount']} em {alert['category']} ({alert['date'].date()})",
            "sggestion": "Reavalie este gasto"
        })
    return recs