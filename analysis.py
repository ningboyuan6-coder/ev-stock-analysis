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

# work item 6 for all stocks: creat 4 chart.
import matplotlib.pyplot as plt
import os 

# Create a directory for the charts
os.makedirs("charts", exist_ok=True)

#chart1:Full-range normalized comparison line chart
norm = close / close.iloc[0] * 100
norm.plot()
plt.title("Normalized Closing Prices (Apr 15 - Oct 15, start=100)")
plt.ylabel("Normalized Price")
plt.legend(stocks)
plt.savefig("charts/chart1_normalized.png"); plt.close()

#chart2:Zoom-in for volatile period (BYDDY, mark new low on 10-14)
close["BYDDY"].loc["2026-08-15":"2026-10-15"].plot()
plt.axvline(pd.Timestamp("2026-10-14"), color="red", ls="--", label="10-14 low 9.22")
plt.title("BYDDY Aug-Oct 2026 (hit new low on 10-14)")
plt.ylabel("Price (USD)")
plt.legend()
plt.savefig("charts/chart2_byddy_zoom.png"); plt.close()

#chart3:Distribution of Daily Returns (Three Box Plots)
daily_returns.plot.box()
plt.title("Distribution of Daily Returns by Stock")
plt.ylabel("Daily Return (%)")
plt.savefig("charts/chart3_returns_box.png"); plt.close()

#chart4:Scatter Plot of Two Stocks (BYDDY vs XPEV)
plt.scatter(daily_returns["BYDDY"], daily_returns["XPEV"], alpha=0.5)
plt.xlabel("BYDDY Daily Return (%)")
plt.ylabel("XPEV Daily Return (%)")
plt.title("BYDDY vs XPEV Daily Returns")
plt.savefig("charts/chart4_byddy_xpev.png"); plt.close()

print("4 charts saved to charts/")