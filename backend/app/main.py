from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api import transactions, analytics

app = FastAPI (title="Gerenciador Financeiro", version="1.0")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], allow_credentials=True, allow_methods=["*"], allow_headers=["*"]
)
app.include_router(transactions.router, prefix="/api/transatcions")
app.include_router(analytics.router, prefix="/api/analytics")