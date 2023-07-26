import sys
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

def getgraphics(coin_name, data, prices):
    prices = [p[1] for p in data["usd_price"]]
    timestamps = [datetime.fromtimestamp(p[0] / 1000) for p in data["usd_price"]]
    plt.plot(timestamps, prices)
    plt.title(f"{coin_name} Fiyat Değişimi (Son 30 Gün)")
    plt.xlabel("Tarih")
    plt.ylabel("Fiyat (USD)")
    plt.show()