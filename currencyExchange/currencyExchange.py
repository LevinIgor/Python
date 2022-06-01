import requests
import sys
import math


def get_rates(currency):
    response = requests.get(f'http://www.floatrates.com/daily/{currency}.json')
    if response.status_code == 200:
        return response
    else:
         print('-----------Error currency not found-------------')
         sys.exit()

IN_CURRENCY = input('Input currency: ')
CURRENCY_LIST = get_rates(IN_CURRENCY)

while True:
    
    TO_CURRENCY = input('Input currency: ')
    if TO_CURRENCY == '':
        sys.exit()
    if TO_CURRENCY not in CURRENCY_LIST.json():  
        print('-----------Error currency not found-------------')
        sys.exit()
    
    cache = input('Input cache: ')
    if not cache.isnumeric():
        print('-----------Error cache not a number-------------')

    print('Finally cache:',round(float(CURRENCY_LIST.json()[TO_CURRENCY]['rate']) * float(cache),2), TO_CURRENCY.upper())