import requests
import matplotlib.pyplot as plt
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class StockPriceTracker:
    def __init__(self, root):
        self.root = root
        self.root.title("Stock Price Tracker")

        self.label_symbol = tk.Label(root, text="Enter stock symbol:")
        self.entry_symbol = tk.Entry(root)
        self.button_fetch = tk.Button(root, text="Fetch and Plot", command=self.fetch_and_plot)
        self.figure = plt.figure(figsize=(10, 6))
        self.canvas = FigureCanvasTkAgg(self.figure, master=root)

        self.label_symbol.pack(pady=5)
        self.entry_symbol.pack(pady=5)
        self.button_fetch.pack(pady=10)
        self.canvas.get_tk_widget().pack()

        self.api_key = '6G74MZJ7UB5T8V3G'

    def fetch_stock_data(self):
        stock_symbol = self.entry_symbol.get().upper()
        url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={stock_symbol}&apikey={self.api_key}"

        try:
            response = requests.get(url)
            data = response.json()

            if 'Time Series (Daily)' not in data:
                print("Error: Unable to fetch stock data. Check your API request or stock symbol.")
                return None

            daily_data = data['Time Series (Daily)']
            dates = list(daily_data.keys())
            prices = [float(entry['4. close']) for entry in daily_data.values()]
            return stock_symbol, dates, prices
        except requests.exceptions.RequestException as e:
            print("Error: Unable to fetch stock data. Check your network connection.")
            return None

    def plot_stock_data(self):
        stock_symbol, dates, prices = self.fetch_stock_data()

        if stock_symbol and dates and prices:
            self.figure.clear()
            plt.plot(dates, prices, marker='o')
            plt.xlabel('Date')
            plt.ylabel('Price')
            plt.title(f'Daily Stock Price for {stock_symbol}')
            plt.xticks(rotation=45)
            self.canvas.draw()

    def fetch_and_plot(self):
        self.plot_stock_data()

if __name__ == "__main__":
    root = tk.Tk()
    app = StockPriceTracker(root)
    root.mainloop()
