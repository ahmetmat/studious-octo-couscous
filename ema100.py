import requests

def getEma100(coinSymbol):

    url = f"https://api.coingecko.com/api/v3/coins/{coinSymbol}/market_chart?vs_currency=usd&days=365"

    headers = {
        "Accepts": "application/json",
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()

        prices = [item[1] for item in data['prices']]

        def calculate_ema(prices, n=100):
            ema = []
            j = 1
            sma = sum(prices[:n]) / n
            multiplier = 2 / (n + 1)
            ema.append(sma)

            for i in prices[n:]:
                ema.append((i - ema[j - 1]) * multiplier + ema[j - 1])
                j += 1
            return ema[-1]

        ema100 = calculate_ema(prices)

        current_price = prices[-1]

        print(f"{coinSymbol} EMA100 değeri: {ema100}")

        if ema100 > current_price:
            print("---------------")
            print(f"{coinSymbol} EMA100 değeri mevcut fiyattan büyük, fiyat düşebilir.")
            print("---------------")

        else:
            print("---------------")
            print(f"{coinSymbol} EMA100 değeri mevcut fiyattan küçük, fiyat yükselebilir.")
            print("---------------")
    else:
        print("---------------")
        print(f"Hata: API'den veri alınamadı. Durum kodu: {response.status_code}")
        print("---------------")