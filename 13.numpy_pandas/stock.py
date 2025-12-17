import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf

def get_stock_data(ticker, start_date, end_date):
    data=yf.download(ticker, start=start_date,end=end_date)
    return data

def visualize_stock_data(stock_data, ticker):
    plt.figure(figsize=(12,6))
    plt.subplot(2,1,1)
    plt.plot(stock_data['Close'],label=ticker)
    plt.title(f"{ticker} Stock Price")
    plt.ylabel("Stock Price")
    plt.legend()

    plt.subplot(2,1,2)
    plt.bar(stock_data.index, stock_data['Volume'], label='Volume', color='orange')
    plt.title(f"{ticker} Volume")
    plt.ylabel("Volume")
    plt.ylabel("Date")
    plt.legend(loc="best")

    ma_5=stock_data["Close"].rolling(window=5).mean()
    ma_20=stock_data["Close"].rolling(window=20).mean()
    plt.subplot(2,1,1)
    plt.plot(ma_5, label='5 MMA',linestyle='dashed')
    plt.plot(ma_20, label='20 MMA',linestyle='dashed')
    plt.legend(loc='best')

    plt.tight_layout()
    plt.show()

ticker="AAPL"
start_date="2022-01-01"
end_date="2023-01-01"
stock_data=get_stock_data(ticker, start_date, end_date)
visualize_stock_data(stock_data, ticker)