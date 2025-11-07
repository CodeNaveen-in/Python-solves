import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.dates import MonthLocator, DateFormatter

def load_and_prepare(file, date_col="Date"):
    df = pd.read_csv(file, parse_dates=[date_col])
    df.set_index(date_col, inplace=True)
    return df

def plot_dual_axis(df1, df2, label1, label2, title):
    fig, ax1 = plt.subplots(figsize=(12, 6))
    ax2 = ax1.twinx()

    ax1.plot(df1.index, df1.iloc[:, 0], color="tab:blue", label=label1, marker="o", linestyle="--")
    ax2.plot(df2.index, df2.iloc[:, 0], color="tab:red", label=label2, marker="s", linestyle="-")

    ax1.set_xlabel("Date")
    ax1.set_ylabel(label1, color="tab:blue")
    ax2.set_ylabel(label2, color="tab:red")
    ax1.set_title(title)
    ax1.grid(True)
    ax1.xaxis.set_major_locator(MonthLocator())
    ax1.xaxis.set_major_formatter(DateFormatter("%b %Y"))

    fig.tight_layout()
    plt.show()

# Load datasets
bitcoin_price = load_and_prepare("bitcoin_price.csv")
bitcoin_trends = load_and_prepare("bitcoin_trends.csv")
tesla_price = load_and_prepare("tesla_price.csv")
tesla_trends = load_and_prepare("tesla_trends.csv")
unemp_rate = load_and_prepare("unemployment_rate.csv")
unemp_trends = load_and_prepare("unemployment_trends.csv")

# Check for missing values
for name, df in [("Bitcoin", bitcoin_price), ("Tesla", tesla_price), ("Unemployment", unemp_rate)]:
    print(f"🔍 Missing values in {name}: {df.isna().sum().sum()}")

# Plot comparisons
plot_dual_axis(bitcoin_price, bitcoin_trends, "Bitcoin Price (USD)", "Search Volume", "Bitcoin Price vs Google Search Volume")
plot_dual_axis(tesla_price, tesla_trends, "Tesla Stock Price (USD)", "Search Volume", "Tesla Stock vs Google Search Volume")
plot_dual_axis(unemp_rate, unemp_trends, "Unemployment Rate (%)", "Search Volume", "Unemployment Rate vs Google Search Volume")