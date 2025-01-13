import yfinance as yf
import matplotlib.pyplot as plt

def get_stock_info(stock_name):
    try:
        stock=yf.Ticker(stock_name)
        stock_info=stock.info
        current_price = stock_info.get('currentPrice')
        pe_ratio = stock_info.get('trailingPE')
        sector = stock_info.get('sector')
        dividend_yield = stock_info.get('dividendYield', 0)
        
        print(f"\nStock name: {stock_info.get('longName', stock_name)}")
        print(f"Sector: {sector}")
        print(f"Current Stock Price: {current_price}")
        print(f"P/E Ratio: {pe_ratio}")
        print(f"Dividend Yield: {dividend_yield}")
        
        print("\nEvaluation:")
        if current_price and pe_ratio:
            if pe_ratio < 20:
                print("The stock has a healthy and average P/E - Price to earning ratio. It might be a good stock to invest on.")
            elif pe_ratio > 30:
                print("The stock's P/E - Price to earning ratio is high. Consider researching further.")
            else:
                print("The stock's P/E Price to earning ratio is moderate. Analyze trends and look into its fundamentals.")
        else:
            print("Insufficient data to find the P/E ratio.")
        
        if dividend_yield and dividend_yield > 0.02:
            print("This stock offers a decent and normal dividend yield.")
        else:
            print("This stock has a low or no dividend yield. Consider investing as it usually has growth potential.")
        
        plot_stock_history(stock_name)
        
    except Exception as e:
        print(f"Error fetching stock information: {e}")

def plot_stock_history(stock_name):
    try:
        print("\nFetching data for the past 5 years...")
        historical_data = yf.download(stock_name, period="5y")
        if historical_data.empty:
            print("Unable to fetch historical data.")
            return
        
        plt.figure(figsize=(10, 6))
        plt.plot(historical_data['Close'], label="Close Price", color="blue")
        plt.title(f"{stock_name} - Stock Price (Last 5 Years)")
        plt.xlabel("Date")
        plt.ylabel("Close Price (in currency)")
        plt.grid(True)
        plt.legend()
        plt.show()
        
    except Exception as e:
        print(f"Error plotting historical data: {e}")

def main():
    print("Welcome to the fAInance advisor! Please note that this model is only for demonstration purposes and can only be used in low level investing. Use at your own risk.")
    stock_name = input("Enter the stock symbol to evaluate. {AAPL, TSLA, INFY.BO): ").strip()
    get_stock_info(stock_name)

if __name__ == "__main__":
    main()