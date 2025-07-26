import ccxt
import os

api_key = os.getenv("BINANCE_API_KEY")
api_secret = os.getenv("BINANCE_API_SECRET")

exchange = ccxt.binance({
    'apiKey': api_key,
    'secret': api_secret,
    'enableRateLimit': True
})

def fetch_ohlcv(symbol, timeframe='15m', limit=50):
    return exchange.fetch_ohlcv(symbol, timeframe=timeframe, limit=limit)

def get_balance(asset):
    return exchange.fetch_balance()['total'][asset]

def place_order(symbol, signal, trade_fraction=10):
    price = exchange.fetch_ticker(symbol)['last']
    usdt_balance = get_balance('USDT')
    btc_balance = get_balance('BTC')

    if signal == 'buy':
        amount = (usdt_balance * trade_fraction / 100) / price
        return exchange.create_market_buy_order(symbol, amount)
    elif signal == 'sell':
        amount = btc_balance * trade_fraction / 100
        return exchange.create_market_sell_order(symbol, amount)
