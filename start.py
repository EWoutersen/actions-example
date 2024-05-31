import requests

headers = {
    'Sec-Fetch-Site': 'same-site',
    'Accept': 'application/json, text/plain, */*',
    'Origin': 'https://www.greggs.co.uk',
    'Sec-Fetch-Dest': 'empty',
    'Accept-Language': 'nl-NL,nl;q=0.9',
    'Sec-Fetch-Mode': 'cors',
    'Host': 'production-digital.greggs.co.uk',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.3 Safari/605.1.15',
    'Referer': 'https://www.greggs.co.uk/',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Connection': 'keep-alive',
}

params = {
    'latitude': '52.4822694',
    'longitude': '-1.8900078',
    'distanceInMeters': '48024',
}

response = requests.get('https://production-digital.greggs.co.uk/api/v1.0/shops', params=params, headers=headers)

print(response.text)
