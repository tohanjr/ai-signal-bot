import ta

def analyze_indicators(df):

    df['rsi'] = ta.momentum.RSIIndicator(df['close']).rsi()

    macd = ta.trend.MACD(df['close'])

    df['macd'] = macd.macd()
    df['macd_signal'] = macd.macd_signal()

    latest = df.iloc[-1]

    signal = None

    if latest['rsi'] < 30 and latest['macd'] > latest['macd_signal']:
        signal = "BUY"

    elif latest['rsi'] > 70 and latest['macd'] < latest['macd_signal']:
        signal = "SELL"

    return signal
