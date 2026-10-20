import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import os

# Tesla, Inc. (TSLA) Stock Analysis

ticker = "TSLA"
start_date = "2026-04-15"
end_date = "2026-10-15"


folder = os.path.dirname(os.path.abspath(__file__))


# Work Item 2 for TSLA: load daily data and inspect it

data = yf.download(ticker, start=start_date, end=end_date, auto_adjust=True, progress=False)
data.to_csv(os.path.join(folder, "TSLA_data.csv"))

print("Tesla (TSLA) Stock Data")
print("Start Date:", start_date)
print("End Date:", end_date)

print("\nfirst 5 rows:")
print(data.head())

print("\ndate range:")
print("start date:", data.index.min())
print("end date:", data.index.max())
print("\nnumber of records:", len(data))
print("\ncolumn names:")
print(data.columns)
print("\ndata types:")
print(data.dtypes)
print("\nmissing values:")
print(data.isnull().sum())
print("total missing values:", data.isnull().sum().sum())

# ============================================================
# Work Item 3 for TSLA: daily returns and descriptive statistics
# ============================================================
close = data["Close"].squeeze()      # TSLA closing prices
volume = data["Volume"].squeeze()    # TSLA trading volume

daily_returns = close.pct_change() * 100
daily_returns = daily_returns.dropna()
print("\nTSLA Daily Returns (%):")
print(daily_returns)

print("\nTSLA Closing Price Statistics:")
print(close.agg(["count", "mean", "median", "min", "max", "std"]).round(2))
print("\nTSLA Daily Returns Statistics (%):")
print(daily_returns.agg(["count", "mean", "median", "min", "max", "std"]).round(2))

# ============================================================
# Work Item 4 for TSLA: monthly summary
# ============================================================
monthly_avg = close.resample("ME").mean().round(2)                                # monthly average close
monthly_returns = daily_returns.resample("ME").sum().round(2)                    # monthly total return (%)
monthly_range = (close.resample("ME").max() - close.resample("ME").min()).round(2)  # monthly high - low
monthly_volume = volume.resample("ME").sum()                                     # monthly total volume

monthly_summary = pd.DataFrame({
    "Avg Close": monthly_avg,
    "Return (%)": monthly_returns,
    "Price Range": monthly_range,
    "Total Volume": monthly_volume,
})
monthly_summary.index = monthly_summary.index.strftime("%Y-%m")
print("\nTSLA Monthly Summary:")
print(monthly_summary)

# ============================================================
# Work Item 5 for TSLA: significant price movements
# ============================================================
highest_close = close.max()
highest_date = close.idxmax()
lowest_close = close.min()
lowest_date = close.idxmin()
big_gain = daily_returns.max()
big_gain_date = daily_returns.idxmax()
big_drop = daily_returns.min()
big_drop_date = daily_returns.idxmin()

print("\nHighest close:", round(highest_close, 2), "on", str(highest_date)[:10])
print("Lowest close: ", round(lowest_close, 2), "on", str(lowest_date)[:10])
print("Biggest gain (%):", round(big_gain, 2), "on", str(big_gain_date)[:10])
print("Biggest drop (%):", round(big_drop, 2), "on", str(big_drop_date)[:10])

first_close = close.iloc[0]
last_close = close.iloc[-1]
total_change = (last_close / first_close - 1) * 100
print("\nOverall change:", round(first_close, 2), "->", round(last_close, 2),
      f"({total_change:.2f}%)")

# Did volume support the moves? (compare each key day's volume to the average)
average_volume = volume.mean()
key_days = {
    "Highest close": highest_date,
    "Lowest close": lowest_date,
    "Biggest gain": big_gain_date,
    "Biggest drop": big_drop_date,
}
print("\nVolume on key days (1.00 = average):")
for label, day in key_days.items():
    relative_volume = volume.loc[day] / average_volume
    compare_text = "above" if relative_volume > 1 else "below"
    print(f"{label} ({str(day)[:10]}): {relative_volume:.2f}x ({compare_text} average)")

# ============================================================
# Work Item 6 for TSLA: charts
# ============================================================
charts_folder = os.path.join(folder, "charts")
os.makedirs(charts_folder, exist_ok=True)

# Chart 5: TSLA closing price with highest and lowest close marked
close.plot(label="TSLA Close")
plt.scatter(highest_date, highest_close, color="green", zorder=3,
            label=f"High {highest_close:.2f} ({str(highest_date)[:10]})")
plt.scatter(lowest_date, lowest_close, color="red", zorder=3,
            label=f"Low {lowest_close:.2f} ({str(lowest_date)[:10]})")
plt.title("TSLA Closing Price (Apr 15 - Oct 15, 2026)")
plt.ylabel("Price (USD)")
plt.legend()
plt.savefig(os.path.join(charts_folder, "chart5_tsla_price.png")); plt.close()

# Chart 6: TSLA daily returns, biggest gain and drop marked
daily_returns.plot(label="Daily Return (%)")
plt.axhline(0, color="gray", lw=0.8)
plt.scatter(big_gain_date, big_gain, color="green", zorder=3,
            label=f"Biggest gain {big_gain:.2f}% ({str(big_gain_date)[:10]})")
plt.scatter(big_drop_date, big_drop, color="red", zorder=3,
            label=f"Biggest drop {big_drop:.2f}% ({str(big_drop_date)[:10]})")
plt.title("TSLA Daily Returns (%)")
plt.ylabel("Daily Return (%)")
plt.legend()
plt.savefig(os.path.join(charts_folder, "chart6_tsla_returns.png")); plt.close()

print("\n2 TSLA charts saved to charts/")

