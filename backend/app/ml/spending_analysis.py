import pandas as pd
from sklearn.ensemble import IsolationForest

def analyze_spending(transactions: list):
    df = pd.DataFrame(transactions)
    if df.empty:
        return {"daily_average": 0, "category_dist": {}, "alerts": []}
    daily_average = df.groupby(df["date"].dt.date)["amount"].mean().mean()
    category_dist = df.groupby("category")["amount"].sum().to_dict()

    if len(df) > 5:
        model = IsolationForest(contamination=0.15)
        preds = model.fit_predict(df[["amount"]])
        alerts = df.loc[preds==-1].to_dict("records")
    else:
        alerts = []
    return {"daily_average": daily_average, "category_dist": category_dist, "alerts": alerts}