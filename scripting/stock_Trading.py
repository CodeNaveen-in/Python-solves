import tkinter as tk
import requests
import html
from tkinter import messagebox

# ---------------------------- CONFIG ------------------------------- #
FMP_API_KEY = "your_fmp_api_key"
MARKETAUX_API_KEY = "your_marketaux_api_key"
STOCK_SYMBOL = "AAPL"

# ---------------------------- FETCH STOCK DATA ------------------------------- #
def get_stock_price():
    try:
        url = f"https://financialmodelingprep.com/api/v3/quote/{STOCK_SYMBOL}?apikey={FMP_API_KEY}"
        response = requests.get(url)
        data = response.json()
        price = data[0]["price"]
        change = data[0]["changePercent"]
        return price, change
    except Exception as e:
        messagebox.showerror("Error", f"Failed to fetch stock data:\n{e}")
        return None, None

# ---------------------------- FETCH NEWS DATA ------------------------------- #
def get_stock_news():
    try:
        url = f"https://api.marketaux.com/v1/news/all?symbols={STOCK_SYMBOL}&filter_entities=true&api_token={MARKETAUX_API_KEY}"
        response = requests.get(url)
        articles = response.json()["data"]
        return [html.unescape(article["title"]) for article in articles[:5]]
    except Exception as e:
        messagebox.showerror("Error", f"Failed to fetch news:\n{e}")
        return []

# ---------------------------- UPDATE UI ------------------------------- #
def update_data():
    price, change = get_stock_price()
    news = get_stock_news()

    if price is not None:
        price_label.config(text=f"Price: ${price:.2f} ({change:.2f}%)")
    news_box.delete(0, tk.END)
    for headline in news:
        news_box.insert(tk.END, headline)

# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title("📊 Stock News Trader")
window.config(padx=30, pady=30, bg="#f0f4f8")

tk.Label(text=f"📈 {STOCK_SYMBOL} Stock Tracker", font=("Segoe UI", 20, "bold"), bg="#f0f4f8").pack(pady=10)
price_label = tk.Label(text="Loading...", font=("Segoe UI", 14), bg="#f0f4f8")
price_label.pack(pady=5)

news_box = tk.Listbox(width=60, height=10, font=("Segoe UI", 12))
news_box.pack(pady=10)

refresh_button = tk.Button(text="🔄 Refresh", font=("Segoe UI", 12), command=update_data)
refresh_button.pack(pady=10)

update_data()
window.mainloop()