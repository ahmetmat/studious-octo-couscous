import requests

def get_rsi(coinSymbol):

    url = f"https://api.coingecko.com/api/v3/coins/{coinSymbol}/market_chart?vs_currency=usd&days=14"
    headers = {
        "Accepts": "application/json",
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()

        prices = [item[1] for item in data['prices']]

        def calculate_rsi(prices, n=14):
            deltas = [prices[i + 1] - prices[i] for i in range(len(prices) - 1)]
            gains = [d if d > 0 else 0 for d in deltas]
            losses = [-d if d < 0 else 0 for d in deltas]
            avg_gain = sum(gains[:n]) / n
            avg_loss = sum(losses[:n]) / n
            rs = avg_gain / avg_loss
            rsi = 100 - (100 / (1 + rs))
            return rsi

        # 14 günlük RSI hesaplaması
        rsi_14d = calculate_rsi(prices)

        # Son 24 saat fiyat verilerinin alınması
        prices_24h = prices[-24:]

        # 24 saatlik RSI hesaplaması
        rsi_24h = calculate_rsi(prices_24h, n=24)
        print("---------------")
        print(f"14 günlük RSI: {rsi_14d:.2f}")
        print("---------------")
        # 14 günlük RSI değerine göre açıklama
        if rsi_14d >= 70:
            print(f"{coinSymbol} aşırı alım koşullarında. Fiyat düşüşü bekleniyor.")
        elif rsi_14d <= 30:
            print(f"{coinSymbol} aşırı satım koşullarında. Fiyat artışı bekleniyor.")
        elif rsi_14d == 50:
            print(f"{coinSymbol} için nötr bir durum gözlemleniyor.")
        elif rsi_14d < 50:
            print(f"{coinSymbol} düşüş trendinde.")
        elif rsi_14d > 50:
            print(f"{coinSymbol} yükseliş trendinde.")
        print("---------------")
        print(f"Son 24 saatlik RSI: {rsi_24h:.2f}")
        print("---------------")
        # 24 saatlik RSI değerine göre açıklama
        if rsi_24h >= 70:
            print(f"{coinSymbol} son 24 saat içinde aşırı alım koşullarında. Fiyat düşüşü bekleniyor.")
        elif rsi_24h <= 30:
            print(f"{coinSymbol} aşırı satım koşullarında. Fiyat artışı bekleniyor.")
        elif rsi_24h == 50:
            print(f"{coinSymbol} için nötr bir durum gözlemleniyor.")
        elif rsi_24h < 50:
            print(f"{coinSymbol} düşüş trendinde.")
        elif rsi_24h > 50:
            print(f"{coinSymbol} yükseliş trendinde.")
