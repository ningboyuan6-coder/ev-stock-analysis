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