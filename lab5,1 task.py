import requests


WEDSITE = 'https://my.itmo.ru/'

response = requests.get(WEDSITE)
if response.status_code == 200:
    print('Success!')
