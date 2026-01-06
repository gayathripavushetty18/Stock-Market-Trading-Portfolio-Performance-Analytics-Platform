import pandas as pd
from pathlib import Path

INPUT_FILE = "data/processed/clean_stock_data.csv"
OUTPUT_FILE = "data/processed/stock_analytics_pandas.csv"

Path("data/processed").mkdir(parents=True, exist_ok=True)

# Load data
df = pd.read_csv(INPUT_FILE)
df["date"] = pd.to_datetime(df["date"])

# Sort for time-series operations
df = df.sort_values(["company", "date"])

# Daily return
df["daily_return"] = df.groupby("company")["close"].pct_change()

# Moving averages
df["ma_7"] = df.groupby("company")["close"].rolling(7).mean().reset_index(0, drop=True)
df["ma_30"] = df.groupby("company")["close"].rolling(30).mean().reset_index(0, drop=True)

# Rolling volatility (30-day)
df["volatility_30"] = (
    df.groupby("company")["daily_return"]
      .rolling(30)
      .std()
      .reset_index(0, drop=True)
)

# Save output
df.to_csv(OUTPUT_FILE, index=False)

print("Pandas time-series transformations complete. Output saved to", OUTPUT_FILE)