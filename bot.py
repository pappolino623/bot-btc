import pandas as pd
import time
import os
from strategy import crossover_strategy
from binance_client import fetch_ohlcv, place_order
from dotenv import load_dotenv

load_dotenv()

symbol = os.getenv("TRADE_SYMBOL")
fraction = float(os.getenv("TRADE_AMOUNT_PERCENT"))

def run_bot():
    while True:
        ohlcv = fetch_ohlcv(symbol)
        df = pd.DataFrame(ohlcv, columns=['timestamp','open','high','low','close','volume'])
        signal = crossover_strategy(df)
        print(f"Señal actual: {signal}")

        if signal:
            order = place_order(symbol, signal, trade_fraction=fraction)
            print("Orden ejecutada:", order)

        time.sleep(15 * 60)

if __name__ == "__main__":
    run_bot()
