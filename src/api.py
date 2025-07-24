"""Module for API endpoints related to stock price alerts."""

from __future__ import annotations
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Dict

app = FastAPI()

# In-memory stores for tickers and alerts
tickers: List[str] = []
alerts: List[Dict] = []


class TickerRequest(BaseModel):
    symbol: str


class AlertRequest(BaseModel):
    symbol: str
    target_price: float
    direction: str  # 'above' or 'below'


@app.post("/tickers", summary="Add a ticker to watch")
def add_ticker(req: TickerRequest):
    symbol = req.symbol.upper()
    if symbol in tickers:
        raise HTTPException(status_code=400, detail="Ticker already added.")
    tickers.append(symbol)
    return {"message": f"Ticker {symbol} added."}


@app.get("/tickers", summary="List all watched tickers")
def list_tickers():
    return {"tickers": tickers}


@app.post("/alerts", summary="Set a price alert for a ticker")
def set_alert(req: AlertRequest):
    if req.symbol.upper() not in tickers:
        raise HTTPException(status_code=404, detail="Ticker not found.")
    alert = req.dict()
    alert["symbol"] = alert["symbol"].upper()
    alerts.append(alert)
    return {
        "message": f"Alert set for {alert['symbol']} {alert['direction']} {alert['target_price']}"
    }


@app.get("/alerts", summary="List all alerts")
def list_alerts():
    return {"alerts": alerts}
