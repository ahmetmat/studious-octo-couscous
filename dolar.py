import requests
import json

base_url = 'https://api.coingecko.com/api/v3'

endpoint = '/coins/tether?localization=false&tickers=false&market_data=true&community_data=false&developer_data=false&sparkline=false'

response = requests.get(base_url + endpoint)
data = json.loads(response.text)

def valuePrinter():
    print('USDT/TRY: ', usdt_try_value)
    print('14 gün değişim yüzdesi: ', usdt_try_change_percentage)

if 'market_data' in data and 'price_change_percentage_14d' in data['market_data']:
    usdt_try_value = data['market_data']['current_price']['try']
    usdt_try_change_percentage = data['market_data']['price_change_percentage_14d']
    valuePrinter()
else:
    print('API yanıtında beklenen anahtarlar mevcut değil.')
