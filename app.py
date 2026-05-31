import schedule
import time

from strategy import generate_signal
from telegram_bot import send_signal

last_signal = None

def job():

    global last_signal

    signal, price = generate_signal()

    if signal and signal != last_signal:

        message = f'''
🚨 AI SIGNAL ALERT 🚨

Signal: {signal}
Price: {price}

Pair: BTC/USDT
Timeframe: 15m

Powered by AI
'''

        send_signal(message)

        last_signal = signal

schedule.every(15).minutes.do(job)

while True:

    schedule.run_pending()

    time.sleep(1)
