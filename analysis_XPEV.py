
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



# Calculate daily percentage returns
close_prices = data["Close"].squeeze()
daily_returns = close_prices.pct_change(fill_method=None) * 100

# Closing price statistics
print("\n=== XPEV Closing Price Statistics ===")
print(close_prices.describe())
print("Median:", close_prices.median())

# Daily return statistics
print("\n=== XPEV Daily Return Statistics (%) ===")
print(daily_returns.describe())
print("Median:", daily_returns.median())



# Identify significant daily stock movements
print("\n=== XPEV Significant Price Movements ===")

# Largest daily increase
max_gain_date = daily_returns.idxmax()
max_gain = daily_returns.max()

# Largest daily decrease
max_loss_date = daily_returns.idxmin()
max_loss = daily_returns.min()

# Extract closing prices and trading volume
volume = data["Volume"].squeeze()

print("\nLargest Daily Increase:")
print("Date:", max_gain_date.date())
print("Daily Return:", round(max_gain, 2), "%")
print("Closing Price: $", round(close_prices.loc[max_gain_date], 2))
print("Trading Volume:", int(volume.loc[max_gain_date]))

print("\nLargest Daily Decrease:")
print("Date:", max_loss_date.date())
print("Daily Return:", round(max_loss, 2), "%")
print("Closing Price: $", round(close_prices.loc[max_loss_date], 2))
print("Trading Volume:", int(volume.loc[max_loss_date]))

# Compare trading volume on significant movement days
average_volume = volume.mean()

print("\n=== XPEV Trading Volume Analysis ===")
print("Average Daily Volume:", round(average_volume))

print("May 26 Volume:", int(volume.loc[max_gain_date]))
print("August 24 Volume:", int(volume.loc[max_loss_date]))

print("May 26 Volume Ratio:",
      round(volume.loc[max_gain_date] / average_volume, 2))

print("August 24 Volume Ratio:",
      round(volume.loc[max_loss_date] / average_volume, 2))

# Create XPEV significant price movement chart
import matplotlib.pyplot as plt
import os

os.makedirs("charts", exist_ok=True)

# Show stock prices around the largest daily decrease
window_start = max_loss_date - pd.Timedelta(days=14)
window_end = max_loss_date + pd.Timedelta(days=14)

zoom_prices = close_prices.loc[window_start:window_end]

plt.figure(figsize=(10, 5))
plt.plot(zoom_prices.index, zoom_prices.values,
         marker="o", label="XPEV Closing Price")

plt.axvline(max_loss_date, color="red",
            linestyle="--", label="Largest Daily Drop")

plt.title("XPEV Stock Price Around August 24, 2026")
plt.xlabel("Date")
plt.ylabel("Closing Price (USD)")
plt.legend()
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig("charts/chart5_xpev_zoom.png", dpi=300)
plt.close()

print("\nChart saved: charts/chart5_xpev_zoom.png")
# Monthly summary using pandas resample
monthly_summary = pd.DataFrame({
    "Closing Price": close_prices,
    "Daily Return (%)": daily_returns
}).resample("ME").mean()

print("\n=== XPEV Monthly Summary ===")
print(monthly_summary.round(2))