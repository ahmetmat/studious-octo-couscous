import requests
import dolar
import graphics

# Mina CoinGecko API'sının URL'si ve parametreleri
mina_url = "https://api.coingecko.com/api/v3/coins/mina-protocol"
mina_params = {
    "tickers": "false",
    "market_data": "true",
    "community_data": "false",
    "developer_data": "false",
    "sparkline": "false"
}

# Mana CoinGecko API'sının URL'si ve parametreleri
mana_url = "https://api.coingecko.com/api/v3/coins/decentraland"
mana_params = {
    "tickers": "false",
    "market_data": "true",
    "community_data": "false",
    "developer_data": "false",
    "sparkline": "false"
}

# Mina CoinGecko API'sından veri al
mina_response = requests.get(mina_url, params=mina_params)

# Alınan veriyi JSON formatına dönüştür
mina_data = mina_response.json()

# Mina fiyatını ve 24 saatlik değişim oranını al
mina_price = mina_data["market_data"]["current_price"]["try"]
mina_percent_change_24h = mina_data["market_data"]["price_change_percentage_24h"]

# Mana CoinGecko API'sından veri al
mana_response = requests.get(mana_url, params=mana_params)

# Alınan veriyi JSON formatına dönüştür
mana_data = mana_response.json()

# Mana fiyatını ve 24 saatlik değişim oranını al
mana_price = mana_data["market_data"]["current_price"]["try"]
mana_percent_change_24h = mana_data["market_data"]["price_change_percentage_24h"]

# Fiyat bilgilerini ve değişim oranlarını yazdır
print("Mina fiyatı: ", mina_price, "TRY")
print("Mina 24 saatlik değişim oranı: ", mina_percent_change_24h, "%")
print("Mana fiyatı: ", mana_price, "TRY")
print("Mana 24 saatlik değişim oranı: ", mana_percent_change_24h, "%")

if(mana_percent_change_24h<mina_percent_change_24h):

    print("Mana alımı yapılabilir")
else:
    print("mina alımı yapılabilir")

dolar.valuePrinter()

