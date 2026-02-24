import yfinance as yf
from plyer import notification
import time


symbol = "BTC-USD"  
target_price = 100000 

def check_price():
    data = yf.Ticker(symbol)
    curr_price = data.history(period="1d")['Close'].iloc[-1]
    
    if curr_price >= target_price:
        notification.notify(
            title=f"target hit: {symbol}",
            message=f"current price is ${curr_price:.2f}!",
            timeout=10
        )
    print(f"checked {symbol}: ${curr_price:.2f}")


while True:
    check_price()
    time.sleep(3600)