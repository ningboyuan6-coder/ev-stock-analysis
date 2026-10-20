import yfinance as yf
import pandas as pd

ticker = "TSLA"
start_date = "2026-04-15"
end_date = "2026-10-15"

data = yf.download(
    ticker,
    start=start_date,
    end=end_date,
    auto_adjust=True,
    progress=False
)

print("Tesla (TSLA) Stock Data")
print("Start Date:", start_date)
print("End Date:", end_date)

if data.empty:
    print("No data returned for the selected date range.")
else:
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