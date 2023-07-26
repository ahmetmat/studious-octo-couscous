import requests

# CoinGecko'nun API'si için base URL
base_url = 'https://api.coingecko.com/api/v3'

# Kullanıcıdan coin adını al
coin_name = input("Coin adını girin: ")

# CoinGecko API'sinde coin ara
search_endpoint = '/coins/list'
search_params = {'include_platform': 'false'}

response = requests.get(base_url + search_endpoint, params=search_params)
data = response.json()

coin_id = ''
for coin in data:
    if coin['name'] == coin_name:
        coin_id = coin['id']
        break

if coin_id == '':
    print("Coin bulunamadı")
    exit()

price_endpoint = f'/coins/{coin_id}'
price_params = {
    'localization': 'false',
    'tickers': 'false',
    'market_data': 'true',
    'community_data': 'false',
    'developer_data': 'false',
    'sparkline': 'false'
}

response = requests.get(base_url + price_endpoint, params=price_params)
data = response.json()

usd_price = data['market_data']['current_price']['usd']
try_price = data['market_data']['current_price']['try']
btc_price = data['market_data']['current_price']['btc']
usd_percent_change_24h = data['market_data']['price_change_percentage_24h']
try_percent_change_24h = data['market_data']['price_change_percentage_24h_in_currency']['try']
btc_percent_change_24h = data['market_data']['price_change_percentage_24h_in_currency']['btc']

print(f"{coin_name} fiyatı:")
print(f"USD: {usd_price}")
print(f"TRY: {try_price}")
print(f"BTC: {btc_price}")
print(f"24 saatlik değişim oranı:")
print(f"USD: {usd_percent_change_24h}%")
print(f"TRY: {try_percent_change_24h}%")
print(f"BTC: {btc_percent_change_24h}%")
