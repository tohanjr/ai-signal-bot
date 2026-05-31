from flask import Flask
import threading
import schedule
import time

from strategy import generate_signal
from telegram_bot import send_signal

app = Flask(__name__)

last_signal = None

def bot_loop():

    global last_signal

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
'''

            send_signal(message)

            last_signal = signal

    schedule.every(15).minutes.do(job)

    while True:
        schedule.run_pending()
        time.sleep(1)

@app.route('/')

def home():
    return "AI Signal Bot Running"

threading.Thread(target=bot_loop).start()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
