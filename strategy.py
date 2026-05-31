import ccxt
import pandas as pd

from indicators import analyze_indicators

exchange = ccxt.binance()

def fetch_data(symbol='BTC/USDT', timeframe='15m', limit=200):

    ohlcv = exchange.fetch_ohlcv(symbol, timeframe, limit=limit)

    df = pd.DataFrame(
        ohlcv,
        columns=['timestamp', 'open', 'high', 'low', 'close', 'volume']
    )

    return df

def generate_signal():

    df = fetch_data()

    signal = analyze_indicators(df)

    price = df.iloc[-1]['close']

    return signal, price
