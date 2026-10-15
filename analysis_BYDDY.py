import yfinance as yf
import pandas as pd

# BYD Company Limited (BYDDY) Stock Analysis
ticker = "BYDDY"
data = yf.download(ticker, start="2026-04-15", end="2026-10-15", auto_adjust=True, progress=False)

# Calculate daily percentage returns for BYDDY stock.
close = data["Close"]
daily_returns = close.pct_change() * 100
daily_returns = daily_returns.dropna()

print(daily_returns)

#report descriptive statistics for BYDDY closing prices and daily returns.
price_stats = close.agg(["count", "mean","median","min","max","std"]).round(2)
return_stats = daily_returns.agg(["count", "mean","median","min","max","std"]).round(2)
print("\nBYDDY Closing Price Statistics:")
print(price_stats)
print("\nBYDDY Daily Returns Statistics:")
print(return_stats)