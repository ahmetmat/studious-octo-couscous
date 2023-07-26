import requests
from graphics import getgraphics

# CoinMarketCap API'si için base URL
base_url = 'https://pro-api.coinmarketcap.com/v1'

# Private Api Key
api_key = 'private api key'

# Kullanıcıdan coin adını al
coin_name = input("Coin adını girin: ")

# CoinMarketCap API'sine istek yapmak için headers belirleyin
headers = {
    'X-CMC_PRO_API_KEY': api_key
}

# CoinMarketCap API'sinde coin ara
quote_endpoint = '/cryptocurrency/quotes/latest'
quote_params = {
    'symbol': coin_name.upper()  # CoinMarketCap API'si için coin sembolü genellikle büyük harflerle gönderilir
}

response = requests.get(base_url + quote_endpoint, params=quote_params, headers=headers)
data = response.json()

# Eşleşen coin bulunamazsa programı sonlandır
if 'data' not in data or data['data'] == {}:
    print("Coin bulunamadı")
    exit()

# Coin'in CoinMarketCap ID'sini al
coin_id = list(data['data'].keys())[0]

# CoinMarketCap API'sinden alınan veri yapısına göre doğru fiyat bilgilerini al
usd_price = data['data'][coin_id]['quote']['USD']['price']
usd_percent_change_24h = data['data'][coin_id]['quote']['USD']['percent_change_24h']

# Fiyat bilgilerini ve değişim oranlarını yazdır
print(f"{coin_name} fiyatı:")
print(f"USD: {usd_price}")
print(f"24 saatlik değişim oranı:")
print(f"USD: {usd_percent_change_24h}%")

getgraphics(coin_name,data,usd_price)