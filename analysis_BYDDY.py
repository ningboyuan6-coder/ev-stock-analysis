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

#work item 5 for BYDDY: find significant price movements
close_byd = close["BYDDY"]
returns_byd = daily_returns["BYDDY"]

highest_close = close_byd.max()      #最高收盘价
highest_date  = close_byd.idxmax()   #最高收盘价日期
lowest_close  = close_byd.min()      #最低收盘价
lowest_date   = close_byd.idxmin()   #最低收盘价日期
big_gain      = returns_byd.max()        #最大单日涨幅
big_gain_date = returns_byd.idxmax()     #最大涨幅日期
big_drop      = returns_byd.min()        #最大单日跌幅
big_drop_date = returns_byd.idxmin()     #最大跌幅日期

print("\nHighest close:", round(highest_close, 2), "on", str(highest_date)[:10])
print("Lowest close: ", round(lowest_close, 2), "on", str(lowest_date)[:10])
print("Biggest gain (%):", round(big_gain, 2), "on", str(big_gain_date)[:10])
print("Biggest drop (%):", round(big_drop, 2), "on", str(big_drop_date)[:10])

# explanations & surpporting sources
#highest close on Apr 16
print("\n Explanations & Supporting Sources:")
print("\n[Why the highest close occurred on 2026-04-16]") 
print("The April 16 peak reflects several positive factors that built up from March onward:")

print("\n1. The Iran war pushed oil prices higher, boosting overseas EV demand")
print("evidence1: The U.S. and Israel attacked Iran on Feb 28, 2026; Iran then effectively blocked the Strait of Hormuz U.S. crude, around $70 before the conflict, spiked above $119 at times.")
print("evidence2: In early April a two-week U.S.-Iran ceasefire took hold, but the Strait had not fully reopened and Goldman Sachs warned Brent could average above $100 in 2026.")
print("evidence3: BYD's March overseas sales rose 65% to 120,083 units on the oil shock, but total deliveries still fell about 20%, so the growth came from overseas, not China.")


print("Source 1: https://www.pbs.org/newshour/world/oil-prices-spike-again-following-latest-standoff-in-the-strait-of-hormuz")
print("Source 2: https://oilprice.com/Latest-Energy-News/World-News/Goldman-Another-Month-of-Hormuz-Closure-Means-Over-100-Brent-Throughout-2026.html")
print("Source 3: https://www.bloomberg.com/news/articles/2026-04-01/byd-exports-jump-on-iran-oil-shock-as-domestic-slump-persists")

print("\n2. BYD raised its overseas target and pushed global expansion")
print("evidence1: BYD raised its 2026 overseas sales target from 1.3 million to 1.5 million vehicles (+15%),and won more orders than any other brand at the Bangkok Motor Show (ended Apr 5).")
print("evidence2: Bloomberg (Mar 13): BYD is studying a plant in Canada (no decision yet) and is open to acquiring a legacy automaker (no deal currently close).")

print("Source 1: https://electrek.co/2026/04/06/byd-ev-orders-surge-to-another-level-overseas-energy-crisis/")
print("Source 2: https://cnevpost.com/2026/03/13/byd-weighs-canada-plant-legacy-automaker-buyout/")


print("\n3. Technology and product news may have also helped BYD's stock")
print("evidence1: Mar 5: BYD unveiled its 2nd Generation Blade Battery and FLASH Charging technology with plans for 20,000 FLASH Charging stations in China by end-2026.")
print("evidence2: Apr 1-3: BYD Energy Storage showcased its full lineup in Beijing, featuring the Haohan system with a 2,710Ah storage blade cell (Haohan itself first launched in Sept 2025).")

print("Source 1: https://www.byd.com/za/news-list/byd-unveils-2nd-generation-blade-battery-and-flash-charging-technologyw")
print("Source 2: https://www.seetaoe.com/details/262022.html")
print("Source 3 (CnEVPost, Haohan launch): https://cnevpost.com/2025/09/19/byd-unveils-haohan-energy-storage-system/")


print("\n4. Why the stock did not keep rising after April 16")
print("evidence1: On Apr 17, Iran said it would reopen the Strait and crude plunged more than 9%, weakening the 'high oil prices help EVs' story.")
print("evidence2: BYD's Q1 2026 profit, reported in late April, fell 55.4% to RMB 4.09bn, and the stock pulled back.")
print("evidence3: The Hong Kong shares (1211.HK) peaked near HK$111.55 on Apr 17; BYDDY is an ADR that tracks them.")

print("Source 1: https://www.pbs.org/newshour/world/oil-prices-spike-again-following-latest-standoff-in-the-strait-of-hormuz")
print("Source 2: https://capital.com/en-int/market-updates/byd-forecast-08-05-2026")
print("Source 3: https://capital.com/en-int/market-updates/byd-stock-forecast-02-06-2026")

# the lowest close on 10.14
print("\n[Why the lowest close occurred on 2026-10-14]")
print("The October 14 low was the bottom of a steady downtrend, not the result of a single crash:")

print("\n1. Car sales in China kept falling, and BYD's stock was hit by the weak domestic market")
print("evidence1: China's NEV retail sales fell 16.7% year-on-year in September to 1.084 million, the ninth straight monthly decline.")
print("evidence2: BYD's Hong Kong shares had lost 35 percent over the past year amid a downturn in Chinese auto demand and excess supply.")

print("Source 1: https://cnevpost.com/2026/10/12/china-sept-2026-nev-retail-cpca/")
print("Source 2: https://www.forbes.com/sites/russellflannery/2026/10/04/byd-shareholders-pick-three-new-board-members-amid-stock-sales-drops/")

print("\n2. New policy unfavorable for exports which was announced days before the low")
print("evidence1: The EU will cap imports of Chinese hybrids and plug-in hybrids at 350,000 a year from as early as Dec 1, 2026, less than half of the roughly 800,000 expected to arrive in 2026.")
print("evidence2: On Oct 12, China announced it will cut the export VAT rebate for new energy vehicles from 13% to 9%, starting Apr 1, 2027.")
print("Source 1: https://www.automotiveworld.com/news/eu-caps-chinese-hybrids-at-350000-but-spares-local-plants/")
print("Source 2: https://fgk.chinatax.gov.cn/eng/c101269/c5252921/content.html")

print("\n3. Strong export numbers were overshadowed by worries about export profits")
print("evidence1: BYD's September sales rose 17% to 463,561, and overseas shipments of passenger vehicles and pickups jumped 153.9% to 179,877.")
print("evidence2: Yet on Oct 13, BYD's Hong Kong shares fell 2.8% to HK$72.25 as three headwinds hit at once: the EU cap on Chinese hybrid imports, China's cut to the NEV export tax rebate, and a JPMorgan price target reduction.")
print("evidence3: Analysts called the rebate cut relatively mild, but said it added uncertainty around BYD's export margins.")
print("Source 1: https://www.thestandard.com.hk/finance/article/344365/Chinas-BYD-sales-rise-in-September-as-export-boom-sustains-momentum")
print("Source 2: https://in.investing.com/news/stock-market-news/why-is-byd-stock-sliding-today-93CH-5629538")


#the biggest daily gain on 2026-7-01
print("\n[Why the biggest daily gain (+5.5%) occurred on 2026-07-01]")
print("The July 1 jump came from June sales numbers that BYD released that same day:")

print("\n1. BYD's sales grew again, two months in a row")
print("evidence1: On Jul 1, BYD reported in a stock filing that June sales rose 5.5% year-on-year to 403,472 vehicles.")
print("evidence2: May sales had risen 0.3%, the first increase in nine months, so June showed the recovery was real.")
print("Source 1: https://money.usnews.com/investing/news/articles/2026-07-01/byds-sales-rise-for-second-month-buoyed-by-exports")
print("Source 2: https://www.investing.com/news/stock-market-news/byd-reports-55-sales-increase-in-june-on-export-strength-93CH-4769872")
print("Source 3: https://www.bloomberg.com/news/articles/2026-06-01/byd-sales-rise-for-first-time-in-nine-months-on-overseas-demand")

print("\n2. Overseas sales hit a new record")
print("evidence1: Overseas sales jumped 94.7% year-on-year to a record 175,349 vehicles, making up for a 22 percent drop in China.")
print("Source 1: https://money.usnews.com/investing/news/articles/2026-07-01/byds-sales-rise-for-second-month-buoyed-by-exports")

print("\n3. The stock was bouncing back from a two-year low, and analysts turned more positive")
print("evidence1: Before the sales data came out, BYD's stock had fallen to its lowest level since September 2024.")
print("evidence2: Hong Kong shares jumped about 9% the next trading day (Jul 2); BYDDY trades during U.S. hours, so it reacted on Jul 1.")
print("evidence3: Deutsche Bank expected BYD's Q2 profit to rise 145 percent from Q1 to RMB 10 billion.")
print("Source 1: https://cnevpost.com/2026/07/02/byd-shares-rebound-sales-recovery/")
print("Source 2: https://www.cnbc.com/2026/07/02/china-ev-stocks-xiaomi-byd-june-deliveries-production.html")

#the biggest daily drop on 2026-8-31
print("\n[Why the biggest daily drop (-3.67%) occurred on 2026-08-31]")
print("The August 31 drop was the market reacting to half-year results that came in below expectations:")

print("\n1. Profit grew, but less than analysts expected")
print("evidence1: Q2 net profit rose about 30% to roughly RMB 8.2bn, BYD's first quarterly profit increase in five quarters.")
print("evidence2: But forecasts from Morgan Stanley, UBS, Citi, Deutsche Bank and CMBI averaged about RMB 9.4bn, so BYD came in roughly 12 percent below expectations. In July, Deutsche Bank had even forecast RMB 10bn.")
print("Source 1: https://eletric-vehicles.com/byd/byd-profit-rises-for-the-first-time-in-five-quarters-still-miss-forecasts-by-12/")
print("Source 2: https://www.cnbc.com/2026/07/02/china-ev-stocks-xiaomi-byd-june-deliveries-production.html")

print("\n2. BYD made less money in the first half of the year")
print("evidence1: On Aug 28, BYD reported H1 2026 revenue, but it blamed the profit drop mainly on foreign-exchange losses, weak demand in China, fierce competition and rising costs.")
print("evidence3: Aug 31 was the first trading day after the report; the Hong Kong shares fell 5.8% to HK$86.65.")
print("Source 1: https://www.cnbc.com/2026/08/31/byd-shares-slide-as-fierce-china-competition-dents-first-half-earnings.html")
print("Source 2: https://cnevpost.com/2026/08/28/byd-h1-2026-earnings/")
print("Source 3: https://in.investing.com/news/stock-market-news/byd-shares-drop-as-h1-profit-falls-on-tough-chinese-market-5576567")
print('\n===============================================================================================')
print("\n Summary of BYDDY stock analysis: on 4.16 BYD had the highest price, that because the High oil prices from the Iran war boosted BYD's overseas sales, and its higher export target and new technology lifted the stock to its peak on Apr 16. Oil prices then plunged on Apr 17 and Q1 profit fell sharply, so the stock never returned to that level.")
print("\nwhat's more, BYD's stock fell all year as car sales in China kept shrinking. Then, just days before Oct 14, the EU capped Chinese hybrid imports and China cut its export tax rebate, hitting exports, BYD's main growth engine. Even record export numbers could not lift the stock, because investors worried BYD would earn less from its overseas sales.")
print("\nIn contrast, on Jul 1, BYD reported a second straight month of sales growth and record overseas sales, which eased fears that its sales slump would continue. Coming right after the stock had fallen to a two-year low, the good news triggered a strong rebound, and analysts also became more optimistic about BYD's profits.")
print("\nBut reality fell short: Q2 profit, reported on Aug 28, rose about 30% yet came in about 12 percent below expectations, and first-half profit fell 20.5%. As a result, on the first trading day after the results (Aug 31), the stock posted its biggest one-day drop of the year.")

# Did volume support the moves?
if data["Volume"].ndim == 2:
    volume_data = data["Volume"]["BYDDY"]
else:
    volume_data = data["Volume"]

average_volume = volume_data.mean()
check_dates = ["2026-04-16", "2026-07-01", "2026-08-31", "2026-10-14"]

for single_date in check_dates:
    try:
        day_volume = volume_data.loc[single_date]
        relative_volume = day_volume / average_volume
        if relative_volume > 1:
            compare_text = "above"
        else:
            compare_text = "below"
        print(f"Volume on {single_date}: {relative_volume:.2f}({compare_text} average)")
    except KeyError:
        print(f"Volume data for {single_date} is not available.")

summary_text = """
So, the April 16 peak formed on slightly above-average volume, showing mild buying momentum pushing BYDDY to its highest price; the modestly heavy volume confirmed steady market enthusiasm for the outlook.
The July 1 rally came on above-average volume. The stronger volume backed the positive sales news, indicating investors were responding to the recovering monthly delivery data.
The Aug 31 drop came on below-average volume, suggesting a valuation adjustment rather than panic selling.
The Oct 14 low came on above-average volume, supporting the policy-driven sell-off.
"""
print(summary_text)
print("\n limitations: However, this analysis only shows the historical price and volume data consistent with the news, but attributing the single day's movement to  one or two news items is the inference but not definitive. Other factors may have contributed to the price changes, and correlation does not imply causation.") 


