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

#work item 4 for BYDDY
monthly_avg = close.resample("ME").mean().round(2) #月平均收盘价
monthly_returns = daily_returns.resample("ME").sum().round(2) #月平均收益率(哪个月整体涨跌）
monthly_range = (close.resample("ME").max() - close.resample("ME").min()).round(2) #月最大最小差值
monthly_volume = data["Volume"].resample("ME").sum().round(2) #月成交量
print('\nMonthly Average Closing Price:')
print(monthly_avg)
print('\nMonthly Returns:')
print(monthly_returns)
print('\nMonthly Price Range:')
print(monthly_range)
print('\nMonthly Trading Volume:')
print(monthly_volume)


