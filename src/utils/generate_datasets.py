import pandas as pd
import numpy as np
from pathlib import Path

np.random.seed(42)

DATA_PATH = "data/raw"
STOCK_PATH = f"{DATA_PATH}/stocks"
PORTFOLIO_PATH = f"{DATA_PATH}/portfolio"

Path(STOCK_PATH).mkdir(parents=True, exist_ok=True)
Path(PORTFOLIO_PATH).mkdir(parents=True, exist_ok=True)

stocks = {
    "AAPL": {"sector": "Technology", "start_price": 150},
    "MSFT": {"sector": "Technology", "start_price": 220},
    "JPM": {"sector": "Finance", "start_price": 100},
    "GOOGL": {"sector": "Technology", "start_price": 120}
}

dates = pd.bdate_range(start="2005-01-01", periods=5200)

def generate_stock_data(symbol, sector, start_price):
    prices = [start_price]

    for _ in range(1, len(dates)):
        change = np.random.normal(0, 1)
        prices.append(max(prices[-1] + change, 5))

    df = pd.DataFrame({
        "date": dates,
        "open": prices,
        "high": [p + np.random.uniform(0, 2) for p in prices],
        "low": [p - np.random.uniform(0, 2) for p in prices],
        "close": [p + np.random.uniform(-1, 1) for p in prices],
        "volume": np.random.randint(1_000_000, 10_000_000, size=len(dates)),
        "company": symbol,
        "sector": sector
    })

    df.to_csv(f"{STOCK_PATH}/{symbol}.csv", index=False)

for stock, info in stocks.items():
    generate_stock_data(stock, info["sector"], info["start_price"])

# Portfolio transactions
portfolio = []

for _ in range(1000):
    stock = np.random.choice(list(stocks.keys()))
    date = np.random.choice(dates)
    transaction_type = np.random.choice(["BUY", "SELL"], p=[0.7, 0.3])
    quantity = np.random.randint(5, 50)
    price = np.random.uniform(50, 300)

    portfolio.append([
        date, stock, transaction_type, quantity, round(price, 2)
    ])

portfolio_df = pd.DataFrame(
    portfolio,
    columns=["transaction_date", "stock", "transaction_type", "quantity", "price"]
)

portfolio_df.to_csv(
    f"{PORTFOLIO_PATH}/portfolio_transactions.csv",
    index=False
)

print("✅ Stock and portfolio datasets generated successfully")
