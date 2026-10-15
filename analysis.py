import pandas as pd
import yfinance as yf

print("Group Stock Analysis")

stocks = ["TSLA", "XPEV", "BYDDY"]

start_date = "2026-04-15"
end_date= "2026-10-15"

print("Stocks:", stocks)
print("Start Date:", start_date)
print("End Date:", end_date)

# Download Stock Data
data = yf.download(stocks, start = start_date, end = end_date, auto_adjust = True, group_by = "column", progress = False)

#check
print("\ndate range:")
print("start date:", data.index.min())
print("end date:", data.index.max())
print("number of records:", len(data))
print("\ncolumn names:")
print(data.columns)
print("\ndata types:")
print(data.dtypes)
print("\nmissing values:")
print(data.isnull().sum())

# Calculate daily percentage returns for 3 stocks
close = data["Close"]
daily_returns = close.pct_change() * 100
daily_returns = daily_returns.dropna()
print(daily_returns)

##report descriptive statistics for 3 stocks' closing prices and daily returns.
print("\nClosing Price Statistics:")
print(close.agg(["count", "mean","median","min","max","std"]).round(2))
print("\nDaily Returns Statistics:")
print(daily_returns.agg(["count", "mean","median","min","max","std"]).round(2))

#the correlation between each pair of stocks' daily returns.
correlation = daily_returns.corr().round(2)
print("\ncorrelation between daily returns of stocks:")
print(correlation)

#interpretation 
print("\nInterpretation:")
print("BYDDY and XPEV correlate at 0.50, so the two Chinese EV makers move together moderately.")
print("BYDDY and TSLA correlate at only 0.14, meaning they are almost independent; TSLA is driven by its own factors.")

