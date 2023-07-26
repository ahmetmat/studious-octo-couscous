import schedule
import time
import requests

def get_EMA100():
    url = "https://scanner.tradingview.com/crypto/scan"

    payload = {
        "symbols": {
            "tickers": ["BINANCE:MINAUSD"],
            "query": {
                "types": []
            }
        },
        "columns": [
            "EMA100"
        ]
    }

    response = requests.post(url, json=payload)

    if response.status_code == 200:
        data = response.json()

        if "data" in data:
            ema100 = data["data"][0]["d"][0]
            print(f"EMA100 değeri: {ema100}")
            print("calıstı")

        else:
            print("Teknik veriler bulunamadı.")

    else:
        print(f"Hata: API'den veri alınamadı. Durum kodu: {response.status_code}")

schedule.every(5).seconds.do(get_EMA100)

while True:
    schedule.run_pending()
    time.sleep(1)
