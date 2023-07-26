import requests
from rsi import get_rsi
from ema100 import getEma100
from getinfo import get_coin_info
from z_skoru import z_skoruFunc
import time

while True:
    coinSymbol = input("Search a crypto technics: ").lower()

    get_coin_info(coinSymbol)
    getEma100(coinSymbol)
    get_rsi(coinSymbol)
    print("---------------")
    z_skoruFunc(coinSymbol)
    print("---------------")    
    time.sleep(15)
