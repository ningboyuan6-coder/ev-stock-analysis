
import yfinance as yf
import pandas as pd

# XPeng stock analysis
ticker = "XPEV"
start_date = "2026-04-15"
end_date = "2026-10-16"

# Download daily stock data
data = yf.download(
    ticker,
    start=start_date,
    end=end_date,
    auto_adjust=True
)

# Inspect the data
print("Stock:", ticker)
print("Date range:", data.index.min(), "to", data.index.max())
print("Number of records:", len(data))
print("Column names:", data.columns.tolist())
print("Data types:")
print(data.dtypes)
print("Missing values:")
print(data.isnull().sum())
