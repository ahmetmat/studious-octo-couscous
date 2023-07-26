import requests
import statistics as stats

def z_skoruFunc(coinSymbol):
    days = input("Lütfen zaman aralığını girin (örn: 30): ")

    url = f"https://api.coingecko.com/api/v3/coins/{coinSymbol}/market_chart?vs_currency=usd&days={days}"
    headers = {
        "Accepts": "application/json",
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()

        prices = [item[1] for item in data['prices']]
        
        mean_price = stats.mean(prices)
        stdev_price = stats.stdev(prices)

        last_price = prices[-1]
        z_score = (last_price - mean_price) / stdev_price

        print(f"{coinSymbol} kripto para biriminin son {days} günlük z skoru: {z_score}")
        if(z_score>1):
            print(f"Son {days} güne bakıldığında alım baskısı gözükmektedir.")
        else:
            print(f"Son {days} güne bakıldığında geri çekilme gözüküyor.")
            
    else:
        print(f"Hata: API'den veri alınamadı. Durum kodu: {response.status_code}")
