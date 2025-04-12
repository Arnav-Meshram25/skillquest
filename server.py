from flask import Flask, jsonify
from flask_cors import CORS
import yfinance as yf
from datetime import datetime, timedelta

app = Flask(__name__)
CORS(app)

@app.route("/data")
def get_candlestick_data():
    ticker = 'AAPL'  # You can change this to any reliable stock
    end_date = datetime.now()
    start_date = end_date - timedelta(days=30)

    data = yf.download(ticker, start=start_date.strftime('%Y-%m-%d'),
                       end=end_date.strftime('%Y-%m-%d'), interval='1d')

    candlesticks = []
    for idx, row in data.iterrows():
        candlesticks.append({
            "time": idx.strftime('%Y-%m-%d'),
            "open": round(row['Open'], 2),
            "high": round(row['High'], 2),
            "low": round(row['Low'], 2),
            "close": round(row['Close'], 2)
        })

    return jsonify(candlesticks)

if __name__ == "__main__":
    app.run(debug=True)
