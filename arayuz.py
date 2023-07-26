import requests

def technical_analyze():
    coin_name = input("Coin adını girin: ")
    coin_name = coin_name.upper()

    print(coin_name)

    url = "https://scanner.tradingview.com/crypto/scan"

    payload = {
        "symbols": {
            "tickers": [f"KRAKEN:{coin_name}USD"],
            "query": {
                "types": []
            }
        },
        "columns": [
            "Recommend.Other",
            "Recommend.All",
            "Recommend.MA",
            "RSI",
            "RSI[1]",
            "Stoch.K"
        ]
    }

    response = requests.post(url, json=payload)

    if response.status_code == 200:
        data = response.json()

        if "data" in data:
            technicals = data["data"]

            for technical in technicals:
                stoch_k_value = technical['d'][5]
                print(stoch_k_value)

                if 20 < stoch_k_value < 80:
                    print("Stoch.K verilerine göre herşey yolunda")
                elif stoch_k_value > 80:
                    print("Aşırı alım mevcut, fiyat düzeltmesi gelebilir.")
                else:
                    print("Aşırı satım mevcut, fiyat yükselmesi gelebilir.")

        else:
            print("Teknik veriler bulunamadı.")

    else:
        print(f"Hata: API'den veri alınamadı. Durum kodu: {response.status_code}")


technical_analyze()
