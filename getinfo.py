import requests
from rsi import get_rsi
from ema100 import getEma100

def get_coin_info(coin_name):
    
    url = f"https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids={coin_name}"
    headers = {
        "Accepts": "application/json",
        "User-Agent": "Mozilla/5.0"
    }
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Hata durumunda hata yükseltme
    except requests.exceptions.HTTPError as err:
        print(text=f"Hata: {err}")
        return
    except requests.exceptions.Timeout:
        print(text="Hata: İstek zaman aşımına uğradı.")
        return
    except requests.exceptions.RequestException as err:
        print(text=f"Hata: {err}")
        return

    
    try:
        data = response.json()
    except ValueError:
        print(text="Hata: JSON verisi çözümlenemedi.")
        return

    if len(data) == 0:
        print(f"{coin_name} için veri bulunamadı.")
        return

    try:
        price = data[0]["current_price"]
        percent_change_24h = data[0]["price_change_percentage_24h"]
        symbol = data[0]["symbol"].upper()
        coinPricePrinter(coin_name,symbol,price,percent_change_24h)

    except KeyError:
        print(f"{coin_name} için gerekli veri bulunamadı.")

def coinPricePrinter(coin_name,symbol,price,percent_change_24h):
    print("---------------")
    print(f"{coin_name} ({symbol}) fiyatı: {price} USD\n{coin_name} 24 saatlik değişim oranı: %{percent_change_24h}")
    print("---------------")
